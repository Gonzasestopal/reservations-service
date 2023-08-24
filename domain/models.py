from datetime import datetime

from pydantic import BaseModel


class Restaurant(BaseModel):
    id: int
    name: str


class Table(BaseModel):
    id: int
    capacity: int
    available_at: datetime
    restaurant: Restaurant
