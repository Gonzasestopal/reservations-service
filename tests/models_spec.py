"""Models tests."""

from datetime import datetime

from expects import be_empty, be_none, contain, equal, expect
from mamba import after, before, describe, it

from database.models import (
    Diner,
    DinersRestrictions,
    Endorsement,
    Reservation,
    Restaurant,
    RestaurantsEndorsements,
    Restriction,
    Table,
)
from tests.fixtures import (
    add_extra_restriction_to_diner,
    create_healthy_diner,
    create_kosher_diner,
    create_vegan_diner,
    create_vegan_healthy_restaurant,
)
from tests.session import attach_session, detach_session

with describe(Diner) as self:
    with before.each:
        self.session = attach_session()

    with after.each:
        detach_session(self.session)

    with it('should have name'):
        diner = Diner(
            name='Jill',
        )
        self.session.add(diner)
        self.session.commit()

        expect(diner.name).to(equal('Jill'))

    with it('should get all diners by name'):
        diner = Diner(
            name='Jill',
        )
        diner_two = Diner(
            name='Jack',
        )
        self.session.add(diner)
        self.session.add(diner_two)
        self.session.commit()

        diners = Diner.get_all_by_name(self.session, ['Jack', 'Jill'])

        expect(diners).to(contain(diner_two, diner))

with describe(Restriction) as self:
    with before.all:
        self.session = attach_session()

    with after.all:
        detach_session(self.session)

    with it('should have name'):
        restriction = Restriction(
            name='Vegan',
        )
        self.session.add(restriction)
        self.session.commit()

        expect(restriction.name).to(equal('Vegan'))

    with it('should have an endorsement asociated'):
        endorsement = Endorsement(
            name='Healthy',
        )
        self.session.add(endorsement)
        self.session.flush()
        restriction = Restriction(
            name='Fit',
            endorsement=endorsement,
        )
        self.session.add(restriction)

        self.session.commit()

        expect(restriction.endorsement.name).to(equal('Healthy'))


with describe(DinersRestrictions) as self:
    with before.each:
        self.session = attach_session()

    with after.each:
        detach_session(self.session)

    with it('should have diner and restriction asociation'):
        diner = Diner(
            name='Jill',
        )
        self.session.add(diner)
        self.session.flush()
        restriction = Restriction(
            name='Vegan',
        )
        self.session.add(restriction)
        self.session.flush()
        diners_restrictions = DinersRestrictions(
            diner_id=diner.id,
            restriction_id=restriction.id,
        )
        self.session.add(diners_restrictions)
        self.session.commit()

        expect(diners_restrictions.diner.name).to(equal('Jill'))
        expect(diners_restrictions.restriction.name).to(equal('Vegan'))

    with it('should get diners restrictions by diners'):
        diner = Diner(
            name='Jack',
        )
        self.session.add(diner)
        self.session.flush()
        restriction = Restriction(
            name='Fit',
        )
        self.session.add(restriction)
        self.session.flush()
        diners_restrictions = DinersRestrictions(
            diner_id=diner.id,
            restriction_id=restriction.id,
        )
        self.session.add(diners_restrictions)
        self.session.commit()

        diners_restrictions = DinersRestrictions.get_all_by_diners(session=self.session, diners=[diner])

        for diner_restriction in diners_restrictions:
            expect(diner_restriction.restriction).to(equal(restriction))


with describe(Restaurant) as self:
    with before.all:
        self.session = attach_session()

    with after.all:
        detach_session(self.session)

    with it('should have name'):
        restaurant = Diner(
            name='Rosettta',
        )
        self.session.add(restaurant)
        self.session.commit()

        expect(restaurant.name).to(equal('Rosettta'))

with describe(Endorsement) as self:
    with before.all:
        self.session = attach_session()

    with after.all:
        detach_session(self.session)

    with it('should have name'):
        endorsement = Endorsement(
            name='Vegan-Friendly',
        )
        self.session.add(endorsement)
        self.session.commit()

        expect(endorsement.name).to(equal('Vegan-Friendly'))


with describe(RestaurantsEndorsements) as self:
    with before.all:
        self.session = attach_session()

    with after.all:
        detach_session(self.session)

    with it('should have restaurant and endorsement asociation'):
        restaurant = Restaurant(
            name='Rosettta',
        )
        self.session.add(restaurant)
        self.session.flush()
        endorsement = Endorsement(
            name='Vegan-Friendly',
        )
        self.session.add(endorsement)
        self.session.flush()
        restaurants_endorsements = RestaurantsEndorsements(
            restaurant_id=restaurant.id,
            endorsement_id=endorsement.id,
        )
        self.session.add(restaurants_endorsements)
        self.session.commit()

        expect(restaurants_endorsements.restaurant.name).to(equal('Rosettta'))
        expect(restaurants_endorsements.endorsement.name).to(equal('Vegan-Friendly'))


with describe(Table):
    with before.each:
        self.session = attach_session()

    with after.each:
        detach_session(self.session)

    with it('shuould have capacity'):
        restaurant = Restaurant(
            name='Rosettta',
        )
        self.session.add(restaurant)
        self.session.flush()
        table = Table(
            restaurant_id=restaurant.id,
            capacity=2,
            available_at=datetime.now(),
        )
        self.session.add(table)
        self.session.commit()

        expect(table.capacity).to(equal(2))

    with it('should have a restaurant associated'):
        restaurant = Restaurant(
            name='Anonimo',
        )
        self.session.add(restaurant)
        self.session.flush()
        table = Table(
            restaurant_id=restaurant.id,
            capacity=2,
            available_at=datetime.now(),
        )
        self.session.add(table)
        self.session.commit()

        expect(table.restaurant.name).to(equal('Anonimo'))

    with it('should have a available dates'):
        now = datetime.now()
        restaurant = Restaurant(
            name='Parnita',
        )
        self.session.add(restaurant)
        self.session.flush()
        table = Table(
            restaurant_id=restaurant.id,
            capacity=2,
            available_at=now,
        )
        self.session.add(table)
        self.session.commit()

        expect(table.available_at).to(equal(now))

    with it('should get available restaurant tables'):
        now = datetime.now()
        diner, vegan_endorsement, vegan_restriction = create_vegan_diner(self.session, 'Jill')
        diner_two, healthy_endorsement, fit_restriction = create_healthy_diner(self.session, 'Jack')
        lactose_restriction = add_extra_restriction_to_diner(self.session, diner, healthy_endorsement)
        table = create_vegan_healthy_restaurant(self.session, 2)

        tables = Table.get_available_restaurant_tables_by_capacity(
            self.session, now, [vegan_restriction, fit_restriction, lactose_restriction],
        )

        expect(tables).to(contain(table))

    with it('should not find any table when diners are more than capacity'):
        now = datetime.now()
        diner, vegan_endorsement, vegan_restriction = create_vegan_diner(self.session, 'Jill')
        diner_two, healthy_endorsement, fit_restriction = create_healthy_diner(self.session, 'Jack')
        lactose_restriction = add_extra_restriction_to_diner(self.session, diner, healthy_endorsement)
        table = create_vegan_healthy_restaurant(self.session, 1)

        tables = Table.get_available_restaurant_tables_by_capacity(
            self.session, now, [vegan_restriction, fit_restriction, lactose_restriction],
        )

        expect(tables).to(be_empty)

    with it('should not find any table when restaurant has no empty schedules'):
        available_at = datetime.fromisoformat('2023-08-24T12:00:00')
        diner, vegan_endorsement, vegan_restriction = create_vegan_diner(self.session, 'Jill')
        diner_two, healthy_endorsement, fit_restriction = create_healthy_diner(self.session, 'Jack')
        lactose_restriction = add_extra_restriction_to_diner(self.session, diner, healthy_endorsement)
        table = create_vegan_healthy_restaurant(self.session, 4)

        tables = Table.get_available_restaurant_tables_by_capacity(
            self.session, available_at, [vegan_restriction, fit_restriction, lactose_restriction],
        )

        expect(tables).to(be_empty)

    with it('should not find any table when restrictions mismatch restaurant endorsements'):
        available_at = datetime.fromisoformat('2023-08-24T12:00:00')
        diner, kosher_endorsement, kosher_restriction = create_kosher_diner(self.session, 'Gonz')
        table = create_vegan_healthy_restaurant(self.session, 4)

        tables = Table.get_available_restaurant_tables_by_capacity(self.session, available_at, [kosher_restriction])

        expect(tables).to(be_empty)


with describe(Reservation):
    with before.each:
        self.session = attach_session()

    with after.each:
        detach_session(self.session)

    with it('shuould have table and diner asociation'):
        now = datetime.now()
        restaurant = Restaurant(
            name='Anonimo',
        )
        table = Table(
            capacity=2,
            restaurant=restaurant,
            available_at=now,
        )

        self.session.add(table)
        self.session.flush()
        diner = Diner(
            name='Jill',
        )
        self.session.add(diner)
        self.session.flush()
        reservation = Reservation(
            diner_id=diner.id,
            table_id=table.id,
            booked_at=now,
        )
        self.session.add(reservation)
        self.session.commit()

        expect(reservation.diner.name).to(equal('Jill'))
        expect(reservation.table.capacity).to(equal(2))

    with it('should create reservation from diners_id and table_id using timestamp'):
        now = datetime.now()
        healthy_diner, *_ = create_healthy_diner(self.session, 'Gonz')  # noqa: WPS472
        table = create_vegan_healthy_restaurant(self.session, 4)

        reservation = Reservation.create_reservation(
            self.session,
            table=table,
            diner=healthy_diner,
            booked_at=now,
        )

        expect(reservation.diner.name).to(equal('Gonz'))
        expect(reservation.booked_at).to(equal(now))
        expect(reservation.table).to(equal(table))

    with it('should check for existing reservations'):
        healthy_diner, *_ = create_healthy_diner(self.session, 'Gonz')  # noqa: WPS472
        vegan_diner, *_ = create_vegan_diner(self.session, 'Jill')  # noqa: WPS472
        table = create_vegan_healthy_restaurant(self.session, 2)
        diners = [healthy_diner, vegan_diner]

        reservation = Reservation.create_reservation(
            self.session,
            table=table,
            diner=healthy_diner,
            booked_at=table.available_at,
        )

        booked_reservations = Reservation.verify_reservations(
            self.session,
            diners=diners,
        )

        expect(booked_reservations[0]).to(equal(reservation))

    with it('should delete reservations'):
        healthy_diner, *_ = create_healthy_diner(self.session, 'Gonz')  # noqa: WPS472
        vegan_diner, *_ = create_vegan_diner(self.session, 'Jill')  # noqa: WPS472
        table = create_vegan_healthy_restaurant(self.session, 2)
        diners = [healthy_diner, vegan_diner]

        reservation = Reservation.create_reservation(
            self.session,
            table=table,
            diner=healthy_diner,
            booked_at=table.available_at,
        )

        Reservation.delete_reservation(self.session, reservation.id)

        reervation = self.session.query(Reservation).get(reservation.id)

        expect(reervation).to(be_none)
