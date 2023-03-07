import re


def caesar_cipher(string, number):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    ciphered_string = ''
    # In python, % is modulo not remainder.
    # So it will still work nicely for positive number.
    shift_by = number % -26
    
    for char in string:
        if re.match(r'[A-Za-z]', char) == None:
            ciphered_string += char
        else:
            alphabet_index = alphabets.index(char)
            ciphered_string += alphabets[alphabet_index + shift_by]
    
    return ciphered_string
