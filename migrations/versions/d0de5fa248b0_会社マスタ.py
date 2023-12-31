"""会社マスタ

Revision ID: d0de5fa248b0
Revises: ba17a32f2787
Create Date: 2023-07-08 00:17:05.773472

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0de5fa248b0'
down_revision = 'ba17a32f2787'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('industry',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('occupation',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tag',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('company',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('industry_id', sa.Integer(), nullable=True),
    sa.Column('occupation_id', sa.Integer(), nullable=True),
    sa.Column('work_location', sa.String(length=128), nullable=True),
    sa.Column('job_role', sa.Text(), nullable=True),
    sa.Column('ideal', sa.String(length=128), nullable=True),
    sa.Column('anuual_income', sa.Integer(), nullable=True),
    sa.Column('monthly_income', sa.Integer(), nullable=True),
    sa.Column('url', sa.String(length=128), nullable=True),
    sa.Column('capital', sa.Integer(), nullable=True),
    sa.Column('established', sa.String(length=64), nullable=True),
    sa.Column('employees', sa.Integer(), nullable=True),
    sa.Column('head_office', sa.String(length=128), nullable=True),
    sa.Column('representative', sa.String(length=64), nullable=True),
    sa.Column('business_content', sa.Text(), nullable=True),
    sa.Column('message', sa.Text(), nullable=True),
    sa.Column('is_published', sa.Boolean(), nullable=True),
    sa.Column('del_flg', sa.Boolean(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['industry_id'], ['industry.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['occupation_id'], ['occupation.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('condition',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('company_id')
    )
    op.create_table('image',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('manager',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('company_id')
    )
    op.create_table('relation',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tags',
    sa.Column('company_id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], ),
    sa.PrimaryKeyConstraint('company_id', 'tag_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tags')
    op.drop_table('relation')
    op.drop_table('manager')
    op.drop_table('image')
    op.drop_table('condition')
    op.drop_table('company')
    op.drop_table('tag')
    op.drop_table('occupation')
    op.drop_table('industry')
    # ### end Alembic commands ###
