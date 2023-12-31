"""add active field to products and restaurants

Revision ID: b71259fd0a46
Revises: 8661827bab9a
Create Date: 2023-10-28 17:38:02.023557

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b71259fd0a46'
down_revision: Union[str, None] = '8661827bab9a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('active', sa.Boolean(), nullable=False, default=True, server_default="True"))
    op.add_column('restaurants', sa.Column('active', sa.Boolean(), nullable=False, default=True, server_default="True"))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('restaurants', 'active')
    op.drop_column('products', 'active')
    # ### end Alembic commands ###
