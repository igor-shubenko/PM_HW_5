import psycopg

connection_string = "host=localhost port=5432 dbname=pm_db connect_timeout=10 user=pm_user password=12131415"

with psycopg.connect(connection_string) as conn:
    with conn.cursor() as cursor:
        # cursor.execute("""
        #             CREATE TABLE users (
        #                 id serial PRIMARY KEY,
        #                 name text)
        #             """)
        # cursor.execute("INSERT INTO users(name) VALUES(%s)", (None,))
        # cursor.execute("Insert into events(type, name, event_date) values(%s, %s, %s)", ('ttt', 'nnn', 12343))
        # cursor.execute("Insert into bets(date_created, userId, eventId) VALUES(%s, %s, %s)", (12345, 1, 1))
        res = cursor.execute("Select * from users")
        print(len(res.fetchall()))
        res2 = cursor.execute("Select * from events")
        print(res2.fetchall())
        res3 = cursor.execute("Select * from bets")
        print(res3.fetchall())




# if __name__ == '__main__':
#     pass
