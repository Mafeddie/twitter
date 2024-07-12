import asyncio

from twikit import Client

###########################################

# Enter your account information
USERNAME = "TechTribalist"
EMAIL = "techtribalist@gmail.com"
PASSWORD = 'Tech1Eddie!'

client = Client('en-US')

async def main():
    # Asynchronous client methods are coroutines and
    # must be called using `await`.
    # await client.login(
    #     auth_info_1=USERNAME,
    #     auth_info_2=EMAIL,
    #     password=PASSWORD
    # )

    ###########################################
    # client.save_cookies('cookies.json')
    
    client.load_cookies('cookies.json')
    
    #     # Create tweet with media
    # TWEET_TEXT = 'The #ICTBill creates a recognized body for ICT professionals in Kenya! This ensures better standards & protects your interests. Learn more & get involved: https://forms.office.com/r/3fcfBLx50T #TechKe #Innovation'
    # MEDIA_IDS = [
    #     await client.upload_media('./image.png', wait_for_completion=True),
    #   ]
    # await client.create_tweet(TWEET_TEXT, MEDIA_IDS)
    
    
        # Fetch user info
    user = await client.get_user_by_screen_name(screen_name='BiancaNaom1')

        # Get user tweets
    user_tweets = await user.get_tweets('Tweets')
    for tweet in user_tweets:
           # Access tweet attributes
        print(
            f'id: {tweet.id}',
            f'text {tweet.text}',
            f'favorite count: {tweet.favorite_count}',
            f'media: {tweet.media}',
            sep='\n'
        )
        
    # # Get more tweets
    # more_user_tweets = await user_tweets.next()

asyncio.run(main())