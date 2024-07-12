import asyncio
from twikit import Client

# Initialize the client
client = Client(language='en-US')

async def get_user_id(username):
    try:
        user = await client.get_user_by_screen_name(screen_name=username)
        return user.id_str
    except Exception as e:
        print(f"Error fetching user ID: {e}")
        return None

async def main():
    username = input("Enter the Twitter username: ")
    user_id = await get_user_id(username)
    if user_id:
        print(f"The user ID for @{username} is {user_id}")
    else:
        print("Failed to fetch user ID.")

# Run the script
asyncio.run(main())
