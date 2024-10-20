"""empty message

Revision ID: 664123fbb441
Revises: 
Create Date: 2024-10-17 21:02:31.650336

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '664123fbb441'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Questions',
    sa.Column('num', sa.Integer(), nullable=False),
    sa.Column('question', sa.String(length=1024), nullable=False),
    sa.Column('variants', sa.String(length=1024), nullable=False),
    sa.PrimaryKeyConstraint('num')
    )
    op.create_table('Rating',
    sa.Column('chat_id', sa.Integer(), nullable=False),
    sa.Column('tg_username', sa.String(length=255), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('chat_id')
    )
    op.create_table('UserData',
    sa.Column('chat_id', sa.Integer(), nullable=False),
    sa.Column('tg_username', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('chat_id')
    )
    op.create_table('test',
    sa.Column('chat_id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('chat_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('test')
    op.drop_table('UserData')
    op.drop_table('Rating')
    op.drop_table('Questions')
    # ### end Alembic commands ###
