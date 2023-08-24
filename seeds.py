"""Populate DB."""

from dotenv import dotenv_values
from sqlalchemy import URL, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from database.config import Base
from database.models import Diner, Endorsement, Restaurant, Restriction, Table

DINERS = (
    'Jill', 'Jack', 'Gonz', 'Jane',
)

RESTRICTIONS = (
    'Lactose', 'Gluten', 'Vegan', 'Kosher',
)


ENDORSEMENTS = (
    'Lactose-Free', 'Gluten-Free', 'Vegan-Friendly', 'Kosher-Certified',
)

RESTAURANTS = (
    'Rosetta', 'Bellinis', 'Pujol', 'Anonimo',
)

TABLE_CAPACITY = (
    2, 4, 6, 8,
)


def create_diners(session):
    for diner in DINERS:
        dinner = Diner(name=diner)
        session.add(dinner)
    session.commit()


def create_restrictions(session):
    for restriction in RESTRICTIONS:
        restriction = Restriction(name=restriction)
        session.add(restriction)
    session.commit()


def create_endorsements(session):
    for endorsement in ENDORSEMENTS:
        endorsement = Endorsement(name=endorsement)
        session.add(endorsement)
    session.commit()


def create_restaurant(session):
    for restaurant in RESTAURANTS:
        restaurant = Restaurant(name=restaurant)
        session.add(restaurant)
    session.commit()


def create_tables(session):
    for table in TABLE_CAPACITY:
        table = Table(capacity=table)
        session.add(table)
    session.commit()


if __name__ == '__main__':
    config = dotenv_values()
    url = URL.create(
        'postgresql',
        username=config['DB_USER'],
        password=config['DB_PASSWORD'],
        host=config['DB_HOST'],
        database=config['DB_NAME'],
        port=config['DB_PORT'],
    )
    engine = create_engine(url)
    db_session = scoped_session(
        sessionmaker(
            bind=engine,
            autocommit=False,
            autoflush=False,
        ),
    )
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    with db_session() as session:
        create_diners(db_session)
        create_restrictions(db_session)
        create_endorsements(db_session)
        create_restaurant(db_session)
        create_tables(db_session)
