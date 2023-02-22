import math

def create_suffix(num):
    if 11 <= num <= 13 or not 1 <= num % 10 <= 3:
        return 'th'
    else:
        return {1: 'st', 2: 'nd', 3: 'rd'}[num % 10]

def get_century(year):
    isTurnOfCentury = str(year).endswith('00')
    
    if isTurnOfCentury:
        year -= 1

    century = math.floor(year / 100) + 1
    
    return str(century) + create_suffix(century)
