"""会社２

Revision ID: 92acc1c9ecca
Revises: d0de5fa248b0
Create Date: 2023-07-08 22:26:00.556824

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92acc1c9ecca'
down_revision = 'd0de5fa248b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('manager')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('manager',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=128), nullable=True),
    sa.Column('company_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('company_id')
    )
    # ### end Alembic commands ###
