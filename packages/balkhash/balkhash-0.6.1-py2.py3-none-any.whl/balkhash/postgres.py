import logging
import datetime
from normality import slugify
from sqlalchemy import Column, DateTime, String, UniqueConstraint
from sqlalchemy import Table, MetaData
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import create_engine, select, distinct, func
from sqlalchemy.dialects import postgresql

from balkhash import settings
from balkhash.dataset import Dataset, Bulk

log = logging.getLogger(__name__)
# We have to cast null fragment values to "" to make the
# UniqueConstraint work
EMPTY = ''


class PostgresDataset(Dataset):

    def __init__(self, config):
        super(PostgresDataset, self).__init__(config)
        database_uri = config.get('database_uri', settings.DATABASE_URI)
        prefix = config.get('prefix', settings.DATABASE_PREFIX)
        name = '%s %s' % (prefix, self.name)
        name = slugify(name, sep='_')
        self.engine = create_engine(database_uri)
        meta = MetaData(self.engine)
        self.table = Table(name, meta,
            Column('id', String),  # noqa
            Column('fragment', String, nullable=False, default=EMPTY),
            Column('properties', postgresql.JSONB),
            Column('schema', String),
            Column('timestamp', DateTime, default=datetime.datetime.utcnow),
            UniqueConstraint('id', 'fragment'),
            extend_existing=True
        )
        self.table.create(bind=self.engine, checkfirst=True)

    def delete(self, entity_id=None, fragment=None):
        table = self.table
        statement = table.delete()
        if entity_id is not None:
            statement = statement.where(table.c.id == entity_id)
            if fragment is not None:
                statement = statement.where(table.c.fragment == fragment)
        self.engine.execute(statement)

    def put(self, entity, fragment=None):
        entity = self._entity_dict(entity)
        upsert_statement = insert(self.table).values(
            id=entity['id'],
            fragment=fragment or EMPTY,
            properties=entity['properties'],
            schema=entity['schema'],
        ).on_conflict_do_update(
            index_elements=['id', 'fragment'],
            set_=dict(
                properties=entity['properties'],
                schema=entity['schema'],
            )
        )
        return self.engine.execute(upsert_statement)

    def bulk(self, size=10000):
        return PostgresBulk(self, size)

    def close(self):
        self.engine.dispose()

    def fragments(self, entity_id=None, fragment=None):
        table = self.table
        statement = table.select()
        if entity_id is not None:
            statement = statement.where(table.c.id == entity_id)
            if fragment is not None:
                statement = statement.where(table.c.fragment == fragment)
        statement = statement.order_by(table.c.id)
        statement = statement.order_by(table.c.fragment)
        conn = self.engine.connect()
        conn = conn.execution_options(stream_results=True)
        entities = conn.execute(statement)
        for ent in entities:
            ent = dict(ent)
            ent.pop('timestamp', None)
            if ent['fragment'] == EMPTY:
                ent['fragment'] = None
            yield ent

    def __len__(self):
        q = select([func.count(distinct(self.table.c.id))])
        return self.engine.execute(q).scalar()

    def __repr__(self):
        return '<PostgresDataset(%r, %r)>' % (self.engine, self.table.name)


class PostgresBulk(Bulk):

    def flush(self):
        if not len(self.buffer):
            return
        values = [
            {
                'id': entity_id,
                'fragment': fragment or EMPTY,
                'properties': entity['properties'],
                'schema': entity['schema']
            } for (entity_id, fragment), entity in self.buffer.items()
        ]
        insert_statement = insert(self.dataset.table).values(values)
        upsert_statement = insert_statement.on_conflict_do_update(
            index_elements=['id', 'fragment'],
            set_=dict(
                properties=insert_statement.excluded.properties,
                schema=insert_statement.excluded.schema,
            )
        )
        self.dataset.engine.execute(upsert_statement)
