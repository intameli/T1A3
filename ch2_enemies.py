"""
List of enemies in chapter 2
"""
atk = {'type': 'basic', 'dmg': 1}

ch2_enemies = [
    {
        'name': 'Angry Mountain Goat',
        'health': 12,
        'attacks': [atk]
    },
    {
        'name': 'Angry Ewe',
        'health': 8,
        'attacks': [{'type': 'basic', 'dmg': 3}]
    },
    {
        'name': 'Cyclops Herder',
        'health': 16,
        'attacks': [atk]
    },
    {
        'name': 'Angry Ram',
        'health': 12,
        'attacks': [atk]
    },
    {
        'name': 'Cyclops Warrior',
        'health': 20,
        'attacks': [atk]
    },
    {
        'name': 'Polyphemus',
        'health': 28,
        'attacks': [{'type': 'tile_smash', 'turns': 1}, atk]
    }
]
