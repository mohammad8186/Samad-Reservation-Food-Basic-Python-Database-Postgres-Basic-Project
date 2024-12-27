from datetime import datetime

from students import Students
from foods import Foods
from transactions import Transactions


class Reservation:
    def __init__(self, record):
        self.record = record
        self.id = record[0]
        self.student_id = record[1]
        self.food_id = record[2]

    def __str__(self):
        return str(self.record)


class Reservations:
    def __init__(self, database, students: Students, foods: Foods, transactions: Transactions):
        self.database = database
        self.create_table()
        self.students = students
        self.foods = foods
        self.transactions = transactions

    def create_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS Reservations (
                ID SERIAL PRIMARY KEY,
                studentID INT NOT NULL,
                foodID INT NOT NULL
            )
        """

        self.database.start_transaction()
        self.database.execute(query)
        self.database.commit()

    def get_all(self) -> [Reservation]:
        query = """
            SELECT * FROM Reservations
        """

        records = self.database.fetch_all(query)
        if records is not None:
            return [Reservation(record) for record in records]

    def get_reservation(self, student_id, food_id) -> Reservation:
        query = f"""
            SELECT * FROM Reservations
            WHERE studentid={student_id} AND foodid={food_id}
        """

        record = self.database.fetch_one(query)
        if record is not None:
            return Reservation(record)

    def __delete(self, reservation_id):
        query = f"""
            DELETE FROM Reservations
            WHERE id = {reservation_id}
        """

        self.database.execute(query)

    def __insert(self, student_id, food_id):
        query = f"""
            INSERT INTO Reservations (studentID, foodID)
            VALUES ({student_id}, {food_id})
            RETURNING *;
        """

        record = self.database.fetch_one(query)
        if record is not None:
            return Reservation(record)

    def __update(self, reservation_id, student_id, food_id):
        query = f"""
            UPDATE Reservations
            SET studentID = {student_id} AND foodID = {food_id}
            WHERE id = {reservation_id}
            RETURNING *;
        """

        record = self.database.fetch_one(query)
        if record is not None:
            Reservation(record)

    def insert_reservation(self, student_id, food_id):
        student = self.students.get_by_student_id(student_id)
        food = self.foods.get(food_id)
        reservation = self.get_reservation(student_id, food_id)

        if reservation is not None:
            raise Exception("This food is already reserved for this student.")

        if student is None:
            raise Exception("There is no such student.")

        if food is None:
            raise Exception("there is no such food.")

        if food.date < datetime.now():
            raise Exception("This food reservation time is over.")

        if student.balance < food.price:
            raise Exception("This student has not enough balance.")

        if food.inventory == 0:
            raise Exception("This food is over.")

        student.balance -= food.price
        food.inventory -= 1

        self.students.update_balance(student.studentID, student.balance)
        self.foods.update_inventory(food.id, food.inventory)

        self.__insert(student_id, food_id)
        self.transactions.insert('null', food.id)

    def update_reservation(self, student_id, food_id, new_food_id):
        student = self.students.get_by_student_id(student_id)
        food = self.foods.get(food_id)
        new_food = self.foods.get(new_food_id)
        reservation = self.get_reservation(student_id, food_id)

        if reservation is None:
            raise Exception("There is no such reservation.")

        if self.get_reservation(student_id, new_food_id) is not None:
            raise Exception("The new food is already reserved for this student.")

        if datetime.now() > food.date:
            raise Exception("The food date is passed.")

        if new_food.date < datetime.now():
            raise Exception("This food reservation time is over.")

        if new_food.inventory == 0:
            raise Exception("This food is over.")

        if student.balance + food.price < new_food.price:
            raise Exception("This student has not enough balance.")

        student.balance -= -food.price + new_food.price
        food.inventory += 1
        new_food.inventory -= 1

        self.students.update_balance(student.studentID, student.balance)
        self.foods.update_inventory(food.id, food.inventory)
        self.foods.update_inventory(new_food.id, new_food.inventory)

        self.__delete(reservation.id)
        self.__insert(student_id, new_food_id)
        self.transactions.insert(food.id, new_food.id)

    def delete_reservation(self, student_id, food_id):
        student = self.students.get_by_student_id(student_id)
        food = self.foods.get(food_id)
        reservation = self.get_reservation(student_id, food_id)

        if reservation is None:
            raise Exception("There is no such reservation.")

        if datetime.now() > food.date:
            raise Exception("The food date is passed.")

        student.balance += food.price
        food.inventory += 1

        self.students.update_balance(student.studentID, student.balance)
        self.foods.update_inventory(food.id, food.inventory)

        self.__delete(reservation.id)
        self.transactions.insert(food.id, 'null')
