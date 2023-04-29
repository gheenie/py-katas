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

	# The roman string encoding the number. It will be gradually built
	roman_equivalent = ''

	# Encode the -1 digit
	last_digit = num % 10
	roman_equivalent += last_digit_translation[last_digit]

	# Encode the -2 digit

	# Get the 2nd last digit. % 10 is needed for number >= 100
	tens = int((num / 10) % 10)

	if tens <= 3:
		roman_equivalent = 'X' * tens + roman_equivalent
	# 'L' is needed for 40 <= number <= 89
	elif tens == 4:
		roman_equivalent = 'XL' + roman_equivalent
	elif tens >= 5 and tens <= 8:
		tens -= 5
		roman_equivalent = 'L' + 'X' * tens + roman_equivalent
	# 'C' is needed for number > 90
	elif tens == 9:
		roman_equivalent = 'XC' + roman_equivalent

	# encode -3 digit onwards
	hundreds = int(num / 100)
	roman_equivalent = 'C' * hundreds + roman_equivalent
	
	return roman_equivalent
