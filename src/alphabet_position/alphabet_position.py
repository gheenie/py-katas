def alphabet_position(string):
  # An alphabet's position is the index in the lookup + 1
  alphabet_position_lookup = 'abcdefghijklmnopqrstuvwxyz'

  # The lookup table only accepts lowercase letters
  string = string.lower()

  # This string will be gradually built with the alphabets' positions
  positions = ''

  # Build the positions string
  for letter in string:
    if letter.isalpha():
      # An alphabet's position is the index in the lookup + 1.
      # Add a whitespace between each position
      positions += str(alphabet_position_lookup.index(letter) + 1) + ' '
    else:
      # Ignore non-alphabets
      positions += ''

  # Remove trailing whitespace
  positions = positions[0:-1]

  return positions
