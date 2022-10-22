import aiohttp
from bs4 import BeautifulSoup
from bs4.builder.__init__ import XMLParsedAsHTMLWarning


async def scrape_page(url: str) -> BeautifulSoup:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
            try:
                soup = BeautifulSoup(html, "html.parser")
            except XMLParsedAsHTMLWarning:
                soup = BeautifulSoup(
                    html,
                    "xml",
                )
            return soup
