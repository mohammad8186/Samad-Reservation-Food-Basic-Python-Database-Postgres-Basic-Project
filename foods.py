class Food:
    def __init__(self, record):
        self.record = record
        self.id = record[0]
        self.name = record[1]
        self.date = record[2]
        self.price = record[3]
        self.inventory = record[4]

    def __str__(self):
        record = list(self.record)
        record[2] = self.date.strftime('%Y-%m-%d %H:%M:%S')
        return str(tuple(record))


class Foods:
    def __init__(self, database):
        self.database = database
        self.create_table()

    def create_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS Foods (
                ID SERIAL PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                date TIMESTAMP NOT NULL,
                price INT NOT NULL,
                inventory INT NOT NULL
            )
        """

        self.database.start_transaction()
        self.database.execute(query)
        self.database.commit()

    def get_all(self) -> [Food]:
        query = """
            SELECT * FROM Foods
        """

        records = self.database.fetch_all(query)
        if records is not None:
            return [Food(record) for record in records]

    def get(self, food_id) -> Food:
        query = f"""
            SELECT * FROM Foods
            WHERE id = {food_id} 
        """

        record = self.database.fetch_one(query)
        if record is not None:
            return Food(record)

    def get_by_name_date(self, name, date) -> Food:
        query = f"""
            SELECT * FROM Foods
            WHERE name = '{name}' and date='{date}'
        """

        record = self.database.fetch_one(query)
        if record is not None:
            return Food(record)

    def delete(self, food_id):
        query = f"""
            DELETE FROM Foods
            WHERE id = {food_id}
        """

        self.database.execute(query)

    def insert(self, name, date, price, inventory):
        query = f"""
            INSERT INTO Foods (name, date, price, inventory)
            VALUES ('{name}', '{date}', {price}, {inventory})
            RETURNING *
        """

        food = self.get_by_name_date(name, date)
        if food is not None:
            print(food)
            raise Exception("This food is already inserted.")

        record = self.database.fetch_one(query)
        if record is not None:
            return Food(record)

    def update_inventory(self, food_id, inventory):
        query = f"""
            UPDATE Foods
            SET inventory = {inventory}
            WHERE id = {food_id}
            RETURNING *
        """

        record = self.database.fetch_one(query)
        if record is not None:
            return Food(record)
