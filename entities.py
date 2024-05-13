"""
Player and Enemy classes
"""
from math import floor
from random import randint
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


class Enemy:
    """Class used by all enemies

    Contains every enemy attack in the game
    """

    def __init__(self, name, health, attacks, player, game):
        self.name = name
        self.health = health
        self.attacks = attacks
        self.attack_i = 0
        self.player = player
        self.game = game
        self.ailments = []

    def apply_ailments(self):
        """Calls the function/s for each ailment and removes if finished
        """
        for effect in self.ailments:
            effect['turns'] -= 1
            if 'apply' in effect:
                effect['apply']()
            if effect['turns'] == 0:
                if 'end' in effect:
                    effect['end']()
                self.ailments.remove(effect)

    def attack(self):
        """Choses which attack to make

        Also applies ailments
        """
        self.apply_ailments()
        curr_atk = self.attacks[self.attack_i]
        fn_str = curr_atk['type']
        getattr(self, fn_str)(curr_atk)
        self.attack_i += 1
        if self.attack_i == len(self.attacks):
            self.attack_i = 0

    def basic(self, atk):
        """A basic attack

        Args:
            atk (dictionary): Info about the attack
        """
        print(f'{self.name} attacks you for {atk["dmg"]} damage.')
        self.player.health -= atk['dmg']

    def fire(self, atk_dict):
        """A fire attack that burns for multiple turns

        Args:
            atk_dict (dictionary): Info about the attack
        """
        atk = atk_dict.copy()
        print(f'{self.name} burns you for {atk["dmg"]} damage.')
        print('You are now on fire.')
        self.player.health -= atk['dmg']

        def apply():
            print(f'You take {atk["dmg"]} fire damage.')
            self.player.health -= atk['dmg']
        atk['apply'] = apply

        def end():
            print('You are no longer on fire.')
        atk['end'] = end

        self.ailments.append(atk)

    def tile_smash(self, atk_dict):
        """An attack that makes a random letter do no dmg

        Args:
            atk_dict (dictionary): Info about the attack
        """
        atk = atk_dict.copy()
        atk['char'] = self.game.tiles[randint(0, 15)]
        atk['weight'] = self.player.weights[atk['char']]
        self.player.weights[atk['char']] = 0

        def end():
            self.player.weights[atk['char']] = atk['weight']
            print(f'{atk["char"]} tiles are not longer smashed.')
        atk['end'] = end

        self.ailments.append(atk)
        print(f'{self.name} smashes the {atk["char"]} tiles, '
              f'they now do no damage.')
