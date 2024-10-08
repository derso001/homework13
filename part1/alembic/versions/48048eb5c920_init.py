"""Init

Revision ID: 48048eb5c920
Revises: 
Create Date: 2024-09-22 23:17:22.045539

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '48048eb5c920'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=250), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('crated_at', sa.DateTime(), nullable=True),
    sa.Column('avatar', sa.String(length=255), nullable=True),
    sa.Column('refresh_token', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('contact',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('phone_number', sa.String(), nullable=True),
    sa.Column('birthday', sa.Date(), nullable=True),
    sa.Column('additional_info', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_contact_email'), 'contact', ['email'], unique=True)
    op.create_index(op.f('ix_contact_first_name'), 'contact', ['first_name'], unique=False)
    op.create_index(op.f('ix_contact_id'), 'contact', ['id'], unique=False)
    op.create_index(op.f('ix_contact_last_name'), 'contact', ['last_name'], unique=False)
    op.create_index(op.f('ix_contact_phone_number'), 'contact', ['phone_number'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_contact_phone_number'), table_name='contact')
    op.drop_index(op.f('ix_contact_last_name'), table_name='contact')
    op.drop_index(op.f('ix_contact_id'), table_name='contact')
    op.drop_index(op.f('ix_contact_first_name'), table_name='contact')
    op.drop_index(op.f('ix_contact_email'), table_name='contact')
    op.drop_table('contact')
    op.drop_table('users')
    # ### end Alembic commands ###
