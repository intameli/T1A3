"""
The main file for this program.
Contains the Game class which has the main_loop method
"""
from random import randint
from util import WORDS, TILE_OPTIONS, valid_tiles
from data.chapters_and_lvls import chapters, lvls, short_chapt, short_lvls
from entities import Player, Enemy


class Game:
    """Class that controls the game
    """

    def __init__(self, long):
        self.running = True
        self.lvls = lvls if long else short_lvls
        self.chapters = chapters if long else short_chapt
        self.tiles = [self.rand_tile() for i in range(16)]
        self.player = Player()
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
        print(f'You defeated {self.curr_enemy.name}')
        self.add_xp()
        self.lvl_up()
        print('You continue along the path.')
        if self.enemy_i == len(self.enemy_list) - 1:
            print('You find a chest and open it.')
            getattr(self.player, self.curr_chapter['treasure'])()
            if self.chapters_i == len(self.chapters) - 1:
                print('You beat the game, congratulations.')
                self.running = False
                return
            print(f"You come to the end of {self.curr_chapter['location']}")
            self.chapters_i += 1
            self.enemy_i = 0
            self.set_chapter()
            print(
                f"You See a sign inicating you are entering {self.curr_chapter['location']}")
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
        i = randint(0, len(TILE_OPTIONS) - 1)
        return TILE_OPTIONS[i]

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

    def get_input(self):
        """Get user input and react to it

        Loops until the player input is valid

        Returns:
            list: The valid tiles the user inputed
        """
        while True:
            player_input = input("Make a word! :  ").upper()
            input_list = valid_tiles(player_input, self.tiles)
            if player_input == '/QUIT':
                self.running = False
                break
            elif player_input == '/SCRAMBLE':
                self.tiles = [self.rand_tile() for i in range(16)]
                break
            elif len(input_list) == 0:
                print('You can only use characters found in the tiles above')
                continue
            elif player_input.lower() not in WORDS:
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
        print('\nYou are a worm named Lex. One day you were chilling\n'
              'in the library when you were magically sucked into a book.\n'
              'You seem to be in some kind of liminal space that resembles\n'
              f'Ancient Greece. As you walk foward {self.curr_enemy.name}\n'
              "appears before you. Oh No. It's battle time.\n\n"
              '/quit to exit game.\n'
              '/scramble to skip your attack and get all new tiles.\n'
              'Minimum word length is 3 tiles')

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
    PROMPT = ("\nType 'long' to play the full game with 13 enemies,\n"
              "any other response will play the short version:  ")
    LONG = True if input(PROMPT).lower() == 'long' else False
    Game(LONG).main_loop()
