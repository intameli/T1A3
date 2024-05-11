from weights_and_dmg import weights, damage
from math import floor
from random import randint


class Player:
    def __init__(self):
        self.health = 12
        self.max_health = 12
        self.weights = weights
        self.master_weights = weights

    def attack(self, input_list):
        score = 0
        for c in input_list:
            score += self.weights[c]
        dmg = damage[floor(score)]
        print(f'Your word attacks for {dmg} damage.')
        return dmg

    def bow_of_zyx(self):
        print('Obtained Bow of Zyx.')
        self.master_weights['Z'] = 2.5
        self.master_weights['Y'] = 2.5
        self.master_weights['X'] = 2.5

    def golden_fleece(self):
        pass


class Enemy:
    def __init__(self, name, health, attacks, player, game):
        self.name = name
        self.health = health
        self.attacks = attacks
        self.attack_i = 0
        self.player = player
        self.game = game
        self.ailments = []

    def apply_ailments(self):
        for effect in self.ailments:
            effect['turns'] -= 1
            if 'apply' in effect:
                effect['apply']()
            if effect['turns'] == 0:
                if 'end' in effect:
                    effect['end']()
                self.ailments.remove(effect)

    def attack(self):
        self.apply_ailments()
        # for effect in self.ailments:
        #     effect['turns'] -= 1
        #     if effect['type'] == 'tile_smash':
        #         if effect['turns'] == 0:
        #             self.player.weights[effect['char']] = effect['weight']
        #             self.ailments.remove(effect)
        #         continue

        #     print(f'You take {effect["dmg"]} {effect["type"]} damage.')
        #     self.player.health -= effect['dmg']
        #     if effect['turns'] == 0:
        #         print(effect['end'])
        #         self.ailments.remove(effect)

        curr_atk = self.attacks[self.attack_i]
        fn_str = curr_atk['type']
        getattr(self, fn_str)(curr_atk)
        self.attack_i += 1
        if self.attack_i == len(self.attacks):
            self.attack_i = 0

    def basic(self, atk):
        print(f'{self.name} attacks you for {atk["dmg"]} damage.')
        self.player.health -= atk['dmg']

    def fire(self, atk_dict):
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
        atk = atk_dict.copy()
        atk['char'] = self.game.tiles[randint(0, 15)]
        atk['weight'] = self.player.weights[atk['char']]
        self.player.weights[atk['char']] = 0

        def end():
            self.player.weights[atk['char']] = atk['weight']
        atk['end'] = end

        self.ailments.append(atk)
        print(f'{self.name} smashes the {atk["char"]} tiles, '
              f'they now do no damage.')
