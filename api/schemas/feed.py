from pydantic import AnyUrl, BaseModel, Field


class FeedBase(BaseModel):
    rss_url: AnyUrl


class FeedCreate(FeedBase):
    latest_article_url: AnyUrl = Field(..., description="The latest article url of the feed")


class FeedCreateResponse(FeedCreate):
    id: int

    class Config:
        orm_mode = True


class Feed(FeedBase):
    id: int = Field(..., description="Feed ID")

    class Config:
        orm_mode = True


class UpdatedFeedBase(Feed):
    class Config:
        orm_mode = True


class Article(BaseModel):
    article_url: AnyUrl = Field(..., description="Article URL")
    article_title: str = Field(..., description="Article title")


class UpdatedFeedResponse(UpdatedFeedBase):
    articles: list[Article] = Field(..., description="List of new articles")
