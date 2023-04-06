from postgres_workers.query_maker import QueryMaker
from psycopg_pool import AsyncConnectionPool


class BetsDataWorker(QueryMaker):
    def __init__(self, pool: AsyncConnectionPool = None,
                 table_name='Bets',
                 cols_names=('date_created',
                             'userId',
                             'eventId')):
        super().__init__(pool=pool, table_name=table_name, cols_names=cols_names)
