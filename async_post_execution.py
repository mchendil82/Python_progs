# import asyncio
# # import aiohttp
# # import time

# # websites = """https://www.youtube.com
# # https://www.facebook.com
# # https://www.baidu.com
# # https://www.yahoo.com
# # https://www.amazon.com
# # https://www.wikipedia.org
# # http://www.qq.com
# # https://www.google.co.in
# # https://www.twitter.com
# # https://www.live.com
# # http://www.taobao.com
# # https://www.bing.com
# # https://www.instagram.com
# # http://www.weibo.com
# # http://www.sina.com.cn
# # https://www.linkedin.com
# # http://www.yahoo.co.jp
# # http://www.msn.com
# # http://www.uol.com.br
# # https://www.google.de
# # http://www.yandex.ru
# # http://www.hao123.com
# # https://www.google.co.uk
# # https://www.reddit.com
# # https://www.ebay.com
# # https://www.google.fr
# # https://www.t.co
# # http://www.tmall.com
# # http://www.google.com.br
# # https://www.360.cn
# # http://www.sohu.com
# # https://www.amazon.co.jp
# # http://www.pinterest.com
# # https://www.netflix.com
# # http://www.google.it
# # https://www.google.ru
# # https://www.microsoft.com
# # http://www.google.es
# # https://www.wordpress.com
# # http://www.gmw.cn
# # https://www.tumblr.com
# # http://www.paypal.com
# # http://www.blogspot.com
# # http://www.imgur.com
# # https://www.stackoverflow.com
# # https://www.aliexpress.com
# # https://www.naver.com
# # http://www.ok.ru
# # https://www.apple.com
# # http://www.github.com
# # http://www.chinadaily.com.cn
# # http://www.imdb.com
# # https://www.google.co.kr
# # http://www.fc2.com
# # http://www.jd.com
# # http://www.blogger.com
# # http://www.163.com
# # http://www.google.ca
# # https://www.whatsapp.com
# # https://www.amazon.in
# # http://www.office.com
# # http://www.google.co.id
# # http://www.youku.com
# # https://www.example.com
# # http://www.craigslist.org
# # https://www.amazon.de
# # http://www.nicovideo.jp
# # https://www.google.pl
# # http://www.soso.com
# # http://www.bilibili.com
# # http://www.dropbox.com
# # http://www.xinhuanet.com
# # http://www.outbrain.com
# # http://www.pixnet.net
# # http://www.alibaba.com
# # http://www.alipay.com
# # http://www.chrome.com
# # http://www.booking.com
# # http://www.googleusercontent.com
# # http://www.google.com.au
# # http://www.popads.net
# # http://www.cntv.cn
# # http://www.zhihu.com
# # https://www.amazon.co.uk
# # http://www.diply.com
# # http://www.coccoc.com
# # https://www.cnn.com
# # http://www.bbc.co.uk
# # https://www.twitch.tv
# # https://www.wikia.com
# # http://www.google.co.th
# # http://www.go.com
# # https://www.google.com.ph
# # http://www.doubleclick.net
# # http://www.onet.pl
# # http://www.googleadservices.com
# # http://www.accuweather.com
# # http://www.googleweblight.com
# # http://www.answers.yahoo.com"""


# # async def get(url, session):
# #     try:
# #         async with session.get(url=url) as response:
# #             resp = await response.read()
# #             print("Successfully got url {} with resp of length {}.".format(url, len(resp)))
# #     except Exception as e:
# #         print("Unable to get url {} due to {}.".format(url, e.__class__))


# # async def main(urls):
# #     async with aiohttp.ClientSession() as session:
# #         ret = await asyncio.gather(*(get(url, session) for url in urls))
# #     print("Finalized all. Return is a list of len {} outputs.".format(len(ret)))


# # urls = websites.split("\n")
# # start = time.time()
# # asyncio.run(main(urls))
# # end = time.time()

# # print("Took {} seconds to pull {} websites.".format(end - start, len(urls)))

# import aiohttp

# async def fetch_url(url):
#   async with aiohttp.ClientSession() as session:
#     async with session.get(url) as response:
#       if response.status == 200:
#         data = await response.text()
#         print(f"URL: {url}, Data: {data[:50]}...")  # Truncate for brevity
#       else:
#         print(f"Error fetching {url}: {response.status}")

# async def main():
#   urls = ["https://www.example.com", "https://www.python.org", "https://www.google.com"]
#   tasks = [aiohttp.create_task(fetch_url(url)) for url in urls]
#   await asyncio.gather(*tasks)

# #asyncio.run(main())
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())


import aiohttp
import asyncio
import os

from aiohttp import ClientSession


GOOGLE_BOOKS_URL = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
LIST_ISBN = [
    '9780002005883',
    '9780002238304',
    '9780002261982',
    '9780006163831',
    '9780006178736',
    '9780006280897',
    '9780006280934',
    '9780006353287',
    '9780006380832',
    '9780006470229',
]


def extract_fields_from_response(response):
    """Extract fields from API's response"""
    item = response.get("items", [{}])[0]
    volume_info = item.get("volumeInfo", {})
    title = volume_info.get("title", None)
    subtitle = volume_info.get("subtitle", None)
    description = volume_info.get("description", None)
    published_date = volume_info.get("publishedDate", None)
    return (
        title,
        subtitle,
        description,
        published_date,
    )


async def get_book_details_async(isbn, session):
    """Get book details using Google Books API (asynchronously)"""
    url = GOOGLE_BOOKS_URL + isbn
    try:
        response = await session.request(method='GET', url=url)
        response.raise_for_status()
        print(f"Response status ({url}): {response.status}")
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error ocurred: {err}")
    response_json = await response.json()
    return response_json


async def run_program(isbn, session):
    """Wrapper for running program in an asynchronous manner"""
    try:
        response = await get_book_details_async(isbn, session)
        parsed_response = extract_fields_from_response(response)
        print(f"Response: {json.dumps(parsed_response, indent=2)}")
    except Exception as err:
        print(f"Exception occured: {err}")
        pass
    async with ClientSession() as session:
    await asyncio.gather(*[run_program(isbn, session) for isbn in LIST_ISBN])