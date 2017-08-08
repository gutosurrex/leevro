"""Initial

Revision ID: 39876672174b
Revises: None
Create Date: 2017-06-26 00:04:43.618307

"""

# revision identifiers, used by Alembic.
revision = '39876672174b'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=255), server_default='', nullable=False),
    sa.Column('reset_password_token', sa.String(length=100), server_default='', nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('confirmed_at', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Boolean(), server_default='0', nullable=False),
    sa.Column('first_name', sa.String(length=100), server_default='', nullable=False),
    sa.Column('last_name', sa.String(length=100), server_default='', nullable=False),
    sa.Column('string_property_01', sa.String(length=80), nullable=True),
    sa.Column('string_property_02', sa.String(length=80), nullable=True),
    sa.Column('string_property_03', sa.String(length=80), nullable=True),
    sa.Column('string_property_04', sa.String(length=80), nullable=True),
    sa.Column('string_property_05', sa.String(length=80), nullable=True),
    sa.Column('integer_property_01', sa.Integer(), nullable=True),
    sa.Column('integer_property_02', sa.Integer(), nullable=True),
    sa.Column('integer_property_03', sa.Integer(), nullable=True),
    sa.Column('integer_property_04', sa.Integer(), nullable=True),
    sa.Column('integer_property_05', sa.Integer(), nullable=True),
    sa.Column('integer_property_06', sa.Integer(), nullable=True),
    sa.Column('integer_property_07', sa.Integer(), nullable=True),
    sa.Column('integer_property_08', sa.Integer(), nullable=True),
    sa.Column('integer_property_09', sa.Integer(), nullable=True),
    sa.Column('integer_property_10', sa.Integer(), nullable=True),
    sa.Column('boolean_property_01', sa.Boolean(), nullable=True),
    sa.Column('boolean_property_02', sa.Boolean(), nullable=True),
    sa.Column('boolean_property_03', sa.Boolean(), nullable=True),
    sa.Column('boolean_property_04', sa.Boolean(), nullable=True),
    sa.Column('boolean_property_05', sa.Boolean(), nullable=True),
    sa.Column('boolean_property_06', sa.Boolean(), nullable=True),
    sa.Column('boolean_property_07', sa.Boolean(), nullable=True),
    sa.Column('boolean_property_08', sa.Boolean(), nullable=True),
    sa.Column('boolean_property_09', sa.Boolean(), nullable=True),
    sa.Column('boolean_property_10', sa.Boolean(), nullable=True),
    sa.Column('boolean_property_11', sa.Boolean(), nullable=True),
    sa.Column('boolean_property_12', sa.Boolean(), nullable=True),
    sa.Column('boolean_property_13', sa.Boolean(), nullable=True),
    sa.Column('boolean_property_14', sa.Boolean(), nullable=True),
    sa.Column('boolean_property_15', sa.Boolean(), nullable=True),
    sa.Column('boolean_property_16', sa.Boolean(), nullable=True),
    sa.Column('boolean_property_17', sa.Boolean(), nullable=True),
    sa.Column('boolean_property_18', sa.Boolean(), nullable=True),
    sa.Column('boolean_property_19', sa.Boolean(), nullable=True),
    sa.Column('boolean_property_20', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('branch',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('origin_id', sa.Integer(), nullable=True),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.Column('expires', sa.Boolean(), nullable=False),
    sa.Column('expiration', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['origin_id'], ['branch.id'], ),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('named_tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('thread',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.Unicode(length=80), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.Column('flag', sa.String(length=10), nullable=False),
    sa.Column('posted_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lineage', sa.String(length=200), nullable=True),
    sa.Column('thread_id', sa.Integer(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('content', sa.Unicode(length=2000), nullable=False),
    sa.Column('posted_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['thread_id'], ['thread.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('custom_tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('thread_id', sa.Integer(), nullable=True),
    sa.Column('named_tag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['named_tag_id'], ['named_tag.id'], ),
    sa.ForeignKeyConstraint(['thread_id'], ['thread.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('file_tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('thread_id', sa.Integer(), nullable=True),
    sa.Column('filename', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['thread_id'], ['thread.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('free_tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('thread_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.ForeignKeyConstraint(['thread_id'], ['thread.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('thread_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['thread_id'], ['thread.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('likes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment_id', sa.Integer(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['comment_id'], ['comment.id'], ),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('likes')
    op.drop_table('user_tag')
    op.drop_table('free_tag')
    op.drop_table('file_tag')
    op.drop_table('custom_tag')
    op.drop_table('comment')
    op.drop_table('thread')
    op.drop_table('named_tag')
    op.drop_table('branch')
    op.drop_table('project')
    op.drop_table('user')
    # ### end Alembic commands ###