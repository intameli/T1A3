"""
List of enemies in chapter 3
"""
atk = {'type': 'basic', 'dmg': 1}

ch3_enemies = [
    {
        'name': 'Big Bad',
        'health': 30,
        'attacks': [
            {'type': 'fire', 'dmg': 1, 'turns': 2},
            {'type': 'tile_smash', 'turns': 1},
            atk
        ]
    }
]
