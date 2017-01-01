"""Add test index field

Revision ID: a728e6b3d880
Revises: 383eac3634aa
Create Date: 2017-01-01 13:19:36.747525

"""

# revision identifiers, used by Alembic.
revision = 'a728e6b3d880'
down_revision = '383eac3634aa'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('test', sa.Column('test_index', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('test', 'test_index')
    # ### end Alembic commands ###
