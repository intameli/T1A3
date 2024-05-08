weights = {
    # remember to chage back to 1, this is just for testing
    'A': 10,
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

"""
Below is the code used to generate the weights dictionary
"""
# scores = {
#     1.25: ['B', 'C', 'F', 'H', 'M', 'P'],
#     1.5: ['V', 'W', 'Y'],
#     1.75: ['J', 'k'],
#     2: ['X', 'Z'],
#     2.75: ['Qu']
# }
# weights = {}
# for c in ascii_uppercase:
#     char = c
#     if c == 'Q':
#         char = 'Qu'
#     weights[char] = 1
#     for key in scores:
#         if char in scores[key]:
#             weights[char] = key

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
damage = {k: int(v*4) for k, v in damage_original.items()}
