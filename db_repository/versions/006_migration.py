from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
monitor = Table('monitor', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('item_id', Integer, nullable=False),
    Column('item_name', String(length=128), default=ColumnDefault('')),
    Column('item_price', String(length=64), default=ColumnDefault('')),
    Column('user_price', String(length=64), nullable=False),
    Column('status', Boolean, nullable=False),
    Column('user_id', Integer),
    Column('mall_id', Integer, nullable=False),
    Column('note', String(length=128), default=ColumnDefault('')),
    Column('add_date', DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['monitor'].columns['user_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['monitor'].columns['user_id'].drop()
