from playwright.async_api import async_playwright
from .stealth import *


async def init_browser(
    playwright, headless: bool = True, browser: str = "chromium", proxy: str = None
):
    """
    Initialize a browser and create a new page with optional stealth settings.

    Parameters:
    - playwright (Playwright): An instance of the Playwright class.
    - headless (bool, optional): Whether to run the browser in headless mode. Default is True.
    - browser (str, optional): The browser to launch. Valid options are "chromium" (default), "firefox", or "webkit".
    - proxy (str, optional): Proxy server to use in the format "protocol://username:password@host:port". Default is None.

    Returns:
    tuple: A tuple containing the browser instance and the newly created page.

    Example:
    ```python
    async with async_playwright() as p:
        browser, page = await init_browser(p, headless=False, browser="firefox", proxy="http://username:password@proxy-server:8080")
        # Your code using the browser and page goes here
        await browser.close()
    ```

    Note:
    - If using a proxy, make sure to provide it in the format "protocol://username:password@host:port".
    - The 'stealth' module is used to apply stealth settings to the page, enhancing the browser automation stealthiness.
    """

    if browser == "firefox":
        chromium = playwright.firefox
    elif browser == "webkit":
        chromium = playwright.webkit
    else:
        chromium = playwright.chromium

    if proxy:
        browser = await chromium.launch(
            headless=headless,
            proxy=proxy,
        )
    else:
        browser = await chromium.launch(headless=headless)

    page = await browser.new_page()
    page = await stealth_page(page)

    return browser, page
