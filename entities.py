class Player:
    def __init__(self):
        self.health = 12
        self.max_health = 12

class Spearman:
    def __init__(self):
        self.health = 4

    def attack(self, obj):
        obj.health -= 1