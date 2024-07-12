import asyncio
import csv
import os
from twikit import Client

# Define the path for the CSV file and the JSON file
CSV_FILE_PATH = 'credentials.csv'
COOKIES_FILE_PATH = 'cookies.json'

# Function to prompt the user for the CSV file path
def get_csv_file_path():
    # You can use an input prompt to allow the user to specify the CSV file path
    csv_file_path = input("Enter the path to the CSV file with username, email, and password values: ")
    if not os.path.isfile(csv_file_path):
        raise FileNotFoundError(f"The file '{csv_file_path}' does not exist.")
    return csv_file_path

# Function to read CSV file and return a list of (username, email, password) tuples
def read_csv_file(file_path):
    credentials = []
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 3:
                username, email, password = row
                credentials.append((username, email, password))
            else:
                print(f"Skipping invalid row: {row}")
    return credentials

# Define the main async function
async def main():
    # Prompt for CSV file path
    csv_file_path = get_csv_file_path()
    # Read credentials from CSV
    credentials_list = read_csv_file(csv_file_path)
    
    # Create an instance of the Client
    client = Client('en-US')

    # Loop through the list of credentials
    for username, email, password in credentials_list:
        try:
            # Login using the current set of credentials
            await client.login(
                auth_info_1=username,
                auth_info_2=email,
                password=password
            )
            # Save the cookies to a JSON file
            client.save_cookies(COOKIES_FILE_PATH)
            print(f"Cookies saved for {username} to {COOKIES_FILE_PATH}")

        except Exception as e:
            print(f"Failed to log in with {username}. Error: {e}")

# Run the main async function
asyncio.run(main())
