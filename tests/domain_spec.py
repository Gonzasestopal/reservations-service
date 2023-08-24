"""Models tests."""

from datetime import datetime

from expects import equal, expect, have_properties
from mamba import after, before, describe, it

from domain.models import Restaurant, Table

with describe(Table):
    with it('should have expected properties'):
        restaurant = Restaurant(
            id=1,
            name='Parnita',
        )
        table = Table(
            id=1,
            capacity=2,
            available_at=datetime.now(),
            restaurant=restaurant,
        )

        expect(table).to(have_properties('capacity', 'available_at', 'restaurant'))

with describe(Restaurant):
    with it('should have expected properties'):
        restaurant = Restaurant(
            id=1,
            name='Parnita',
        )
        expect(restaurant).to(have_properties('id', 'name'))
