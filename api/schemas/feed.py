from pydantic import BaseModel, Field


class FeedBase(BaseModel):
    base_url: str


class FeedCreate(FeedBase):
    rss_url: str | None = Field(None, example="https://example.com/rss")
    pass


class FeedCreateResponse(FeedCreate):
    id: int

    class Config:
        orm_mode = True


class Feed(FeedBase):
    id: int = Field(..., description="Feed ID")
    rss_url: str
