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
# 100, 250
lvls = [
    {
        'xp': 10,
        'effect': 'health'
    },
    {
        'xp': 20,
        'effect': 'dmg'
    }
]
