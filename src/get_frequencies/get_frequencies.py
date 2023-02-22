def get_frequencies(string):
	frequency_table = {}

	for char in string:
		if not char.isalpha():
			continue

		frequency_table[char] = frequency_table.get(char, 0) + 1
	
	return frequency_table
