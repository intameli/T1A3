"""
List of chapters in game
List of levels attainable in game
"""
from ch1_enemies import ch1_enemies
from ch2_enemies import ch2_enemies

chapters = [
    {
        'location': 'Ancient Greece',
        'enemies': ch1_enemies,
        'treasure': 'bow_of_zyx'
    },
    {
        'location': 'Island of the Cyclopes',
        'enemies': ch2_enemies,
        'treasure': 'golden_fleece'
    }
]

short_chapt = [{**ch, 'enemies': ch['enemies'][-1:]}
               for i, ch in enumerate(chapters)]

lvls = [
    {
        'xp': 100,
        'effect': 'health'
    },
    {
        'xp': 250,
        'effect': 'dmg'
    }
]

short_lvls = [{**lvl, 'xp': i * 15} for i, lvl in enumerate(lvls)]
