"""Repositories tests."""

from unittest.mock import Mock, call

from expects import contain, equal, expect
from mamba import after, before, describe, it

from database import repositories

with describe(repositories.DinerRepository) as self:
    with before.each:
        self.session = Mock()
        self.base_model = Mock()

    with it('should get available diners by id'):
        diner_repository = repositories.DinerRepository(self.session, self.base_model)

        diner_repository.get_all_by_id([1, 2])

        expect(self.base_model.get_all_by_id.call_args).to(equal(
            call(
                session=self.session,
                diners_id=[1, 2],
            ),
        ))

    with it('should get available diners by name'):
        diner_repository = repositories.DinerRepository(self.session, self.base_model)

        diner_repository.get_all_by_name(['Gonz', 'Jill'])

        expect(self.base_model.get_all_by_name.call_args).to(equal(
            call(
                session=self.session,
                diners_name=['Gonz', 'Jill'],
            ),
        ))


with describe(repositories.ReservationRepository) as self:
    with before.each:
        self.session = Mock()
        self.base_model = Mock()
        self.entity = Mock()
        self.table = Mock()
        self.diner = Mock()

    with it('should create reservation'):
        restaurant_entity = Mock()
        diner_entity = Mock()
        table_entity = Mock()
        reservation_repository = repositories.ReservationRepository(self.session, self.base_model, self.entity)

        reservation_repository.create_reservation(
            table=self.table,
            diner=self.diner,
            booked_at='now',
            diner_entity=diner_entity,
            restaurant_entity=restaurant_entity,
            table_entity=table_entity,
        )

        expect(self.base_model.create_reservation.call_args).to(equal(
            call(
                session=self.session,
                table=self.table,
                diner=self.diner,
                booked_at='now',
            ),
        ))

    with it('should return domain data representation'):
        reservation_repository = repositories.ReservationRepository(self.session, self.base_model, self.entity)
        reservation = Mock()
        restaurant_entity = Mock()
        diner_entity = Mock()
        table_entity = Mock()

        reservation = reservation_repository.create_reservation(
            table=self.table,
            diner=self.diner,
            booked_at='now',
            diner_entity=diner_entity,
            restaurant_entity=restaurant_entity,
            table_entity=table_entity,
        )

        entity_one = self.entity(
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

        expect(reservation).to(equal(entity_one))


with describe(repositories.DinersRestrictionsRepository) as self:
    with before.each:
        self.session = Mock()
        self.base_model = Mock()

    with it('should create reservation'):
        gonz = Mock()
        jill = Mock()
        reservation_repository = repositories.DinersRestrictionsRepository(self.session, self.base_model)

        reservation_repository.get_all_by_diners(
            diners=[gonz, jill],
        )

        expect(self.base_model.get_all_by_diners.call_args).to(equal(
            call(
                session=self.session,
                diners=[gonz, jill],
            ),
        ))


with describe(repositories.TableRepository) as self:
    with before.each:
        self.session = Mock()
        self.base_model = Mock()
        self.entity = Mock()

    with it('should create reservation'):
        diner_with_vegan_restriction = Mock()
        diner_with_fit_restriction = Mock()
        tables = [Mock(), Mock()]
        self.base_model.get_available_restaurant_tables_by_capacity.return_value = tables
        table_repository = repositories.TableRepository(self.session, self.base_model, self.entity)

        table_repository.get_available_restaurant_tables_by_capacity(
            available_at='now',
            diners_restrictions=[diner_with_vegan_restriction, diner_with_fit_restriction],
            restaurant_entity=Mock(),
        )

        expect(self.base_model.get_available_restaurant_tables_by_capacity.call_args).to(equal(
            call(
                available_at='now',
                diners_restrictions=[diner_with_vegan_restriction, diner_with_fit_restriction],
                session=self.session,
            ),
        ))

    with it('should return domain data representation'):
        diner_with_vegan_restriction = Mock()
        diner_with_fit_restriction = Mock()
        restaurant_entity = Mock()
        table_one = Mock()
        table_two = Mock()
        tables = [table_one, table_two]
        self.base_model.get_available_restaurant_tables_by_capacity.return_value = tables
        table_repository = repositories.TableRepository(self.session, self.base_model, self.entity)

        tables = table_repository.get_available_restaurant_tables_by_capacity(
            available_at='now',
            diners_restrictions=[diner_with_vegan_restriction, diner_with_fit_restriction],
            restaurant_entity=restaurant_entity,
        )

        entity_one = self.entity(
            id=table_one.id,
            capacity=table_one.capacity,
            restaurant=restaurant_entity(
                id=table_one.restaurant.id,
                name=table_one.restaurat.name,
            ),
            available_at=table_one.available_at,
        )

        expect(tables).to(contain(entity_one))
