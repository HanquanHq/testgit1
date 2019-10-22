"""ceshi

Revision ID: 38c88b3c2f6d
Revises: 2bddb1382e90
Create Date: 2019-10-09 09:53:14.551000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '38c88b3c2f6d'
down_revision = '2bddb1382e90'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('food', sa.Column('addcol1', sa.String(length=64), nullable=True))
    op.drop_column('food', 'addcol2')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('food', sa.Column('addcol2', mysql.VARCHAR(length=64), nullable=True))
    op.drop_column('food', 'addcol1')
    # ### end Alembic commands ###
