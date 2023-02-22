from datetime import datetime

def create_suffix(num):
    if 11 <= num <= 13 or not 1 <= num % 10 <= 3:
        return 'th'
    else:
        return {1: 'st', 2: 'nd', 3: 'rd'}[num % 10]

def lengthen_date(date):
    parsed_date = datetime.strptime(date, '%d.%m.%Y')

    lengthened = parsed_date.strftime('%A %d{suffix} %B %Y')
    
    return lengthened.format( suffix=create_suffix(parsed_date.day) )
