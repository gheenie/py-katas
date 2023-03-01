from itertools import groupby

def herd_the_babies(string):
    letters = list(string)

    # Sorts aA-zZ
    letters.sort(key=str.lower)

    # Will be a list of list. Each innermost list contains both upper and lower of one alphabet.
    alphabet_groups = []

    for k, g in groupby(letters, key=lambda x: x.lower()):
        # g will be a group of one alphabet, eg aaAA
        alphabet_groups.append(sorted(list(g)))

    # Flatten the list, then join into a str
    return ''.join([letter for alphabet_group in alphabet_groups for letter in alphabet_group])
