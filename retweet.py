import asyncio
import json
from twikit import Client
import time

client = Client('en-US')



async def main():
    client.load_cookies('cookies.json')
   
    
    Tweet_ids = []   
    tweets = await client.search_tweet(query='Tujadiliane',product='Top',count=10)

    # for tweet in tweets:
    #     Tweet_ids.append(tweet.id)
    #     print(len(Tweet_ids))
    #     print(Tweet_ids)
    #     # Access tweet attributes
        # print(
        #     f'id: {tweet.id}',
        #     # f'text {tweet.text}',
        #     # f'favorite count: {tweet.favorite_count}',
        #     # f'media: {tweet.media}',
        #     sep='\n'
        # )
    
    for tweet_Id in Tweet_ids:
        tweet = await client.get_tweet_by_id(tweet_Id)
        
        print(
        f'id: {tweet.id}',
        f'favorite count: {tweet.favorite_count}',
        sep='\n'
        )   
        response = await client.retweet(tweet_Id)
        print(response)
        time.sleep(110)
    
asyncio.run(main())