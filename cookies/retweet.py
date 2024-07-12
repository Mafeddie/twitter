import asyncio
import json
from twikit import Client
import time


client = Client('en-US')
file_path = r"C:\Users\kihir\Code\twitter\cookies\cookies.json"
# Function to read the JSON file and process each object
async def read_json_file_and_process(file_path):
    """
    Reads a JSON file containing an array of objects and processes each object
    with the provided process_function.

    Args:
        file_path (str): The path to the JSON file.
        process_function (callable): The function to process each JSON object.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    for obj in data:
        print(obj)
        client.set_cookies(obj)
        response = await client.retweet(1811658128041050465)
        print(response)
        time.sleep(110)

asyncio.run(read_json_file_and_process(file_path))