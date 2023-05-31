"""empty message

Revision ID: b49edb6e5d56
Revises: 06872d9888ca
Create Date: 2023-05-24 20:02:06.652899

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b49edb6e5d56'
down_revision = '06872d9888ca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('investments', schema=None) as batch_op:
        batch_op.drop_constraint('investments_portfolio_id_fkey', type_='foreignkey')
        batch_op.drop_column('portfolio_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('investments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('portfolio_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('investments_portfolio_id_fkey', 'portfolios', ['portfolio_id'], ['id'])

    # ### end Alembic commands ###