import asyncio

from twikit import Client

client = Client('en-US')

async def main():
    client.load_cookies('cookies.json')
       
        # Get news trends
    trends = await client.get_trends('news')
    for trend in trends:
            print(trend)  
        
       
asyncio.run(main())