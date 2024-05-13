"""
List of chapters in game
List of levels attainable in game
"""
from data.ch1_enemies import ch1_enemies
from data.ch2_enemies import ch2_enemies
from data.ch3_enemies import ch3_enemies

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
    },
    {
        'location': 'The Wandering Rocks',
        'enemies': ch3_enemies,
        'treasure': 'friendship'
    }
]

short_chapt = [{**ch, 'enemies': ch['enemies'][-1:]}
               for i, ch in enumerate(chapters)]

lvls = [
    {
        'xp': 50,
        'effect': 'health'
    },
    {
        'xp': 150,
        'effect': 'dmg'
    }
]

short_lvls = [{**lvl, 'xp': i * 15} for i, lvl in enumerate(lvls)]
