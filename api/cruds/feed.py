from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import api.models.feed as feed_model
import api.schemas.feed as feed_schema


async def create_feed(db: AsyncSession, feed_create: feed_schema.FeedCreate) -> feed_model.Feed:
    db_feed = feed_model.Feed(**feed_create.dict())
    db.add(db_feed)
    await db.commit()
    await db.refresh(db_feed)
    return db_feed


async def get_all_feeds(db: AsyncSession) -> list[feed_model.Feed]:
    result: Result = await db.execute(select(feed_model.Feed))
    return result.scalars().all()


async def get_feed(db: AsyncSession, feed_id: int) -> feed_model.Feed | None:
    result: Result = await db.execute(select(feed_model.Feed).where(feed_model.Feed.id == feed_id))
    return result.scalars().first()


async def delete_feed(db: AsyncSession, feed: feed_model.Feed) -> None:
    await db.delete(feed)
    await db.commit()
    return


async def update_feed(db: AsyncSession, latest_url: str, origin: feed_model.Feed) -> feed_model.Feed:
    origin.latest_article_url = latest_url  # type: ignore
    db.add(origin)
    await db.commit()
    await db.refresh(origin)
    return origin
