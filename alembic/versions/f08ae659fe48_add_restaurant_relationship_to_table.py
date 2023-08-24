"""Add restaurant relationship to table

Revision ID: f08ae659fe48
Revises: 7dd3eacc9a14
Create Date: 2023-08-24 15:04:21.116944

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f08ae659fe48'
down_revision: Union[str, None] = '7dd3eacc9a14'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tables', sa.Column('restaurant_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_table_restaurant_id', 'tables', 'restaurants', ['restaurant_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fk_table_restaurant_id', 'tables', type_='foreignkey')
    op.drop_column('tables', 'restaurant_id')
    # ### end Alembic commands ###
