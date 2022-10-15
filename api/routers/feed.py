from fastapi import APIRouter

from api.schemas import feed as feed_schema

router = APIRouter()


@router.post("/feed", response_model=feed_schema.Feed)
async def register_feed(url: str):
    pass


@router.get("/feed", response_model=list[feed_schema.Feed])
async def list_feed():
    return [feed_schema.Feed(id=1, base_url="https://example.com", rss_url="https://example.com/rss")]


@router.delete("/feed/{feed_id}", response_model=feed_schema.Feed)
async def delete_feed():
    pass
