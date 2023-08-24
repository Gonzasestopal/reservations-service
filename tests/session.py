"""SQLAlchemy Session helper."""

from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker

from database import Base

engine = create_engine('sqlite://', echo=True)


def attach_session():
    """Create temp session."""
    session = scoped_session(sessionmaker(bind=engine, expire_on_commit=False))
    session.connection().execute(text(
        "ATTACH DATABASE ':memory:' AS {schema}".format(schema='public'),
    ))
    Base.metadata.create_all(engine)
    return session


def detach_session(session):
    """Cleanup temp session."""
    Base.metadata.drop_all(bind=engine)
    session.connection().detach()
    session.close()
