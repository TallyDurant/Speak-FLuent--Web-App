"""empty message

Revision ID: 0092fca0b4fd
Revises: 7dfa3bd93f58
Create Date: 2020-10-16 23:48:32.761654

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0092fca0b4fd'
down_revision = '7dfa3bd93f58'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('confirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'confirmed')
    # ### end Alembic commands ###
