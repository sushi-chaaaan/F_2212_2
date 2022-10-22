from sqlalchemy import Column, Integer, String

from api.db import Base


class Feed(Base):
    __tablename__ = "feeds"

    id = Column(Integer, primary_key=True, index=True)
    rss_url = Column(String(255), nullable=False)
    latest_article_url = Column(String(255), nullable=False)
