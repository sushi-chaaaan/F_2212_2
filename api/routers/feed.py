from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.cruds import feed as feed_crud
from api.db import get_db
from api.schemas import feed as feed_schema
from src.extract_rss import extract_rss

router = APIRouter()


@router.post("/feed", response_model=feed_schema.FeedCreateResponse)
async def create_feed(url: str, db: AsyncSession = Depends(get_db)):
    rss_urls: list[str] = await extract_rss(url)
    if rss_urls == []:
        raise HTTPException(status_code=400, detail="RSS not found or some error occurred.")
    else:
        # TODO:今のところ複数RSSがあった場合どうしようもないので要再検討
        feed = feed_schema.FeedCreate(url=rss_urls[0])
        # print(feed.url)
        return await feed_crud.create_feed(db, feed)


@router.get("/feed", response_model=list[feed_schema.Feed])
async def get_all_feeds():
    return [feed_schema.Feed(id=1, url="https://example.com/rss")]


@router.get("/feed/{feed_id}", response_model=feed_schema.Feed)
async def get_single_feed(feed_id: int):
    return feed_schema.Feed(id=feed_id, url="https://example.com/rss")


@router.delete("/feed/{feed_id}", response_model=None)
async def delete_feed():
    return None
