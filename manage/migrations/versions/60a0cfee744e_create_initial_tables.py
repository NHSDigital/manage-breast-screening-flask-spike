"""Create initial tables

Revision ID: 60a0cfee744e
Revises: 
Create Date: 2025-04-15 11:31:15.401927

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '60a0cfee744e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clinics',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('setting', sa.String(length=255), nullable=False),
    sa.Column('starts_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('ends_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('location', sa.String(length=255), nullable=False),
    sa.Column('status', sa.Enum('SCHEDULED', 'IN_PROGRESS', 'CLOSED', 'CANCELLED', name='clinicstatus'), nullable=False),
    sa.Column('type', sa.Enum('ASSESSMENT', 'SCREENING', name='clinictype'), nullable=False),
    sa.Column('risk_type', sa.Enum('MIXED_RISK', 'ROUTINE_RISK', 'MOBILE', name='risktype'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('clinics')
    # ### end Alembic commands ###
