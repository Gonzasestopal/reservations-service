"""Models repositories."""

from sqlalchemy.orm import Session

from domain.models import Restaurant as DomainRestaurant
from domain.models import Table as DomainTable

from .interface import BaseRepository
from .models import Table


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

    def get_available_restaurant_tables_by_capacity(self, available_at, capacity):
        tables = self._base_model.get_available_restaurant_tables_by_capacity(
            available_at=available_at,
            capacity=capacity,
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
