from postgres_workers.query_maker import QueryMaker
from psycopg_pool import AsyncConnectionPool


class UserDataWorker(QueryMaker):
    def __init__(self, pool: AsyncConnectionPool = None,
                 table_name='Users',
                 cols_names=('name',
                             'age',
                             'time_created',
                             'gender',
                             'last_name',
                             'ip',
                             'city',
                             'premium',
                             'birth_day',
                             'balance')):
        super().__init__(pool=pool, table_name=table_name, cols_names=cols_names)
