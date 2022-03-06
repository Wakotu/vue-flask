"""empty message

Revision ID: 5fd158d52dad
Revises: 5834a5885acc
Create Date: 2022-02-27 16:07:12.972605

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5fd158d52dad'
down_revision = '5834a5885acc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('hash_pwd', sa.String(length=256), nullable=False))
    op.drop_column('users', 'pwd')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pwd', mysql.VARCHAR(collation='utf8_bin', length=20), nullable=False))
    op.drop_column('users', 'hash_pwd')
    # ### end Alembic commands ###
