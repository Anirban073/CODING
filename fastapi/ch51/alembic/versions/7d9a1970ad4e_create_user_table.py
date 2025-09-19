"""create user table

Revision ID: 7d9a1970ad4e
Revises: 
Create Date: 2025-09-17 19:54:13.598248

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7d9a1970ad4e'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.INTEGER, primary_key=True),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("email", sa.String, nullable=False),
    )


def downgrade() -> None:
    op.drop_table('users')
 