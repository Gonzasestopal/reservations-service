"""Models repositories."""

from sqlalchemy.orm import Session

from domain.models import Restaurant as DomainRestaurant
from domain.models import Table as DomainTable

from .interface import BaseRepository
from .models import Diner, DinersRestrictions, Table


class TableRepository(BaseRepository):
    """Table repository."""

    def __init__(self, session: Session):
        self._session = session
        self._base_model = Table
        self._entity = DomainTable

    def get_by_id(self, table_id):
        return self._session.query(self._base_model).get(table_id).first()

    def get_all(self):
        return self._session.query(self._base_model).all()

    def get_available_restaurant_tables_by_capacity(self, available_at, diners_restrictions):
        tables = self._base_model.get_available_restaurant_tables_by_capacity(
            available_at=available_at,
            diners_restrictions=diners_restrictions,
            session=self._session,
        )
        return [
            self._entity(
                id=table.id,
                capacity=table.capacity,
                restaurant=DomainRestaurant(
                    id=table.restaurant.id,
                    name=table.restaurant.name,
                ),
                available_at=table.available_at,
            )
            for table in tables
        ]


class DinersRestrictionsRepository(BaseRepository):
    def __init__(self, session: Session):
        self._session = session
        self._base_model = DinersRestrictions

    def get_by_id(self, diners_restriction_id):
        return self._session.query(self._base_model).get(diners_restriction_id).first()

    def get_all(self):
        return self._session.query(self._base_model).all()

    def get_all_by_diners(self, diners):
        return self._base_model.get_all_by_diners(
            diners=diners,
            session=self._session,
        )

class DinerRepository(BaseRepository):
    """Diner repository."""

    def __init__(self, session: Session):
        self._session = session
        self._base_model = Diner

    def get_by_id(self, diner_id):
        return self._session.query(self._base_model).get(diner_id).first()

    def get_all(self):
        return self._session.query(self._base_model).all()

    def get_all_by_name(self, diners_name):
        return self._base_model.get_all_by_name(
            session=self._session,
            diners_name=diners_name,
        )


