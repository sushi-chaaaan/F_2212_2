from sqlalchemy import Column, Integer, String

from api.db import Base


class Feed(Base):
    __tablename__ = "feeds"

    id = Column(Integer, primary_key=True, index=True)
    base_url = Column(String(255), nullable=False)
    rss_url = Column(String(255), nullable=False)

    def __repr__(self):
        return f"Feed(id={self.id}, base_url={self.base_url}, rss_url={self.rss_url})"
