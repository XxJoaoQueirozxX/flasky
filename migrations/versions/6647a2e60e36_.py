"""empty message

Revision ID: 6647a2e60e36
Revises: f7bf4ca645fe
Create Date: 2020-12-01 19:04:10.569442

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6647a2e60e36'
down_revision = 'f7bf4ca645fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    # ### end Alembic commands ###