"""initial

Revision ID: c8447996d0ce
Revises: 19c558bde9c8
Create Date: 2026-10-14 16:20:23.912954

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'c8447996d0ce'
down_revision: Union[str, Sequence[str], None] = '19c558bde9c8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass