"""
Player class
"""
from math import floor
from data.weights_and_dmg import weights, damage


class Player:
    """Class that defines the player
    """

    def __init__(self):
        self.health = 12
        self.max_health = 12
        self.xp = 0
        self.lvl = 1
        self.dmg_multi = 1
        self.weights = weights
        self.master_weights = weights
        self.treasures = []

    def attack(self, input_list):
        """Calculates how much dmg your word does

        First calculates total letter scores then 
        uses that to get dmg from a dict

        Args:
            input_list (list): The valid tiles from the player

        Returns:
            integer: The amount of dmg you do
        """
        if len(input_list) == 0:
            return 0
        score = 0
        for c in input_list:
            score += self.weights[c]
        dmg = damage[floor(score)]
        dmg = floor(dmg * self.dmg_multi)
        print(f'Your word attacks for {dmg} damage.')
        return dmg

    def bow_of_zyx(self):
        """Applies the effects of bow_of_zyx
        """
        print('Obtained the Bow of Zyx.\n'
              'The bow increases damage done by X, Y and Z letter tiles.')
        self.master_weights['Z'] = 2.5
        self.master_weights['Y'] = 2.5
        self.master_weights['X'] = 2.5
        self.treasures.append('Bow of Zyx')

    def golden_fleece(self):
        """Applies the effects of golden_fleece
        """
        print('Obtained the Golden Fleece.\n'
              'The fleece increases player health')
        self.max_health += 4
        self.treasures.append('Golden Fleece')

    def friendship(self):
        """Applies friendship
        """
        print('As you open the chest you feel yourself being pulled back into\n'
              'the real world. You find yourself facing the book you were just inside.\n'
              'The book is turned to a page with only one line that reads:\n'
              "'The ultimate treasure was the friends we made along the way'\n"
              'You look around. You are alone.')
