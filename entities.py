class Player:
    def __init__(self):
        self.health = 12
        self.max_health = 12

class Enemy:
    def __init__(self, name, health, attacks, player):
        self.name = name
        self.health = health
        self.attacks = attacks
        self.attack_i = 0
        self.player = player
        self.ailments = []

    def atack(self):
        for effect in self.ailments:
            verb = effect['name']
            effect['turns'] -= 1
            print(f'You take {verb} damage')
            self.player.health -= 1
            if effect['turns'] == 0:
                self.ailments.remove(effect)
                
        curr_atk = self.attacks[self.attack_i]
        fn_str = list(curr_atk.keys())[0]
        value = list(curr_atk.values())[0]
        getattr(self, fn_str)(value)
        self.attack_i += 1
        if self.attack_i == len(self.attacks):
            self.attack_i = 0

    def basic(self, dmg):
        print(f'{self.name} attacks you for {dmg} damage')
        self.player.health -= dmg

    def burn(self, dmg):
        print(f'{self.name} burns you for {dmg} damage')
        self.player.health -= dmg
        self.ailments.append({'name':'burn','dmg':1, 'turns': 2})