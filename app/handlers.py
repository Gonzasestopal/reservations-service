from database.config import db_session
from database.repositories import (DinerRepository,
                                   DinersRestrictionsRepository,
                                   TableRepository)


def get_restaurants(
        available_at,
        diners_name,
        table_repository_cls=TableRepository,
        diners_restrictions_repository_cls=DinersRestrictionsRepository,
        diner_repository_cls=DinerRepository,
    ):
    with db_session() as session:
        diner_repository = diner_repository_cls(session=session)
        diners = diner_repository.get_all_by_name(diners_name=diners_name)

        diners_restrictions_repository = diners_restrictions_repository_cls(session=session)
        diners_restrictions = diners_restrictions_repository.get_all_by_diners(
            diners=diners,
        )

        table_repository = table_repository_cls(session=session)
        tables = table_repository.get_available_restaurant_tables_by_capacity(
            available_at=available_at,
            diners_restrictions=diners_restrictions,
        )

    return tables
