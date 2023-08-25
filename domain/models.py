from datetime import datetime

from pydantic import BaseModel


class Diner(BaseModel):
    id: int
    name: str


class Restaurant(BaseModel):
    id: int
    name: str


class Table(BaseModel):
    id: int
    capacity: int
    available_at: datetime
    restaurant: Restaurant


class Reservation(BaseModel):
    id: int
    booked_at: datetime
    diner: Diner
    table: Table
