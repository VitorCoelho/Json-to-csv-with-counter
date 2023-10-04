import pandas as pd
import json

def is_usa_city(city_data):
    # Check if the city belongs to the USA
    return city_data.get("country") == "USA"

def json_to_csv(input_json_file, output_csv_file):
    # Initialize an empty list to store USA city JSON objects
    usa_cities_data = []

    # Read the JSON file line by line and filter for USA cities
    with open(input_json_file, 'r') as f:
        for line in f:
            try:
                city_data = json.loads(line)
                if is_usa_city(city_data):
                    usa_cities_data.append(city_data)
            except json.JSONDecodeError as e:
                print(f"Skipping invalid JSON: {line}")

    # Convert USA city JSON list to DataFrame
    df = pd.json_normalize(usa_cities_data)

    # Save DataFrame to CSV
    df.to_csv(output_csv_file, index=False)

if __name__ == "__main__":
    input_json_file = "1.json"  # Replace with your JSON file path
    output_csv_file = "output_usa_cities.csv"  # Replace with your desired CSV file path for USA cities

    json_to_csv(input_json_file, output_csv_file)
