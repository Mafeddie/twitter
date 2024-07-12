import asyncio
from twikit import Client
# import re

async def main():
    client = Client(language='en-US')
    username = 'TechTribalist'

    # Login
    await client.login(auth_info_1=username, auth_info_2='techtribalist@gmail.com', password='Tech1Eddie!')

    # Fetch user info
    user = await client.get_user_by_screen_name(screen_name=username)

    # Access user attributes
    print(
        f'id: {user.id}',
        f'name: {user.name}',
        f'followers: {user.followers_count}',
        f'tweets count: {user.statuses_count}',
        sep='\n'
    )
    
 
    tweets = await client.get_user_tweets(user.id, 'Tweets', count=20)
    for tweet in tweets:
        tweet = await client.get_tweet_by_id(tweet.id)

        # Access tweet attributes
        print(
            f'id: {tweet.id}',
            f'text {tweet.text}',
            f'favorite count: {tweet.favorite_count}',
            f'media: {tweet.media}',
            sep='\n'
        )
         
         
    # Create a tweet with media
    #await create_tweet(client, "Hello, world!", media_paths=['image1.jpg', 'image2.jpg'])

    # Search for tweets
    # await search_tweets(client, 'python')

    # Retrieve user tweets
    #await get_user_tweets(client, user.id_str)

asyncio.run(main())
