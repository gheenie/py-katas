def alphabet_position(string):
  alphabet_position_lookup = 'abcdefghijklmnopqrstuvwxyz'

  # The lookup table only accepts lowercase letters
  string = string.lower()

  positions = str(alphabet_position_lookup.index(string) + 1)

  return positions
