from postgres_workers.main_worker import MainDatabaseWorker


class UserDataWorker(MainDatabaseWorker):
    def create_user_record(self, data: dict) -> dict:
        query = "INSERT INTO Users(name, age, time_created, gender, last_name, " \
                 "ip, city, premium, birth_day, balance) " \
                "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        values = tuple(data.values())

        return self._create_record(query, values)

    def read_user_record(self, idn: str) -> list:
        if idn == 'all':
            query = "SELECT * FROM Users ORDER BY id;"
        elif idn.isdigit():
            query = f"SELECT * FROM Users WHERE id={idn};"
        else:
            return {"Error":"Wrong identificator"}
        return self._read_record(query)

    def update_user_record(self, idn: int, data: dict) -> dict:
        data = {k: v for k, v in data.items() if v is not None}     #remove default None values after validation

        query_start = "UPDATE Users SET "
        temp_strings = []
        for k, v in data.items():
            if type(v) is str:
                temp_string = f"{k}='{v}'"
            else:
                temp_string = f"{k}={v}"
            temp_strings.append(temp_string)
        query = query_start + ', '.join(temp_strings) + f' WHERE id={idn};'

        return self._update_record(query)


    def delete_user_record(self, idn: str) -> dict:
        if idn == 'all':
            query = "TRUNCATE Users CASCADE;"
        elif idn.isdigit():
            query = f"DELETE FROM Users WHERE id={idn};"
        else:
            return {"Error":"Wrong identificator"}
        return self._delete_record(query)


