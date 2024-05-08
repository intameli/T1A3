from weights_and_dmg import weights, damage
from math import floor


class Player:
    def __init__(self):
        self.health = 12
        self.max_health = 12
        self.weights = weights

    def attack(self, input_list):
        score = 0
        for c in input_list:
            score += self.weights[c]
        dmg = damage[floor(score)]
        print(self.weights['Y'])
        return dmg

    def bow_of_zyx(self):
        print('Obtained Bow of Zyx')
        self.weights['Z'] = 2.5
        self.weights['Y'] = 2.5
        self.weights['X'] = 2.5


class Enemy:
    def __init__(self, name, health, attacks, player):
        self.name = name
        self.health = health
        self.attacks = attacks
        self.attack_i = 0
        self.player = player
        self.ailments = []

    def attack(self):
        for effect in self.ailments:
            effect['turns'] -= 1
            print(f'You take {effect["type"]} damage')
            self.player.health -= 1
            if effect['turns'] == 0:
                self.ailments.remove(effect)

        curr_atk = self.attacks[self.attack_i]
        fn_str = curr_atk['type']
        getattr(self, fn_str)(curr_atk)

        self.attack_i += 1
        if self.attack_i == len(self.attacks):
            self.attack_i = 0

    def basic(self, atk):
        print(f'{self.name} attacks you for {atk["dmg"]} damage')
        self.player.health -= atk['dmg']

    def burn(self, atk):
        print(f'{self.name} burns you for {atk["dmg"]} damage')
        self.player.health -= atk['dmg']
        self.ailments.append(atk)
