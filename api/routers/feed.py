from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from api.cruds import feed as feed_crud
from api.db import get_db
from api.schemas import feed as feed_schema
from src.extract_rss import extract_rss
from src.parse_rss import get_latest_article_url, parse_rss

router = APIRouter()


@router.post("/feed", response_model=feed_schema.FeedCreateResponse)
async def create_feed(url: str, db: AsyncSession = Depends(get_db)):
    # FIXME: RSSのURLを直接投げられると死ぬ致命的な欠点がある
    # 直したけどこれでいいのか？
    # TODO: 重複している場合登録しない処理を作りたかったが間に合わない

    if url.endswith(".rdf") or url.endswith(".xml"):
        # .rdf or .xmlの場合は、RSSのURLだと推定する。正直危険
        _url = url
    else:
        rss_urls: list[str] = await extract_rss(url)
        if rss_urls == []:
            raise HTTPException(status_code=400, detail="RSS not found or some error occurred.")
        else:
            # FIXME: 複数RSSがあった場合どうしようもない
            _url = rss_urls[0]
    _latest_article_url = get_latest_article_url(_url)
    feed = feed_schema.FeedCreate(rss_url=_url, latest_article_url=_latest_article_url)  # type: ignore
    # print(feed.url)
    return await feed_crud.create_feed(db, feed)


@router.get("/feed", response_model=list[feed_schema.Feed])
async def get_all_feeds(db: AsyncSession = Depends(get_db)):
    return await feed_crud.get_all_feeds(db)


@router.get("/feed/{feed_id}", response_model=feed_schema.Feed)
async def get_single_feed(feed_id: int, db: AsyncSession = Depends(get_db)):
    return await feed_crud.get_feed(db, feed_id)


@router.delete("/feed/{feed_id}")
async def delete_feed(feed_id: int, db: AsyncSession = Depends(get_db)):
    _feed = await feed_crud.get_feed(db, feed_id)
    if _feed is None:
        raise HTTPException(status_code=404, detail="Feed not found.")
    try:
        await feed_crud.delete_feed(db, _feed)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    else:
        return JSONResponse(content={"message": "Feed deleted."}, status_code=status.HTTP_200_OK)


@router.get("/update", response_model=list[feed_schema.UpdatedFeedResponse])
async def return_update_feed(db: AsyncSession = Depends(get_db)):
    # get all feeds
    feeds = await feed_crud.get_all_feeds(db)

    updated_feed: list[feed_schema.UpdatedFeedResponse] = []
    for feed in feeds:
        new_entries = await parse_rss(rss_url=feed.rss_url, latest_article_url_before_update=feed.latest_article_url)  # type: ignore
        new_articles = [feed_schema.Article(article_url=entry.link, article_title=entry.title) for entry in new_entries]
        response = feed_schema.UpdatedFeedResponse(rss_url=feed.rss_url, id=feed.id, articles=new_articles)  # type: ignore
        updated_feed.append(response)
        await feed_crud.update_feed(db, latest_url=new_entries[0].link, origin=feed)
    return updated_feed
