"""Create all tables

Revision ID: 306b63f34b5b
Revises: fc741cdf31e1
Create Date: 2021-03-04 13:19:48.112629

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '306b63f34b5b'
down_revision = 'fc741cdf31e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    op.drop_table('movies')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movies',
    sa.Column('imdbID', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('Title', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('Year', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('Type', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('Poster', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('created_at', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('Poster2', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('imdbID', name='movies_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('posts',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('movie_id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('author', sa.VARCHAR(length=32), server_default=sa.text("''::character varying"), autoincrement=False, nullable=False),
    sa.Column('title', sa.VARCHAR(length=255), server_default=sa.text("''::character varying"), autoincrement=False, nullable=False),
    sa.Column('text', sa.VARCHAR(length=255), server_default=sa.text("''::character varying"), autoincrement=False, nullable=False),
    sa.Column('created_at', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['movie_id'], ['movies.imdbID'], name='posts_movie_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='posts_pkey')
    )
    # ### end Alembic commands ###