import aiohttp
from bs4 import BeautifulSoup


async def scrape_page(url: str) -> BeautifulSoup:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
            soup = BeautifulSoup(html, "html.parser")
            return soup
