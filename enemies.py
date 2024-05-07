atk = {'type': 'basic', 'dmg': 1}

enemies = [
    {
        'name': 'Spearman',
        'health': 4,
        'attacks': [atk]
    },
    {
        'name': 'Warrior',
        'health': 8,
        'attacks': [atk]
    },
    {
        'name': 'Hound',
        'health': 12,
        'attacks': [atk]
    },
    {
        'name': 'Captain',
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
        'attacks': [{'type': 'burn', 'dmg': 1, 'turns': 2}, atk, atk]
    }
]