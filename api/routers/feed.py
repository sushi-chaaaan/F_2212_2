from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.cruds import feed as feed_crud
from api.db import get_db
from api.schemas import feed as feed_schema

router = APIRouter()


@router.post("/feed", response_model=feed_schema.FeedCreateResponse)
async def create_feed(feed: feed_schema.FeedCreate, db: AsyncSession = Depends(get_db)):
    # TODO:ここでRSS取得処理を行う

    return await feed_crud.create_feed(db, feed)


@router.get("/feed", response_model=list[feed_schema.Feed])
async def list_feed():
    return [feed_schema.Feed(id=1, base_url="https://example.com", rss_url="https://example.com/rss")]


@router.delete("/feed/{feed_id}", response_model=None)
async def delete_feed():
    return None
