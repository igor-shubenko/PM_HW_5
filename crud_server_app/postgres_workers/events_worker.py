from postgres_workers.main_worker import MainDatabaseWorker


class EventsDataWorker(MainDatabaseWorker):
    def create_event_record(self, data: dict) -> dict:
        query = "INSERT INTO Events(type, name, event_date) VALUES(%s, %s, %s);"
        values = tuple(data.values())

        return self._create_record(query, values)

    def read_event_record(self, idn: str) -> list:
        if idn == 'all':
            query = 'SELECT * FROM Events ORDER BY id;'
        elif idn.isdigit():
            query = f'SELECT * FROM Events WHERE id={idn};'
        else:
            return {"Error":"Wrong identificator"}

        return self._read_record(query)

    def update_event_record(self, idn: int, data: dict) -> dict:
        data = {k: v for k, v in data.items() if v is not None}
        query_start = "UPDATE Events SET "
        temp_strings = []

        for k, v in data.items():
            if type(v) is str:
                temp_string = f"{k}='{v}'"
            else:
                temp_string = f"{k}={v}"
            temp_strings.append(temp_string)
        query = query_start + ', '.join(temp_strings) + f' WHERE id={idn};'

        return self._update_record(query)

    def delete_event_record(self, idn: str):
        if idn == 'all':
            query = 'TRUNCATE Events CASCADE;'
        elif idn.isdigit():
            query = f'DELETE FROM Events WHERE id={idn};'
        else:
            return {"Error":"Wrong identificator"}

        return self._delete_record(query)


