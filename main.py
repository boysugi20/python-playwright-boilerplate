import asyncio
from functions.page import *

PROXY = {"server": "http://myproxy.com:3128", "username": "usr", "password": "pwd"}


async def run(playwright, proxy_info: dict):
    browser, page = await init_browser(
        playwright, headless=False, browser="chromium", proxy=proxy_info
    )

    await page.goto("http://bot.sannysoft.com")
    await page.screenshot(path="screenshot/example.png", full_page=True)

    await browser.close()


async def main():
    async with async_playwright() as playwright:
        await run(playwright, proxy_info=PROXY)


asyncio.run(main())
