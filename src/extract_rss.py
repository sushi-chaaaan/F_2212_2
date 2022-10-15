import re

from bs4 import BeautifulSoup


def extract_rss_link(soup: BeautifulSoup) -> list[str] | None:
    links = []
    try:
        for link in soup.find_all("a", href=re.compile("rss")):
            print(li := link["href"])
            links.append(li)
        return links
    except Exception as e:
        print(e)
        return None
