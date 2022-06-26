"""empty message

Revision ID: 09b535a6b039
Revises: 5844a63ac475
Create Date: 2022-06-26 23:11:03.912114

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09b535a6b039'
down_revision = '5844a63ac475'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todo', sa.Column('body', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todo', 'body')
    # ### end Alembic commands ###
