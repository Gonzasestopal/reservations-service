import urllib

from app.settings import API_BASE_URL

RESERVATIONS_API_URL = urllib.parse.urljoin(API_BASE_URL, 'reservations')


def build_reservation_url(table_id, diners_ids, reservations_api_base_url=None):
    if not reservations_api_base_url:
        reservations_api_base_url = RESERVATIONS_API_URL

    querystrings = {
        'table_id': table_id,
        'diners': diners_ids,
    }
    encoded_querystrings = urllib.parse.urlencode(querystrings, doseq=True)
    return reservations_api_base_url + '?' + encoded_querystrings
