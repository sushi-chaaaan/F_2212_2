import re

from src.scraper import scrape_page


def get_root_url(url: str) -> str:
    url_root_filter = re.compile(r"(https?|ftp)(:\/\/[-_.!~*\'()a-zA-Z0-9;?:\@&=+\$,%#]+/)")

    res = url_root_filter.match(url)
    if res:
        return res.group()
    else:
        raise Exception("Invalid URL. cannot get root url.")


async def extract_rss(base_url: str) -> list[str]:  # type: ignore
    # スクレイピング
    soup = await scrape_page(base_url)

    rss_link: list[str] = []
    # RSSリンクを取得
    try:
        for link in soup.find_all("a", href=re.compile("rss")):
            rss_link.append(link["href"])
    except Exception as e:
        print(e)
    else:
        # print(rss_link)
        root_url = get_root_url(base_url)
        if not root_url.endswith("/"):
            root_url += "/"
        # print(root_url)
        match len(rss_link):
            case 0:
                return []
            case 1:
                rss_link = [rss_link[0][0] if not rss_link[0][0].startswith("/") else root_url + rss_link[0][1:]]
                # print(rss_link)
                return rss_link
            case _:
                raise Exception("Multiple RSS links found. Please specify the RSS link.")


# DEBUG-CODE
# if __name__ == "__main__":
#     import asyncio

#     asyncio.run(extract_rss("https://www.watch.impress.co.jp/"))
