"""add content column to posts table

Revision ID: e4a630d9d4d6
Revises: c7822140272a
Create Date: 2023-07-16 11:10:52.961577

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4a630d9d4d6'
down_revision = 'c7822140272a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column('posts', 'content')
