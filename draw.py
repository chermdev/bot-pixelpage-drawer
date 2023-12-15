import asyncio

import httpx


headers = {
    'authority': 'pixelpage.deno.dev',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,es-MX;q=0.8,es;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://pixelpage.deno.dev',
    'pragma': 'no-cache',
    'referer': 'https://pixelpage.deno.dev/',
    'sec-ch-ua': ('"Not_A Brand";v="8", '
                  '"Chromium";v="120",'
                  '"Google Chrome";v="120"'),
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/120.0.0.0 Safari/537.36'),
}


def calc_pos(x, y):
    return y + (16 * x)


async def paint_color(pos: int, color: str):
    try:
        async with httpx.AsyncClient() as ac:
            await ac.request('POST', 'https://pixelpage.deno.dev/api/update',
                             headers=headers, json=[pos, color])
        print(f"Request {pos} sent color {color}")
    except Exception as e:
        print(f"Request {pos} timeout: {e}")


async def async_requests(pixels):
    tasks = [paint_color(pos, color) for pos, color in pixels]
    return await asyncio.gather(*tasks, return_exceptions=True)


def draw(pixels: list):
    print(f"Sending {len(pixels)} requests")
    asyncio.run(async_requests(pixels))
