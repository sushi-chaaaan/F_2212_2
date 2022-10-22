import feedparser


async def parse_rss(rss_url: str, latest_article_url_before_update: str):
    feed = feedparser.parse(rss_url)

    new_feeds = []
    for i, entry in enumerate(feed.entries):
        if entry.link == latest_article_url_before_update:
            _latest_before_update = i
            new_feeds = feed.entries[:_latest_before_update]
    return new_feeds


def get_latest_article_url(rss_url: str) -> str:
    feed = feedparser.parse(rss_url)
    return feed.entries[0].link


# if __name__ == "__main__":
#     print(
#         parse_rss(
#             "https://www.watch.impress.co.jp/data/rss/1.0/ipw/feed.rdf",
#             "https://www.watch.impress.co.jp/docs/news/1449695.html",
#         )
#     )
