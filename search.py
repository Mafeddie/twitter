import asyncio
import json
from twikit import Client

client = Client('en-US')

async def main():
    client.load_cookies('cookies.json')
       
    tweets = await client.search_tweet(query='#Tubonge',product='Top',count=10)

    for tweet in tweets:

        # Access tweet attributes
        print(
            f'id: {tweet.id}',
            f'text {tweet.text}',
            f'favorite count: {tweet.favorite_count}',
            f'media: {tweet.media}',
            sep='\n'
        )
    
asyncio.run(main())