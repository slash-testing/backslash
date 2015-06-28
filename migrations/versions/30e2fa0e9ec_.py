"""empty message

Revision ID: 30e2fa0e9ec
Revises: 44becdc6831
Create Date: 2015-06-28 22:28:21.475146

"""

# revision identifiers, used by Alembic.
revision = '30e2fa0e9ec'
down_revision = '44becdc6831'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('test_information', sa.Column('name', sa.String(length=256), nullable=False))
    op.alter_column('test_information', 'file_name',
               existing_type=sa.VARCHAR(length=1024),
               nullable=True)
    op.create_index(op.f('ix_test_information_name'), 'test_information', ['name'], unique=False)
    op.drop_index('ix_test_information_function_name', table_name='test_information')
    op.drop_column('test_information', 'function_name')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('test_information', sa.Column('function_name', sa.VARCHAR(length=256), autoincrement=False, nullable=False))
    op.create_index('ix_test_information_function_name', 'test_information', ['function_name'], unique=False)
    op.drop_index(op.f('ix_test_information_name'), table_name='test_information')
    op.alter_column('test_information', 'file_name',
               existing_type=sa.VARCHAR(length=1024),
               nullable=False)
    op.drop_column('test_information', 'name')
    ### end Alembic commands ###
