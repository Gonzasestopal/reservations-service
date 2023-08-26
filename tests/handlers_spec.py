"""Handlers tests."""

from datetime import datetime, timedelta
from unittest.mock import Mock

from expects import be_true, equal, expect, raise_error
from mamba import before, describe, it

from app.errors import ExistingBookingError
from app.handlers import generate_reservation

with describe(generate_reservation) as self:
    with before.each:
        self.table_repository = Mock()
        self.diner_repository = Mock()
        self.reservation_repository = Mock()

        self.table_repository_cls = Mock(return_value=self.table_repository)
        self.diner_repository_cls = Mock(return_value=self.diner_repository)
        self.reservation_repository_cls = Mock(return_value=self.reservation_repository)

    with it('should verify for existing reservations'):
        self.reservation_repository.verify_reservation.return_value = []
        self.diner_repository.get_all_by_id.return_value = [Mock()]

        reservation = generate_reservation(
            1,
            [1, 2, 3],
            diner_repository_cls=self.diner_repository_cls,
            table_repository_cls=self.table_repository_cls,
            reservation_repository_cls=self.reservation_repository_cls,
        )

        expect(self.reservation_repository.verify_reservation.called).to(be_true)

    with it('should verify and generate reservation'):
        self.reservation_repository.verify_reservation.return_value = []
        self.diner_repository.get_all_by_id.return_value = [Mock()]

        reservation = generate_reservation(
            1,
            [1, 2, 3],
            diner_repository_cls=self.diner_repository_cls,
            table_repository_cls=self.table_repository_cls,
            reservation_repository_cls=self.reservation_repository_cls,
        )

        expect(self.reservation_repository.create_reservation.called).to(be_true)

    with it('should not generate reservation if existing reservation found'):
        self.table_repository.get_by_id.return_value = Mock(available_at=datetime.now())
        self.reservation_repository.verify_reservation.return_value = [Mock(booked_at=datetime.now())]
        self.diner_repository.get_all_by_id.return_value = [Mock()]

        expect(lambda: generate_reservation(
            1,
            [1, 2, 3],
            diner_repository_cls=self.diner_repository_cls,
            table_repository_cls=self.table_repository_cls,
            reservation_repository_cls=self.reservation_repository_cls,
        )).to(raise_error(ExistingBookingError))


    with it('should generate reservation if existing reservation found but its 2 hour from now'):
        self.table_repository.get_by_id.return_value = Mock(available_at=datetime.now())
        self.reservation_repository.verify_reservation.return_value = [Mock(booked_at=datetime.now() + timedelta(hours=3))]
        self.diner_repository.get_all_by_id.return_value = [Mock(), Mock(), Mock()]

        reservations = generate_reservation(
            1,
            [1, 2, 3],
            diner_repository_cls=self.diner_repository_cls,
            table_repository_cls=self.table_repository_cls,
            reservation_repository_cls=self.reservation_repository_cls,
        )

        reservation_one = self.reservation_repository.create_reservation.return_value
        reservation_two = self.reservation_repository.create_reservation.return_value
        reservation_three = self.reservation_repository.create_reservation.return_value

        expect(reservations).to(equal([reservation_one, reservation_two, reservation_three]))
