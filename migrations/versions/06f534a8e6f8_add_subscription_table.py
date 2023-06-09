"""Add subscription table

Revision ID: 06f534a8e6f8
Revises: 1ebd8f45f5cc
Create Date: 2023-04-18 19:10:37.330102

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06f534a8e6f8'
down_revision = '1ebd8f45f5cc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subscription', sa.String(length=100), nullable=False),
    sa.Column('other', sa.String(length=50), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(length=20), nullable=False),
    sa.Column('frequency', sa.String(length=100), nullable=False),
    sa.Column('image_url', sa.String(length=100), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    # ### end Alembic commands ###
