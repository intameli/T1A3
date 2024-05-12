"""
Weights dictionary for calculating player damage
dmg dictionary also for finding player damage
Both are created from info on the Bookwork Adventures Wiki
"""
weights = {
    'A': 1,
    'B': 1.25,
    'C': 1.25,
    'D': 1,
    'E': 1,
    'F': 1.25,
    'G': 1,
    'H': 1.25,
    'I': 1,
    'J': 1.75,
    'K': 1,
    'L': 1,
    'M': 1.25,
    'N': 1,
    'O': 1,
    'P': 1.25,
    'Qu': 2.75,
    'R': 1,
    'S': 1,
    'T': 1,
    'U': 1,
    'V': 1.5,
    'W': 1.5,
    'X': 2,
    'Y': 1.5,
    'Z': 2
}

damage_original = {
    0: 0,
    1: 0,
    2: 0.25,
    3: 0.5,
    4: 0.75,
    5: 1,
    6: 1.5,
    7: 2,
    8: 2.75,
    9: 3.5,
    10: 4.5,
    11: 5.5,
    12: 6.75,
    13: 8,
    14: 9.5,
    15: 11,
    16: 13,
    17: 13,
    18: 13,
    19: 13,
    20: 13,
    21: 13,
    22: 13
}
# All damages are multiplied by 4 because the original game uses hearts to
# represent health (min damage is 1/4 of heart) and I
# want health to be a whole number
# Health and enemy attack are also using values from the wiki multiplied by 4
damage = {k: int(v*4) for k, v in damage_original.items()}
