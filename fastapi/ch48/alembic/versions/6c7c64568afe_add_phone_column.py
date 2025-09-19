"""add phone column

Revision ID: 6c7c64568afe
Revises: 7d9a1970ad4e
Create Date: 2025-09-17 21:02:54.078516

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6c7c64568afe'
down_revision: Union[str, Sequence[str], None] = '7d9a1970ad4e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("phone", sa.String()))


def downgrade() -> None:
    op.drop_column("users", "phone")
