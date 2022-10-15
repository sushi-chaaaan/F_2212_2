from pydantic import BaseModel, Field


class FeedBase(BaseModel):
    url: str


class FeedCreate(FeedBase):
    pass


class FeedCreateResponse(FeedCreate):
    id: int

    class Config:
        orm_mode = True


class Feed(FeedBase):
    id: int = Field(..., description="Feed ID")
