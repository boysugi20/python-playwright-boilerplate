from playwright_stealth import stealth_async
from fake_useragent import UserAgent


async def stealth_page(page):
    """
    Apply stealth settings to a Playwright page, including using a random User-Agent.

    Parameters:
    - page (Page): The Playwright page to which stealth settings will be applied.

    Returns:
    Page: The modified Playwright page.

    Example:
    ```python
    async with async_playwright() as p:
        browser, page = await init_browser(p)
        page = await stealth_page(page)
        # Your code using the modified page goes here
    ```

    Note:
    - The 'playwright_stealth' module is used to apply additional stealth settings to the page.
    - The 'fake_useragent' library is used to generate a random User-Agent for increased anonymity.
    """
    # Use playwright_stealth for additional stealth settings
    await stealth_async(page)

    # Set a random User-Agent using fake_useragent
    ua = UserAgent(browsers=["chrome"])
    user_agent = ua.random
    await page.set_extra_http_headers({"User-Agent": user_agent})

    return page
