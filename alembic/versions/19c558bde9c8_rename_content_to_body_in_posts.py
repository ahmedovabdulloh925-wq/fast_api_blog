"""rename_content_to_body_in_posts

Revision ID: 19c558bde9c8
Revises: 4efe24d09eb2
Create Date: 2026-10-07 09:40:08.627213

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '19c558bde9c8'
down_revision: Union[str, Sequence[str], None] = '4efe24d09eb2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        'posts',
        'content',      # Eski nom
        new_column_name='body'   # Yangi nom
    )

def downgrade() -> None:
    op.alter_column(
        'posts',
        'body',
        new_column_name='content'
    )
