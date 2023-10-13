import psycopg

class Connection():
    conn = None

    def __init__(self):
        try:
            self.conn = psycopg.connect("dbname=examen_03 user=pollito password=daniel12345 host=localhost port=5432")

        except psycopg.OperationalError as err:
            print(err)
            self.conn.close()


    def __def__(self):
            self.conn.close()