"""
List of enemies in chapter 1
"""
atk = {'type': 'basic', 'dmg': 1}

ch1_enemies = [
    {
        'name': 'Trojan Spearman',
        'health': 4,
        'attacks': [atk]
    },
    {
        'name': 'Trojan Warrior',
        'health': 8,
        'attacks': [atk]
    },
    {
        'name': 'War Hound',
        'health': 12,
        'attacks': [atk]
    },
    {
        'name': 'Trojan Captain',
        'health': 12,
        'attacks': [atk]
    },
    {
        'name': 'Alexander',
        'health': 8,
        'attacks': [{'type': 'basic', 'dmg': 2}]
    },
    {
        'name': 'Polydamas',
        'health': 12,
        'attacks': [{'type': 'fire', 'dmg': 1, 'turns': 2}, atk, atk]
    }
]
