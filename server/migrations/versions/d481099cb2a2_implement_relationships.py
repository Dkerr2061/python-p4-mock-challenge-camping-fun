"""implement relationships

Revision ID: d481099cb2a2
Revises: ba0b933159c4
Create Date: 2024-04-09 14:17:32.618992

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd481099cb2a2'
down_revision = 'ba0b933159c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('signups', sa.Column('activity_id', sa.Integer(), nullable=True))
    op.add_column('signups', sa.Column('camper_id', sa.Integer(), nullable=True))
    op.create_foreign_key(op.f('fk_signups_activity_id_activities'), 'signups', 'activities', ['activity_id'], ['id'])
    op.create_foreign_key(op.f('fk_signups_camper_id_campers'), 'signups', 'campers', ['camper_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_signups_camper_id_campers'), 'signups', type_='foreignkey')
    op.drop_constraint(op.f('fk_signups_activity_id_activities'), 'signups', type_='foreignkey')
    op.drop_column('signups', 'camper_id')
    op.drop_column('signups', 'activity_id')
    # ### end Alembic commands ###