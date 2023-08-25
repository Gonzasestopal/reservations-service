
from expects import equal, expect
from mamba import describe, it

from app.helpers import build_reservation_url

with describe(build_reservation_url):
    with it('should build api url with params'):
        table_id = 1
        diners_ids = [1, 2, 3, 4]
        qs_params = {
            'table_id': table_id,
            'diners': diners_ids,
        }

        url = build_reservation_url(table_id, diners_ids, 'dominio')

        expect(url).to(equal('dominio?table_id=1&diners=1&diners=2&diners=3&diners=4'))
