"""SQLAlchemy Data Models."""
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, String

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
