from itertools import groupby

def herd_the_babies(string):
    letters = list(string)

    letters.sort(key=lambda char: (char.upper(), char))

    return ''.join(letters)
