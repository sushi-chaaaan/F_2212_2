from sqlalchemy import create_engine

from api.models.feed import Feed

DB_URL = "mysql+pymysql://root@db:3306/demo?charset=utf8"
engine = create_engine(DB_URL, echo=True)


def reset_database():
    Feed.metadata.drop_all(engine)
    Feed.metadata.create_all(engine)


if __name__ == "__main__":
    reset_database()
