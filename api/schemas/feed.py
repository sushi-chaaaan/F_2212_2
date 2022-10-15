from pydantic import BaseModel, Field


class FeedBase(BaseModel):
    base_url: str


class FeedCreate(FeedBase):
    url: str


class FeedCreateResponse(FeedCreate):
    id: int

    class Config:
        orm_mode = True


class Feed(FeedBase):
    id: int = Field(..., description="Feed ID")
    url: str
