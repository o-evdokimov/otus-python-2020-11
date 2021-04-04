"""empty message

Revision ID: 1f4e86f4c583
Revises: 
Create Date: 2021-04-03 02:18:39.065155

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f4e86f4c583'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('device',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('state', sa.String(), nullable=False),
    sa.Column('ip_address', sa.String(), nullable=True),
    sa.Column('hardware_model', sa.String(), nullable=True),
    sa.Column('network_role', sa.String(), nullable=True),
    sa.Column('org_unit', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('device')
    # ### end Alembic commands ###
