import csv
import re

def is_us_city(city):
    # Check if the city has a valid US state code
    us_state_codes = set([
        'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
        'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
        'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
        'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
        'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'
    ])
    return city.upper() in us_state_codes

def count_us_cities(csv_file):
    unique_us_cities = set()  # Set to store unique US city names

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            city = row.get('city')  # Assuming 'city' is the column name for cities
            state = row.get('state')  # Assuming 'state' is the column name for state codes
            if city and state and is_us_city(state):
                unique_us_cities.add(city.lower())  # Convert to lowercase for case-insensitive comparison

    return len(unique_us_cities)

if __name__ == "__main__":
    csv_file_path = 'output-allcities.csv'  # Replace with the actual path to your CSV file
    unique_us_city_count = count_us_cities(csv_file_path)
    print(f'Total unique US cities: {unique_us_city_count}')
