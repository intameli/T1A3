"""
Enemy classes
"""
from random import randint


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
        char = self.game.tiles[randint(0, 15)]
        weight = self.player.weights[char]
        self.player.weights[char] = 0

        def end():
            self.player.weights[char] = weight
            print(f'{char} tiles are no longer smashed.')
        atk['end'] = end

        self.ailments.append(atk)
        print(f'{self.name} smashes the {char} tiles, '
              f'they now do no damage.')
