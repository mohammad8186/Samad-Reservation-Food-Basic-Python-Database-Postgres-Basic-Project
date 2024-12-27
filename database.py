import psycopg2


class Database:
    def __init__(self):
        self.connection: psycopg2 = None
        self.cursor = None
        self.create_connection()

    def create_connection(self):
        try:
            self.connection = psycopg2.connect(
                database="postgres",
                user="postgres",
                password="09902048023M.sh",
                host="localhost",
                port="5432")

            print("Connected to PostgreSQL database!\n")

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL.", error)

    def close_connection(self):
        self.connection.close()
        print("\nConnection to PostgreSQL is closed!")

    def start_transaction(self):
        self.cursor = self.connection.cursor()

    def execute(self, query):
        self.cursor.execute(query)

    def fetch_one(self, query):
        self.cursor.execute(query)
        record = self.cursor.fetchone()
        return record

    def fetch_all(self, query):
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        return records

    def commit(self):
        self.connection.commit()
        self.cursor.close()
        self.cursor = None
