import math
from src.lengthen_date.lengthen_date import create_suffix

def get_century(year):
    isTurnOfCentury = str(year).endswith('00')
    
    if isTurnOfCentury:
        year -= 1

    century = math.floor(year / 100) + 1
    
    return str(century) + create_suffix(century)
