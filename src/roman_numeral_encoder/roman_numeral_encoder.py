def roman_numeral_encoder(num):
	last_digit_translation = {
		0: '',
		1: 'I',
		2: 'II',
		3: 'III',
		4: 'IV',
		5: 'V',
		6: 'VI',
		7: 'VII',
		8: 'VIII',
		9: 'IX',
	}

	# The roman string which will be gradually built
	roman_equivalent = ''

	# Encode the -1 digit
	last_digit = num % 10
	roman_equivalent += last_digit_translation[last_digit]

	# Encode the -2 digit
	tens = num / 10
	roman_equivalent = 'X' * int(tens) + roman_equivalent

	# encode -3 digit onwards 
	
	return roman_equivalent
