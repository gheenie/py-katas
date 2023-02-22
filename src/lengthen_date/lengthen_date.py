from datetime import datetime

def lengthen_date(date):
    parsed_date = datetime.strptime(date, '%d.%m.%Y')

    lengthened = parsed_date.strftime('%A %d{suffix} %B %Y')

    def create_suffix(day):
        if 3 < day < 21 or 23 < day < 31:
            return 'th'
        else:
            return {1: 'st', 2: 'nd', 3: 'rd'}[day % 10]
    
    return lengthened.format( suffix=create_suffix(parsed_date.day) )
