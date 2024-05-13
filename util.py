"""
Functions used by main
"""
from string import ascii_uppercase


def load_words():
    """Reads valid words from file

    Returns:
        set: Every word in the bookworm dictionary
    """
    with open('data/wordlist.txt', encoding="utf-8") as word_file:
        valid_words = set(word_file.read().split())
    return valid_words


WORDS = load_words()


def get_tile_options():
    """Creates a list of possible tiles

    Vowels are added twice

    Returns:
        list: Tile options
    """
    options = []
    vowels = ['A', 'E', 'I', 'O', 'U']
    for c in ascii_uppercase:
        char = c
        if c == 'Q':
            char = 'Qu'
        options.append(char)
        if char in vowels:
            options.append(char)
    return options


TILE_OPTIONS = get_tile_options()


def valid_tiles(player_input, tiles):
    """Checks if input is valid

    Args:
        player_input (string): Input from the player

    Returns:
        list: The valid tiles the user inputed
    """
    tiles_copy = tiles.copy()
    input_list = []
    for i, c in enumerate(player_input):
        char = c
        if c == 'Q' and player_input[i + 1] == 'U':
            char = 'Qu'
        if c == 'U' and player_input[i - 1] == 'Q':
            continue
        if char in tiles_copy:
            tiles_copy.remove(char)
            input_list.append(char)
        else:
            input_list = []
            break
    return input_list
