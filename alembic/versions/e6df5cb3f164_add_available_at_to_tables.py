"""Add available at to tables

Revision ID: e6df5cb3f164
Revises: f08ae659fe48
Create Date: 2023-08-24 15:46:04.722141

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e6df5cb3f164'
down_revision: Union[str, None] = 'f08ae659fe48'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tables', sa.Column('available_at', sa.Time(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tables', 'available_at')
    # ### end Alembic commands ###