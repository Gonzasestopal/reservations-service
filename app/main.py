"""App route resolver."""

import os

from fastapi import FastAPI
from mangum import Mangum

from app.routes import reservations_router, restaurants_router

stage = os.environ.get('STAGE', None)
openapi_prefix = f'/{stage}' if stage else '/'

# Here is the magic
app = FastAPI(openapi_prefix=openapi_prefix)

app.include_router(restaurants_router)
app.include_router(reservations_router)


@app.get('/')
async def root():
    return {'message': 'Hello World'}

handler = Mangum(app)  # noqa: WPS110
