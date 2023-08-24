"""SQLAlchemy Data Models."""
from sqlalchemy import Column, ForeignKey, extract
from sqlalchemy.orm import Session, joinedload, relationship
from sqlalchemy.types import DateTime, Integer, String

from database.config import Base


class Diner(Base):
    """Diner Model."""

    __tablename__ = 'diners'

    id = Column(Integer, primary_key=True, autoincrement='auto')
    name = Column(String(100), unique=True, nullable=False)


class Restriction(Base):
    """Restriction model."""

    __tablename__ = 'restrictions'

    id = Column(Integer, primary_key=True, autoincrement='auto')
    name = Column(String(50), unique=True, nullable=False)


class DinersRestrictions(Base):
    """DinersRestriction model."""

    __tablename__ = 'diners_restrictions'

    id = Column(Integer, primary_key=True, autoincrement='auto')
    diner_id = Column(
        'diner_id',
        Integer,
        ForeignKey('diners.id', name='fk_diners_restrictions_diner_id'),
    )
    diner = relationship(Diner)
    restriction_id = Column(
        'restriction_id',
        Integer,
        ForeignKey('restrictions.id', name='fk_diners_restrictions_restriction_id'),
    )
    restriction = relationship(Restriction)


class Restaurant(Base):
    """Restaurant model."""

    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True, autoincrement='auto')
    name = Column(String(50), unique=True, nullable=False)


class Endorsement(Base):
    """Endorsement model."""

    __tablename__ = 'endorsements'

    id = Column(Integer, primary_key=True, autoincrement='auto')
    name = Column(String(50), unique=True, nullable=False)


class RestaurantsEndorsements(Base):
    """RestaurantsEndorsements model."""

    __tablename__ = 'restaurants_endorsements'

    id = Column(Integer, primary_key=True, autoincrement='auto')
    restaurant_id = Column(
        'restaurant_id',
        Integer,
        ForeignKey('restaurants.id', name='fk_restaurants_endorsements_restaurant_id'),
    )
    restaurant = relationship(Restaurant)
    endorsement_id = Column(
        'endorsement_id',
        Integer,
        ForeignKey('endorsements.id', name='fk_restaurants_endorsements_endorsement_id'),
    )
    endorsement = relationship(Endorsement)


class Table(Base):
    """Table model."""

    __tablename__ = 'tables'

    id = Column(Integer, primary_key=True, autoincrement='auto')
    capacity = Column(Integer, nullable=False)
    restaurant_id = Column(
        'restaurant_id',
        Integer,
        ForeignKey('restaurants.id', name='fk_table_restaurant_id'),
    )
    restaurant = relationship(Restaurant)
    available_at = Column(DateTime, nullable=False)

    @classmethod
    def get_available_restaurant_tables_by_capacity(cls, session, available_at, capacity):
        return session.query(Table).options(
            joinedload(Table.restaurant),
        ).join(
            Restaurant, Table.restaurant_id == Restaurant.id,
        ).filter(
            Table.capacity >= capacity,
            extract('day', Table.available_at) == available_at.day,
            extract('month', Table.available_at) == available_at.month,
            extract('year', Table.available_at) == available_at.year,
            extract('hour', Table.available_at) == available_at.hour,
            extract('minute', Table.available_at) == available_at.minute,
        ).all()


class Reservation(Base):
    """Reservation model."""

    __tablename__ = 'reservations'

    id = Column(Integer, primary_key=True, autoincrement='auto')
    table_id = Column(
        'table_id',
        Integer,
        ForeignKey('tables.id', name='fk_reservations_table_id'),
    )
    table = relationship(Table)
    diner_id = Column(
        'diner_id',
        Integer,
        ForeignKey('diners.id', name='fk_reservations_diner_id'),
    )
    diner = relationship(Diner)


metadata = Base.metadata
