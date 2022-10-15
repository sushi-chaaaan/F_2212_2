from pydantic import BaseModel, Field


class Feed(BaseModel):
    id: int = Field(..., description="Feed ID")
    base_url: str
    rss_url: str
