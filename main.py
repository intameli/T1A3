import string
from random import randint

tile_options = []
vowels = ['A', 'E', 'I', 'O', 'U']
for c in string.ascii_uppercase:
    tile_options.append(c + 'u') if c == 'Q' else tile_options.append(c)
    if c in vowels:
        tile_options.append(c)


class Game:
    def __init__(self):
        self.running = True
        self.input = ''

    def get_input(self):
        self.input =  input("text: ").upper()
        if self.input == '/QUIT':
            self.running = False

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
        
    def main_loop(self):
        tiles = [self.rand_tile() for i in range(16)]
        while self.running:
            # if tiles == ['.' for i in range(16)]:
            tiles = [self.rand_tile() for i in range(16)]
            self.print_UI(tiles)
            self.get_input()
            tiles_copy = tiles.copy()
            input_arr = []
            valid = True
            for i, c in enumerate(self.input):
                char = c
                if c == 'Q' and self.input[i + 1] == 'U':
                    char = 'Qu'
                if c == 'U' and self.input[i - 1] == 'Q':
                    continue
                if char in tiles_copy:
                    tiles_copy.remove(char)
                    input_arr.append(char)
                else:
                    valid = False
                    break
            if valid == False:
                continue
            for c in input_arr:
                index = tiles.index(c)
                tiles[index] = '.'
            self.print_UI(tiles)
            print('')
            



game = Game()
game.main_loop()
