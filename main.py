import string
from random import randint
from math import floor

scores = {
    1.25: ['B', 'C', 'F', 'H', 'M', 'P'],
    1.5: ['V','W','Y'],
    1.75: ['J','k'],
    2: ['X','Z'],
    2.75: ['Qu']
}

weights = {}
for c in string.ascii_uppercase:
    char = c
    if c == 'Q':
        char = 'Qu'
    weights[char] = 1
    for key in scores:
        if char in scores[key]:
            weights[char] = key

damage_original = {
  0: 0,
  1: 0,
  2: 0.25,
  3: 0.5,
  4:0.75,
  5:1,
  6:1.5,
  7: 2,
  8:2.75,
  9:3.5,
  10:4.5,
  11: 5.5,
  12: 6.75,
  13: 8,
  14: 9.5,
  15: 11,
  16:13
}
damage = {k: int(v*4) for k, v in damage_original.items()}

tile_options = []
vowels = ['A', 'E', 'I', 'O', 'U']
for c in string.ascii_uppercase:
    tile_options.append(c + 'u') if c == 'Q' else tile_options.append(c)
    if c in vowels:
        tile_options.append(c)

def load_words():
    with open('wordlist.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

if __name__ == '__main__':
    english_words = load_words()

class Game:
    def rand_tile(self):
            i = randint(0, len(tile_options) - 1)
            return tile_options[i]
    
    def print_UI(self, tiles):
        for j in range(4):
                row = ''
                for i in range(4):
                    tile = tiles[(j * 4) + i]
                    row += tile + '  ' if len(tile) == 1 else tile + ' '
                print(row)

    def valid_tiles(self, tiles, player_input):
        tiles_copy = tiles.copy()
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
        
    def main_loop(self):
        tiles = [self.rand_tile() for i in range(16)]
        while True:
            self.print_UI(tiles)
            player_input =  input("text: ").upper()
            input_arr = self.valid_tiles(tiles, player_input)
            if player_input == '/QUIT':
                break
            elif player_input == '/SCRAMBLE':
                tiles = [self.rand_tile() for i in range(16)]
            elif len(input_arr) == 0:
                print('You can only use characters found in the tiles above')
                continue
            elif player_input.lower() not in english_words:
                print('Word not found in dictionary')
                continue
            
            score = 0
            for c in input_arr:
                score += weights[c]
                index = tiles.index(c)
                tiles[index] = self.rand_tile()
            dmg = damage[floor(score)]
            print(str(dmg))
            



game = Game()
game.main_loop()
