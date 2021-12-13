"""empty message

Revision ID: eee5289eb9c1
Revises: 6fa28c6227e4
Create Date: 2021-12-13 11:11:09.337548

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eee5289eb9c1'
down_revision = '6fa28c6227e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('users_name_key', 'users', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('users_name_key', 'users', ['name'])
    # ### end Alembic commands ###
