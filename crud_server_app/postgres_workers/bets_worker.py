from postgres_workers.main_worker import MainDatabaseWorker


class BetsDataWorker(MainDatabaseWorker):
    def create_bet_record(self, data):
        query = "INSERT INTO Bets(date_created, userId, eventId) VALUES(%s, %s, %s);"
        values = tuple(data.values())

        return self._create_record(query, values)

    def read_bet_record(self, idn):
        if idn == 'all':
            query = "SELECT * FROM Bets ORDER BY id;"
        elif idn.isdigit():
            query = f"SELECT * FROM Bets WHERE id={idn};"
        else:
            return {"Error": "Wrong identificator"}

        return self._read_record(query)

    def update_bet_record(self, idn, data):
        data = {k: v for k, v in data.items() if v is not None}  # remove default None values after validation

        query_start = "UPDATE Bets SET "
        temp_strings = []
        for k, v in data.items():
            if type(v) is str:
                temp_string = f"{k}='{v}'"
            else:
                temp_string = f"{k}={v}"
            temp_strings.append(temp_string)
        query = query_start + ', '.join(temp_strings) + f' WHERE id={idn};'

        return self._update_record(query)

    def delete_bet_record(self, idn):
        if idn == 'all':
            query = "TRUNCATE Bets;"
        elif idn.isdigit():
            query = f"DELETE FROM Bets WHERE id={idn};"
        else:
            return {"Error": "Wrong identificator"}

        return self._delete_record(query)
