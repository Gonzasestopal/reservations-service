from database.config import db_session
from database.repositories import TableRepository


def get_restaurants(available_at, diners, repository=TableRepository):
    with db_session() as session:
        repository = repository(session=session)
        tables = repository.get_available_restaurant_tables_by_capacity(
            available_at=available_at,
            capacity=len(diners),
        )

    return tables
