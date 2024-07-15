import asyncio
import json
from twikit import Client

client = Client('en-US')

async def main():
    client.load_cookies('cookies.json')
    #    RutoMustStay stopSabotagingRuto dealdone
    tweets = await client.search_tweet(query='RutoMustStay',product='Latest',count=50)
    print(len(tweets))
    for tweet in tweets:

        # Access tweet attributes
        print(
            f'id: {tweet.id}',
            f'text {tweet.text}',
            f'favorite count: {tweet.favorite_count}',
            # f'media: {tweet.media}',
            sep='\n'
        )
    
asyncio.run(main())