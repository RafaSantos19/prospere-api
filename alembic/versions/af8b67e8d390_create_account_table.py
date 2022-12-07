"""create account table

Revision ID: af8b67e8d390
Revises: ""
Create Date: 2022-11-15 21:37:30.891356

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af8b67e8d390'
down_revision = ''
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=200), nullable=False),
    sa.Column('password', sa.String(length=512), nullable=False),
    sa.Column('xp', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('levels',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('difficult', sa.String(length=260), nullable=False),
    sa.Column('theme', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=260), nullable=False),
    sa.Column('points', sa.Integer, nullable=False),
    sa.Column('level', sa.Integer, nullable=False),
    sa.ForeignKeyConstraint(['level'], ['levels.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('answers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=260), nullable=False),
    sa.Column('question', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['question'], ['questions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

def downgrade() -> None:
    pass
