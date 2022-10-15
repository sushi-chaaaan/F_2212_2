from sqlalchemy.ext.asyncio import AsyncSession

import api.models.feed as feed_model
import api.schemas.feed as feed_schema


async def create_feed(db: AsyncSession, feed_create: feed_schema.FeedCreate) -> feed_model.Feed:
    db_feed = feed_model.Feed(**feed_create.dict())
    db.add(db_feed)
    await db.commit()
    await db.refresh(db_feed)
    return db_feed
