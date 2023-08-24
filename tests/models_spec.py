"""Models tests."""

from expects import equal, expect
from mamba import after, before, describe, it

from database.models import (Diner, DinersRestrictions, Endorsement,
                             Reservation, Restaurant, RestaurantsEndorsements,
                             Restriction, Table)
from tests.session import attach_session, detach_session

with describe(Diner) as self:
    with before.all:
        self.session = attach_session()

    with after.all:
        detach_session(self.session)

    with it('should have name'):
        diner = Diner(
            name='Jill',
        )
        self.session.add(diner)
        self.session.commit()

        expect(diner.name).to(equal('Jill'))

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


with describe(DinersRestrictions) as self:
    with before.all:
        self.session = attach_session()

    with after.all:
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
    with before.all:
        self.session = attach_session()

    with after.all:
        detach_session(self.session)

    with it('shuould have capacity'):
        table = Table(capacity=2)
        self.session.add(table)
        self.session.commit()

        expect(table.capacity).to(equal(2))


with describe(Reservation):
    with before.all:
        self.session = attach_session()

    with after.all:
        detach_session(self.session)

    with it('shuould have table and diner asociation'):
        table = Table(capacity=2)
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
        )
        self.session.add(reservation)
        self.session.commit()

        expect(reservation.diner.name).to(equal('Jill'))
        expect(reservation.table.capacity).to(equal(2))
