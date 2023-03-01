def sum_ascii(array):
    highest_ascii_sum = 0
    name_with_highest_ascii_sum = ''

    for name in array:
        ascii_sum = 0

        for letter in name: ascii_sum += ord(letter.lower())

        if ascii_sum > highest_ascii_sum:
            highest_ascii_sum = ascii_sum
            name_with_highest_ascii_sum = name

        print(ascii_sum)

    return name_with_highest_ascii_sum
