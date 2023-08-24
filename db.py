from database.models import Base
from database.config import engine


def init_db():
    Base.metadata.create_all(engine)
    print("Initialized the db")


if __name__ == "__main__":
    init_db()
