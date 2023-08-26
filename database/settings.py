"""Settings from environment."""

import os

DB_NAME = os.getenv('POSTGRES_NAME')
DB_HOST = os.getenv('POSTGRES_HOST')
DB_USER = os.getenv('POSTGRES_USER')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_PORT = os.getenv('POSTGRES_PORT')
