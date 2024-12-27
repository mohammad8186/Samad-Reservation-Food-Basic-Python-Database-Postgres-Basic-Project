from datetime import datetime


class Transaction:
    def __init__(self, record):
        self.record = record
        self.src_reservation_id = record[0]
        self.dst_reservation_id = record[1]
        self.date = record[2]

    def __str__(self):
        record = list(self.record)
        record[2] = self.date.strftime('%Y-%m-%d %H:%M:%S')
        return str(tuple(record))


class Transactions:
    def __init__(self, database):
        self.database = database
        self.create_table()

    def create_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS Transactions (
                SRCreservationID INT,
                DSTreservationID INT,
                date TIMESTAMP NOT NULL
            )
        """

        self.database.start_transaction()
        self.database.execute(query)
        self.database.commit()

    def get_all(self):
        query = """
            SELECT * FROM Transactions
        """

        records = self.database.fetch_all(query)
        if records is not None:
            return [Transaction(record) for record in records]

    def insert(self, src_reservation_id, dst_reservation_id):
        date = datetime.now()

        query = f"""
            INSERT INTO Transactions (SRCreservationID, DSTreservationID, date)
            VALUES ({src_reservation_id}, {dst_reservation_id}, '{date}')
            RETURNING *
        """

        record = self.database.fetch_one(query)
        if record is not None:
            return Transaction(record)
