"""Added columns to user

Revision ID: 541f61ab86ca
Revises: 1c697a5bd34f
Create Date: 2014-02-02 15:00:14.801202

"""

# revision identifiers, used by Alembic.
revision = '541f61ab86ca'
down_revision = '1c697a5bd34f'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bf_user', sa.Column('business_url', sa.Unicode(), nullable=True))
    op.add_column('bf_user', sa.Column('description', sa.Unicode(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('bf_user', 'description')
    op.drop_column('bf_user', 'business_url')
    ### end Alembic commands ###