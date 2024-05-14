"""empty message

Revision ID: 70c4e590f15d
Revises: d9a202cc61c5
Create Date: 2024-05-14 04:42:26.663988

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '70c4e590f15d'
down_revision: Union[str, None] = 'd9a202cc61c5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
