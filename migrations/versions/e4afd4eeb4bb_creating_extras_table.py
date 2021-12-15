"""Creating Extras table

Revision ID: e4afd4eeb4bb
Revises: af2a617f4f73
Create Date: 2021-12-14 20:43:15.239241

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4afd4eeb4bb'
down_revision = 'af2a617f4f73'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('extras',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('animals_allowed', sa.Boolean(), nullable=False),
    sa.Column('parties_allowed', sa.Boolean(), nullable=False),
    sa.Column('wifi', sa.Boolean(), nullable=False),
    sa.Column('swiming_pool', sa.Boolean(), nullable=False),
    sa.Column('grill', sa.Boolean(), nullable=False),
    sa.Column('republic_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['republic_id'], ['republics.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('republic_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('extras')
    # ### end Alembic commands ###
