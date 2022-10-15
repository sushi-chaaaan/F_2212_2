from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.cruds import feed as feed_crud
from api.db import get_db
from api.schemas import feed as feed_schema
from src.extract_rss import extract_rss

router = APIRouter()


@router.post("/feed", response_model=feed_schema.FeedCreateResponse)
async def create_feed(feed: feed_schema.FeedCreate, db: AsyncSession = Depends(get_db)):
    rss_urls: list[str] = await extract_rss(feed.base_url)
    if rss_urls == []:
        raise HTTPException(status_code=400, detail="RSS not found or some error occurred.")
    else:
        # TODO:今のところ複数RSSがあった場合どうしようもないので要再検討
        feed.rss_url = rss_urls[0]
        print(feed.rss_url)
        return await feed_crud.create_feed(db, feed)


@router.get("/feed", response_model=list[feed_schema.Feed])
async def list_feed():
    return [feed_schema.Feed(id=1, base_url="https://example.com", rss_url="https://example.com/rss")]


@router.delete("/feed/{feed_id}", response_model=None)
async def delete_feed():
    return None
