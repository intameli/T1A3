import string

tiles = []
vowels = ['A', 'E', 'I', 'O', 'U']
for c in string.ascii_uppercase:
    tiles.append(c + 'u') if c == 'Q' else tiles.append(c)
    if c in vowels:
        tiles.append(c)


class Game:
    def __init__(self):
        self.running = True

    def get_input(self):
        text =  input("text: ")
        if text == '/quit':
            self.running = False
        
    def main_loop(self):
        while self.running:
            print(tiles)
            self.get_input()

game = Game()
game.main_loop()
