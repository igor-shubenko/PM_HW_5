from postgres_workers.query_maker import QueryMaker
from psycopg_pool import AsyncConnectionPool

class EventsDataWorker(QueryMaker):
    def __init__(self, pool: AsyncConnectionPool = None,
                 table_name='Events',
                 cols_names=('type',
                             'name',
                             'event_date')):
        super().__init__(pool=pool, table_name=table_name, cols_names=cols_names)
