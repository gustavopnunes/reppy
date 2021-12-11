"""removing states table

Revision ID: 6fa28c6227e4
Revises: b6a871638396
Create Date: 2021-12-10 19:12:39.661837

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6fa28c6227e4'
down_revision = 'b6a871638396'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('addresses', sa.Column('uf', sa.String(length=2), nullable=True))
    op.drop_constraint('addresses_uf_id_fkey', 'addresses', type_='foreignkey')
    op.drop_column('addresses', 'uf_id')
    op.drop_table('states')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('addresses', sa.Column('uf_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('addresses_uf_id_fkey', 'addresses', 'states', ['uf_id'], ['id'])
    op.drop_column('addresses', 'uf')
    op.create_table('states',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('uf', sa.VARCHAR(length=2), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='states_pkey')
    )
    # ### end Alembic commands ###