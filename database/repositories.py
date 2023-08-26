"""Models repositories."""

from datetime import datetime
from typing import List

from sqlalchemy.orm import Session

from app.helpers import build_reservation_url
from database.interface import BaseRepository
from database.models import Diner, DinersRestrictions, Reservation, Table
from domain.models import Diner as DomainDiner
from domain.models import Reservation as DomainReservation
from domain.models import Restaurant as DomainRestaurant
from domain.models import Table as DomainTable


class TableRepository(BaseRepository):
    """Table repository."""

    def __init__(self, session: Session, base_model=Table, entity=DomainTable):
        self._session = session
        self._base_model = base_model
        self._entity = entity

    def get_by_id(self, table_id):
        return self._session.query(self._base_model).get(table_id)

    def get_all(self):
        return self._session.query(self._base_model).all()

    def get_available_restaurant_tables_by_capacity(
        self,
        available_at: datetime,
        diners_restrictions: List[DinersRestrictions],
        restaurant_entity=DomainRestaurant,
    ):
        tables = self._base_model.get_available_restaurant_tables_by_capacity(
            available_at=available_at,
            diners_restrictions=diners_restrictions,
            session=self._session,
        )

        diners_ids = {diner_restriction.diner.id for diner_restriction in diners_restrictions}

        return [
            self._entity(
                id=table.id,
                capacity=table.capacity,
                restaurant=restaurant_entity(
                    id=table.restaurant.id,
                    name=table.restaurant.name,
                ),
                available_at=table.available_at,
                reservation_url=build_reservation_url(table.id, diners_ids),
            )
            for table in tables
        ]


class DinersRestrictionsRepository(BaseRepository):
    def __init__(self, session: Session, base_model=DinersRestrictions):
        self._session = session
        self._base_model = base_model

    def get_by_id(self, diners_restriction_id):
        return self._session.query(self._base_model).get(diners_restriction_id)

    def get_all(self):
        return self._session.query(self._base_model).all()

    def get_all_by_diners(self, diners):
        return self._base_model.get_all_by_diners(
            diners=diners,
            session=self._session,
        )


class DinerRepository(BaseRepository):
    """Diner repository."""

    def __init__(self, session: Session, base_model=Diner):
        self._session = session
        self._base_model = base_model

    def get_by_id(self, diner_id):
        return self._session.query(self._base_model).get(diner_id)

    def get_all(self):
        return self._session.query(self._base_model).all()

    def get_all_by_id(self, diners_id):
        return self._base_model.get_all_by_id(
            session=self._session,
            diners_id=diners_id,
        )

    def get_all_by_name(self, diners_name):
        return self._base_model.get_all_by_name(
            session=self._session,
            diners_name=diners_name,
        )


class ReservationRepository(BaseRepository):
    def __init__(self, session: Session, base_model=Reservation, entity=DomainReservation):
        self._session = session
        self._base_model = base_model
        self._entity = entity

    def get_by_id(self, diners_restriction_id):
        return self._session.query(self._base_model).get(diners_restriction_id)

    def get_all(self):
        return self._session.query(self._base_model).all()

    def create_reservation(  # noqa: WPS211
        self,
        diner,
        table,
        booked_at,
        restaurant_entity=DomainRestaurant,
        diner_entity=DomainDiner,
        table_entity=DomainTable,
    ):
        reservation = self._base_model.create_reservation(
            session=self._session,
            diner=diner,
            table=table,
            booked_at=booked_at,
        )

        return self._entity(
            id=reservation.id,
            booked_at=reservation.booked_at,
            diner=diner_entity(
                id=reservation.diner.id,
                name=reservation.diner.name,
            ),
            table=table_entity(
                id=reservation.table.id,
                available_at=reservation.table.available_at,
                capacity=reservation.table.capacity,
                restaurant=restaurant_entity(
                    id=reservation.table.restaurant.id,
                    name=reservation.table.restaurant.name,
                ),
            ),
        )

    def verify_reservation(
        self,
        diners,
        restaurant_entity=DomainRestaurant,
        diner_entity=DomainDiner,
        table_entity=DomainTable,
    ):
        reservations = self._base_model.verify_reservations(
            session=self._session,
            diners=diners,
        )

        return [
            self._entity(
                id=reservation.id,
                booked_at=reservation.booked_at,
                diner=diner_entity(
                    id=reservation.diner.id,
                    name=reservation.diner.name,
                ),
                table=table_entity(
                    id=reservation.table.id,
                    available_at=reservation.table.available_at,
                    capacity=reservation.table.capacity,
                    restaurant=restaurant_entity(
                        id=reservation.table.restaurant.id,
                        name=reservation.table.restaurant.name,
                    ),
                ),
            ) for reservation in reservations
        ]

    def delete_reservation(self, diner_id):
        self._base_model.delete_reservation(self._session, diner_id)
