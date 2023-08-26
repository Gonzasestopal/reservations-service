from datetime import datetime
from typing import List

from fastapi import APIRouter, Query, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.errors import ExistingBookingError

from app.handlers import generate_reservation as create_reservation_handler
from app.handlers import get_restaurants as get_restaurant_handler
from domain.models import Table as DomainTable

restaurants_router = APIRouter(
    prefix='/restaurants',
    tags=['restaurants'],
)


@restaurants_router.get('', response_model=DomainTable)
async def get_restaurants(available_at: datetime, diners: List[str] = Query(None, alias='diners')):  # noqa: B008, WPS404, E501
    restaurants = get_restaurant_handler(available_at, diners)
    return JSONResponse(jsonable_encoder(restaurants))


reservations_router = APIRouter(
    prefix='/reservations',
    tags=['reservations'],
)


@reservations_router.get('')
async def generate_reservation(table_id: int, diners_id: List[str] = Query(None, alias='diners')):   # noqa: B008, WPS404, E501
    try:
        reservations = create_reservation_handler(table_id=table_id, diners_id=diners_id)
    except ExistingBookingError:
        raise HTTPException(status_code=403, detail='Already booked')
    return JSONResponse(jsonable_encoder(reservations))


@reservations_router.delete('/')
async def remove_reservations():
    return {'message': 'Hello World'}
