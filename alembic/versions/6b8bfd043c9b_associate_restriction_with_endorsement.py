"""Associate restriction with endorsement

Revision ID: 6b8bfd043c9b
Revises: 72a4db0a082e
Create Date: 2023-08-24 17:49:14.889237

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6b8bfd043c9b'
down_revision: Union[str, None] = '72a4db0a082e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###