from datetime import datetime

from database.models import (
    Diner,
    DinersRestrictions,
    Endorsement,
    Restaurant,
    RestaurantsEndorsements,
    Restriction,
    Table,
)


def create_vegan_diner(session, diner_name):
    diner = Diner(
        name=diner_name,
    )
    session.add(diner)
    endorsement = Endorsement(
        name='Vegan-Friendly',
    )
    restriction = Restriction(
        name='Vegan',
        endorsement=endorsement,
    )
    session.add(restriction)
    diner_restriction = DinersRestrictions(
        diner=diner,
        restriction=restriction,
    )
    session.add(diner_restriction)
    session.commit()
    return diner, endorsement, diner_restriction


def create_healthy_diner(session, diner_name):
    diner = Diner(
        name=diner_name,
    )
    session.add(diner)
    endorsement = Endorsement(
        name='Healthy',
    )
    restriction = Restriction(
        name='Fit',
        endorsement=endorsement,
    )
    session.add(restriction)
    diner_restriction = DinersRestrictions(
        diner=diner,
        restriction=restriction,
    )
    session.add(diner_restriction)
    session.commit()
    return diner, endorsement, diner_restriction


def create_kosher_diner(session, diner_name):
    diner = Diner(
        name=diner_name,
    )
    session.add(diner)
    endorsement = Endorsement(
        name='Kosher-Certified',
    )
    restriction = Restriction(
        name='Kosher',
        endorsement=endorsement,
    )
    session.add(restriction)
    diner_restriction = DinersRestrictions(
        diner=diner,
        restriction=restriction,
    )
    session.add(diner_restriction)
    session.commit()
    return diner, endorsement, diner_restriction


def add_extra_restriction_to_diner(session, diner, endorsement):
    restriction = Restriction(
        name='Lactose',
        endorsement=endorsement,
    )
    session.add(restriction)
    diner_with_fit_restriction = DinersRestrictions(
        diner=diner,
        restriction=restriction,
    )
    session.add(diner_with_fit_restriction)
    session.commit()
    return diner_with_fit_restriction


def create_vegan_healthy_restaurant(session, capacity):
    healthy_endorsement = session.query(Endorsement).filter_by(name='Healthy').first()
    if not healthy_endorsement:
        healthy_endorsement = Endorsement(
            name='Healthy',
        )
        session.add(healthy_endorsement)
    vegan_endorsement = session.query(Endorsement).filter_by(name='Vegan').first()
    if not vegan_endorsement:
        vegan_endorsement = Endorsement(
            name='Vegan',
        )
        session.add(vegan_endorsement)
    restaurant = Restaurant(
        name='Parnita',
    )
    session.add(restaurant)
    restaurants_endorsement = RestaurantsEndorsements(
        restaurant=restaurant,
        endorsement=healthy_endorsement,
    )
    session.add(restaurants_endorsement)
    restaurants_endorsement_two = RestaurantsEndorsements(
        restaurant=restaurant,
        endorsement=vegan_endorsement,
    )
    session.add(restaurants_endorsement_two)
    table = Table(
        restaurant=restaurant,
        capacity=capacity,
        available_at=datetime.now(),
    )
    session.add(table)
    session.commit()
    return table
