from chapters_and_lvls import chapters, lvls
from string import ascii_uppercase
from random import randint
from entities import Player, Enemy


class Game:
    def __init__(self):
        self.running = True
        self.words = self.load_words()
        self.tile_options = self.get_tile_options()
        self.tiles = [self.rand_tile() for i in range(16)]
        self.player = Player()
        self.chapters_i = 0
        self.enemy_i = 5
        self.set_chapter()

    def set_chapter(self):
        self.curr_chapter = chapters[self.chapters_i]
        self.enemy_arr = [Enemy(**e, player=self.player, game=self)
                          for e in self.curr_chapter['enemies']]
        self.curr_enemy = self.enemy_arr[self.enemy_i]

    def load_words(self):
        with open('wordlist.txt') as word_file:
            valid_words = set(word_file.read().split())
        return valid_words

    def get_tile_options(self):
        options = []
        vowels = ['A', 'E', 'I', 'O', 'U']
        for c in ascii_uppercase:
            char = c
            if c == 'Q':
                char = 'Qu'
            options.append(char)
            if char in vowels:
                options.append(char)
        return options

    def add_xp(self):
        multiply = 10
        if len(self.enemy_arr) == self.enemy_i + 1:
            multiply = 15
        xp = multiply * (self.chapters_i + 1)
        self.player.xp += xp
        print(f'You received {xp} xp.')

    def lvl_up(self):
        try:
            if self.player.xp >= lvls[self.player.lvl - 1]['xp']:
                self.player.lvl += 1
                print(
                    f'You have leveled up. You are now lvl {self.player.lvl}.')
                match lvls[self.player.lvl - 2]['effect']:
                    case 'health':
                        self.player.health += 4
                        print('Your health has increased.')
                    case 'dmg':
                        self.player.dmg_multi += 0.25
                        print('You now do more damage.')
        except IndexError:
            pass

    def next_enemy(self):
        print(f'You defeated {self.curr_enemy.name}.')
        self.add_xp()
        self.lvl_up()
        if self.enemy_i == len(self.enemy_arr) - 1:
            if self.chapters_i == len(chapters) - 1:
                print('You beat the game, congratulations!')
                self.running = False
                return
            getattr(self.player, self.curr_chapter['treasure'])()
            self.chapters_i += 1
            self.enemy_i = 0
            self.set_chapter()
        else:
            self.enemy_i += 1
            self.curr_enemy = self.enemy_arr[self.enemy_i]
        self.player.health = self.player.max_health
        self.player.weights = self.player.master_weights
        print(f'{self.curr_enemy.name} appears before you.')

    def rand_tile(self):
        i = randint(0, len(self.tile_options) - 1)
        return self.tile_options[i]

    def print_UI(self):
        print(f'\nLocation: {self.curr_chapter["location"]}  '
              f'Enemy: {self.curr_enemy.name}\n'
              f'Level: {self.player.lvl}  XP: {self.player.xp}\n'
              f'Lex Health: {self.player.health}  '
              f'Enemy Health: {self.curr_enemy.health}'
              )
        ail_str = ''
        for effect in self.curr_enemy.ailments:
            ail_str += f'Effect: {effect["type"]} Turns: {effect["turns"]}  '
        if ail_str:
            print(ail_str)
        print(' ' * 15, 'Treasures:') if self.player.treasures else print('')
        for j in range(4):
            row = ''
            for i in range(4):
                tile = self.tiles[(j * 4) + i]
                row += tile + '  ' if len(tile) == 1 else tile + ' '
            if len(self.player.treasures) > j:
                row += f'    {self.player.treasures[j]}'
            print(row)

    def valid_tiles(self, player_input):
        tiles_copy = self.tiles.copy()
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
            player_input = input("Make a word! :  ").upper()
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
            elif player_input.lower() not in self.words:
                print('Word not found in dictionary')
                continue
            else:
                break
        return input_arr

    def player_death(self):
        print(
            "Oh no you died.\nDon't worry, you're only back to the start of the chapter.")
        self.enemy_i = 0
        self.curr_enemy = self.enemy_arr[self.enemy_i]
        self.player.health = self.player.max_health
        self.player.weights = self.player.master_weights

    def main_loop(self):
        print('*' * 20)
        while self.running:
            self.print_UI()
            input_list = self.get_input()
            if self.running == False:
                break
            print('*' * 20)
            print('')

            for c in input_list:
                index = self.tiles.index(c)
                self.tiles[index] = self.rand_tile()

            self.curr_enemy.health -= self.player.attack(input_list)
            if self.curr_enemy.health <= 0:
                self.next_enemy()
                continue
            self.curr_enemy.attack()
            if self.player.health <= 0:
                self.player_death()


Game().main_loop()
