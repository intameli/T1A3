from chapters import chapters
from string import ascii_uppercase
from random import randint
from entities import Player, Enemy

tile_options = []
vowels = ['A', 'E', 'I', 'O', 'U']
for c in ascii_uppercase:
    char = c
    if c == 'Q':
        char = 'Qu'
    tile_options.append(char)
    if char in vowels:
        tile_options.append(char)
    # if char in ['X','Z','Qu','K','J']:
    #     tile_options.extend([char] * 2)
    # elif char in ['B', 'C', 'F', 'H', 'M', 'P', 'V','W','Y']:
    #     tile_options.extend([char] * 3)
    # else:
    #     tile_options.extend([char] * 4)
# print(tile_options)


def load_words():
    with open('wordlist.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words


if __name__ == '__main__':
    english_words = load_words()


class Game:
    def __init__(self):
        self.running = True
        self.tiles = [self.rand_tile() for i in range(16)]
        self.player = Player()
        self.chapters_i = 0
        self.curr_chapter = chapters[self.chapters_i]
        self.enemy_arr = [Enemy(**e, player=self.player)
                          for e in self.curr_chapter['enemies']]
        self.enemy_i = 5
        self.curr_enemy = self.enemy_arr[self.enemy_i]

    def next_enemy(self):
        print(f'You defeated {self.curr_enemy.name}')

        if self.enemy_i == len(self.enemy_arr) - 1:
            if self.chapters_i == len(chapters) - 1:
                print('You beat the game, congratulations!')
                self.running = False
                return
            getattr(self.player, self.curr_chapter['treasure'])()
            self.chapters_i += 1
            self.curr_chapter = chapters[self.chapters_i]
            self.enemy_i = 0
            self.enemy_arr = [Enemy(**e, player=self.player)
                              for e in self.curr_chapter['enemies']]
        else:
            self.enemy_i += 1

        self.curr_enemy = self.enemy_arr[self.enemy_i]
        print(f'{self.curr_enemy.name} appears before you')

    def rand_tile(self):
        i = randint(0, len(tile_options) - 1)
        return tile_options[i]

    def print_UI(self):
        print(self.curr_enemy.name)
        print(f'Health: {self.player.health}  '
              f'Enemy Health: {self.curr_enemy.health}'
              )
        for j in range(4):
            row = ''
            for i in range(4):
                tile = self.tiles[(j * 4) + i]
                row += tile + '  ' if len(tile) == 1 else tile + ' '
            print(row)

    def valid_tiles(self, player_input):
        tiles_copy = self.tiles.copy()
        valid = True
        arr = []
        for i, c in enumerate(player_input):
            char = c
            if c == 'Q' and player_input[i + 1] == 'U':
                char = 'Qu'
            if c == 'U' and player_input[i - 1] == 'Q':
                continue
            if char in tiles_copy:
                tiles_copy.remove(char)
                arr.append(char)
            else:
                arr = []
                break
        return arr

    def get_input(self):
        # error handling for numbers?
        while True:
            player_input = input("text: ").upper()
            input_arr = self.valid_tiles(player_input)
            if player_input == '/QUIT':
                self.running = False
                break
            elif player_input == '/SCRAMBLE':
                self.tiles = [self.rand_tile() for i in range(16)]
                break
            elif len(input_arr) == 0:
                print('You can only use characters found in the tiles above')
                continue
            elif player_input.lower() not in english_words:
                print('Word not found in dictionary')
                continue
            else:
                break
        return input_arr

    def main_loop(self):
        while self.running:
            self.print_UI()
            input_list = self.get_input()
            if self.running == False:
                break

            for c in input_list:
                index = self.tiles.index(c)
                self.tiles[index] = self.rand_tile()

            self.curr_enemy.health -= self.player.attack(input_list)
            if self.curr_enemy.health <= 0:
                self.next_enemy()
                self.player.health = self.player.max_health
                continue
            self.curr_enemy.attack()


Game().main_loop()
