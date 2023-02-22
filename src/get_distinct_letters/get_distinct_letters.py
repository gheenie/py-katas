def get_distinct_letters(string1, string2):
	set1 = set(string1)
	set2 = set(string2)

	unique_letters = set1.symmetric_difference(set2)
	
	unique_letters_alphabetical = list(unique_letters)
	unique_letters_alphabetical.sort()
	
	return ''.join(unique_letters_alphabetical)
