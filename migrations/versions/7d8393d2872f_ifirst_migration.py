"""ifirst migration

Revision ID: 7d8393d2872f
Revises: 
Create Date: 2019-10-07 11:11:22.417000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d8393d2872f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('food', sa.Column('addcol', sa.String(length=64), nullable=True))
    op.add_column('food', sa.Column('addcol1', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('food', 'addcol1')
    op.drop_column('food', 'addcol')
    # ### end Alembic commands ###
