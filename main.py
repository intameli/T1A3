"""
The main file for this program.
Contains the Game class which has the main_loop method
"""
from string import ascii_uppercase
from random import randint
from chapters_and_lvls import chapters, lvls, short_chapt, short_lvls
from entities import Player, Enemy


class Game:
    """Class that controls the game
    """

    def __init__(self):
        self.running = True
        self.words = self.load_words()
        self.tile_options = self.get_tile_options()
        self.tiles = [self.rand_tile() for i in range(16)]
        self.player = Player()
        self.long = self.get_game_length()
        self.lvls = lvls if self.long else short_lvls
        self.chapters = chapters if self.long else short_chapt
        self.chapters_i = 0
        self.enemy_i = 0
        self.set_chapter()

    def set_chapter(self):
        """sets curr_chapter, enemy_list, curr_enemy

        Enemy classes are created for each enemy in the chapter
        """
        self.curr_chapter = self.chapters[self.chapters_i]
        self.enemy_list = [Enemy(**e, player=self.player, game=self)
                           for e in self.curr_chapter['enemies']]
        self.curr_enemy = self.enemy_list[self.enemy_i]

    def get_game_length(self):
        """Get whether the player wants to play the full game

        Returns:
            boolean: Whether or not you want a long game
        """
        prompt = ("Type 'long' to play the full game with 12 enemies,\n"
                  "any other response will play the short version:  ")
        return True if input(prompt).lower == 'long' else False

    def load_words(self):
        """Reads valid words from file

        Returns:
            set: Every word in the bookworm dictionary
        """
        with open('wordlist.txt', encoding="utf-8") as word_file:
            valid_words = set(word_file.read().split())
        return valid_words

    def get_tile_options(self):
        """Creates a list of possible tiles

        Vowels are added twice

        Returns:
            list: Tile options
        """
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
        """Calculate XP and update it
        """
        multiply = 10
        if len(self.enemy_list) == self.enemy_i + 1:
            multiply = 15
        xp = multiply * (self.chapters_i + 1)
        self.player.xp += xp
        print(f'You received {xp} xp.')

    def lvl_up(self):
        """Levels up the player if nessessary
        """
        try:
            if self.player.xp >= self.lvls[self.player.lvl - 1]['xp']:
                self.player.lvl += 1
                print(
                    f'You have leveled up. You are now lvl {self.player.lvl}.')
                match self.lvls[self.player.lvl - 2]['effect']:
                    case 'health':
                        self.player.max_health += 4
                        print('Your health has increased.')
                    case 'dmg':
                        self.player.dmg_multi += 0.25
                        print('You now do more damage.')
        except IndexError:
            pass

    def next_enemy(self):
        """Set the next enemy/chapter

        Function also:
        - adds xp and levels up
        - resets player health and weights(because of the tile_smash attack)
        - checks for end of the game
        - runs treasure function if you beat a boss
        """
        print(f'You defeated {self.curr_enemy.name}.')
        self.add_xp()
        self.lvl_up()
        if self.enemy_i == len(self.enemy_list) - 1:
            if self.chapters_i == len(self.chapters) - 1:
                print('You beat the game, congratulations!')
                self.running = False
                return
            getattr(self.player, self.curr_chapter['treasure'])()
            self.chapters_i += 1
            self.enemy_i = 0
            self.set_chapter()
        else:
            self.enemy_i += 1
            self.curr_enemy = self.enemy_list[self.enemy_i]
        self.player.health = self.player.max_health
        self.player.weights = self.player.master_weights
        print(f'{self.curr_enemy.name} appears before you.')

    def rand_tile(self):
        """Gets a random tile

        Returns:
            string: The letter/s
        """
        i = randint(0, len(self.tile_options) - 1)
        return self.tile_options[i]

    def print_ui(self):
        """Prints the UI
        """
        print(f'\nLocation: {self.curr_chapter["location"]}  '
              f'Enemy: {self.curr_enemy.name}\n'
              f'Level: {self.player.lvl}  XP: {self.player.xp}\n'
              f'Lex Health: {self.player.health}  '
              f'Enemy Health: {self.curr_enemy.health}'
              )
        ail_str = ''
        for effect in self.curr_enemy.ailments:
            ail_str += f'[Effect: {effect["type"]}, Turns: {effect["turns"]}]  '
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
        """Checks if input is valid

        Args:
            player_input (string): Input from the player

        Returns:
            list: The valid tiles the user inputed
        """
        tiles_copy = self.tiles.copy()
        input_list = []
        for i, c in enumerate(player_input):
            char = c
            if c == 'Q' and player_input[i + 1] == 'U':
                char = 'Qu'
            if c == 'U' and player_input[i - 1] == 'Q':
                continue
            if char in tiles_copy:
                tiles_copy.remove(char)
                input_list.append(char)
            else:
                input_list = []
                break
        return input_list

    def get_input(self):
        """Get user input and react to it

        Loops until the player input is valid

        Returns:
            list: The valid tiles the user inputed
        """
        while True:
            player_input = input("Make a word! :  ").upper()
            input_list = self.valid_tiles(player_input)
            if player_input == '/QUIT':
                self.running = False
                break
            elif player_input == '/SCRAMBLE':
                self.tiles = [self.rand_tile() for i in range(16)]
                break
            elif len(input_list) == 0:
                print('You can only use characters found in the tiles above')
                continue
            elif player_input.lower() not in self.words:
                print('Word not found in dictionary')
                continue
            else:
                break
        return input_list

    def player_death(self):
        """Handles the death of the player
        """
        print(
            "Oh no you died.\nDon't worry, you're only back to the start of the chapter.")
        self.enemy_i = 0
        self.curr_enemy = self.enemy_list[self.enemy_i]
        self.player.health = self.player.max_health
        self.player.weights = self.player.master_weights

    def main_loop(self):
        """The main loop that runs the game
        """
        print('*' * 20)
        while self.running:
            self.print_ui()
            input_list = self.get_input()
            if self.running == False:
                break
            print('*' * 20)
            print('')

            # Replace used tiles with random ones
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


if __name__ == '__main__':
    Game().main_loop()
