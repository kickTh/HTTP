import requests
from fake_useragent import UserAgent
import asyncio
import aiohttp

user_agent = UserAgent()


async def HTTP_GET(v):
    headers = {
        'User-Agent': user_agent.random
    }

    url = v

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                response.raise_for_status()

    except aiohttp.ClientError as err:
        print(f'An error occurred: {err}')


async def main():
    while True:
        try:
            await asyncio.wait_for(HTTP_GET("https:/google.com/"), timeout=10)
        except asyncio.TimeoutError:
            print('Request timed out')
        except asyncio.CancelledError:
            print('Request cancelled')
        except Exception as e:
            print(f'An error occurred: {e}')


if __name__ == '__main__':
    asyncio.run(main())
