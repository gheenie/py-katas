from datetime import datetime

def mask():
    pass


# @mask('customer_name', 'address_line_1', 'address_line_2', 'post_code', 'telephone')
def get_product_history(product_code):
    return {
        'product_code': product_code,
        'number_in_stock': 14,
        'most_recent_purchases': [
            {
                'customer_id': 1234,
                'number_purchased': 3,
                'customer_name': 'Robert De Niro',
                'address_line_1': '54 Acacia Avenue',
                'address_line_2': 'Didsbury',
                'city': 'Manchester',
                'post_code': 'M45 3PQ',
                'telephone': '0161 323 3434' 
            },
            {
                'customer_id': 4321,
                'number_purchased': 1,
                'customer_name': 'Meryl Streep',
                'address_line_1': '32 Mimosa Road',
                'address_line_2': 'Knowsley',
                'city': 'Liverpool',
                'post_code': 'L13 9XQ',
                'telephone': '0151 232 4343' 
            },
            {
                'customer_id': 5555,
                'number_purchased': 9,
                'customer_name': 'Boris Johnson',
                'address_line_1': '98 Gasworks Street',
                'address_line_2': 'Wallsend',
                'city': 'Newcastle',
                'post_code': 'NE5 6LL',
                'telephone': '0191 111 1111' 
            }
        ]
    }


# @mask('full_name', 'address_1', 'postal_code', 'mobile', 'primary_email')
def get_customer_profile(customer_number):
    return {
        'customer_number': customer_number,
        'customer_purchase_points': 73,
        'customer_joined': datetime(2019, 7, 23),
        'number_of_purchases': 43,
        'customer_details': {
            'customer_identifiers': {
                'full_name': 'Roger Hammerstein',
                'title': 'Lord',
                'gender': 'male'
            },
            'customer_locations': [
                {
                    'location_type': 'primary_residence',
                    'address_1': '19 Smithington Drive',
                    'address_2': 'Cleethorpes',
                    'address_3': 'Lincolnshire',
                    'postal_code': 'DN35 1UV',
                },
                {
                    'location_type': 'secondary_residence',
                    'address_1': '191 Billingsgate Road',
                    'address_2': 'Hackney',
                    'address_3': 'London',
                    'postal_code': 'E5 9ST',
                }
            ],
            'telephone_numbers': {
                'mobile': '07777 777777'
            },
            'email': {
                'primary_email': 'big_roj@hammerste.in'
            }
        }   
    }