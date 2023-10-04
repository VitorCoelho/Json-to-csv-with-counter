import csv
import re
from collections import Counter

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

def count_businesses_by_city(csv_file):
    city_business_counts = Counter()  # Counter to store counts for each city

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            city = row.get('city')  # Assuming 'city' is the column name for cities
            state = row.get('state')  # Assuming 'state' is the column name for state codes
            if city and state and is_us_city(state):
                # Convert to lowercase for case-insensitive comparison
                city = city.lower()
                # Increment the count for the city
                city_business_counts[city] += 1

    return city_business_counts

if __name__ == "__main__":
    csv_file_path = 'output-allcities.csv'  # Replace with the actual path to your CSV file
    city_business_counts = count_businesses_by_city(csv_file_path)

    # Print the total number of unique US cities
    total_us_cities = len(city_business_counts)
    print(f'Total unique US cities: {total_us_cities}')

    # Sort and print the city counts in descending order
    sorted_city_counts = dict(sorted(city_business_counts.items(), key=lambda item: item[1], reverse=True))
    for city, count in sorted_city_counts.items():
        print(f'City: {city}, Number of Businesses: {count}')
