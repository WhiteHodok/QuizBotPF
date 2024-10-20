"""empty message

Revision ID: 41b90fc0a935
Revises: 6ea269883bbe
Create Date: 2024-10-17 21:22:33.868220

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '41b90fc0a935'
down_revision: Union[str, None] = '6ea269883bbe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('test')
    op.alter_column('Rating', 'tg_username',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('Rating', 'rating',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('UserData', 'tg_username',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('UserData', 'tg_username',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('Rating', 'rating',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('Rating', 'tg_username',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.create_table('test',
    sa.Column('chat_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('text', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('chat_id', name='test_pkey')
    )
    # ### end Alembic commands ###
