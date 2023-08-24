from datetime import datetime
from typing import List

from fastapi import APIRouter, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from domain.models import Table as DomainTable

from .handlers import get_restaurants as get_restaurant_handler

restaurants_router = APIRouter(
    prefix='/restaurants',
    tags=['restaurants'],
)

@restaurants_router.get('', response_model=DomainTable)
async def get_restaurants(available_at: datetime, diners: List[str] = Query(None, alias='diners')):
    restaurants = get_restaurant_handler(available_at, diners)
    return JSONResponse(jsonable_encoder(restaurants))


reservations_router = APIRouter(
    prefix='/reservations',
    tags=['reservations'],
)

@reservations_router.post('/')
async def genreate_reservations():
    return {'message': 'Hello World'}


@reservations_router.delete('/')
async def remove_reservations():
    return {'message': 'Hello World'}
