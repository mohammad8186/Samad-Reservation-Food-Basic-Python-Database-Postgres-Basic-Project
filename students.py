

class Student:

    def __init__(self, record):
        self.record = record
        self.id = record[0]
        self.studentID = record[1]
        self.major = record[2]
        self.birth_date = record[3]
        self.first_name = record[4]
        self.last_name = record[5]
        self.balance = record[6]

    def __str__(self):
        record = list(self.record)
        record[3] = self.birth_date.strftime('%Y-%m-%d')
        return str(tuple(record))



class Students:


    majors = ['cs', 'math', 'art', 'politics']

    def __init__(self, database):
        self.database = database
        self.create_table()


    def create_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS Students (
                ID SERIAL PRIMARY KEY,
                studentID INT CHECK (studentID > 0) UNIQUE NOT NULL,
                major VARCHAR(50) NOT NULL,
                birth_date DATE NOT NULL,
                first_name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50) NOT NULL,
                balance INT CHECK (balance >= 0) NOT NULL
                
            )
        """

        self.database.start_transaction()
        self.database.execute(query)
        self.database.commit()

    def get_all(self) -> [Student]:
        query = """
            SELECT * FROM Students
        """

        records = self.database.fetch_all(query)
        if records is not None:
            return [Student(record) for record in records]

    def get_by_student_id(self, student_id) -> Student:
        query = f"""
            SELECT * FROM Students
            WHERE studentID = {student_id} 
        """

        record = self.database.fetch_one(query)
        if record is not None:
            return Student(record)

    def delete_by_student_id(self, student_id):
        query = f"""
            DELETE FROM Students
            WHERE studentID = {student_id}
        """

        self.database.execute(query)

    def insert(self, student_id, major, birth_date, first_name, last_name, balance):

        if major not in Students.majors:
            raise Exception(f"Major should be one of [{', '.join(Students.majors)}]")

        query = f"""
            INSERT INTO Students (studentID, major, birth_date, first_name, last_name, balance)
            VALUES ({student_id}, '{major}', '{birth_date}', '{first_name}', '{last_name}', {balance})
            RETURNING *
        """

        record = self.database.fetch_one(query)
        if record is not None:
            return Student(record)

    def update_balance(self, student_id, balance):
        student = self.get_by_student_id(student_id)
        student.balance = balance

        query = f"""
            UPDATE Students
            SET balance = {student.balance}
            WHERE studentID = {student_id}
            RETURNING *
        """

        record = self.database.fetch_one(query)
        if record is not None:
            return Student(record)

    def add_balance(self, student_id, balance):
        student = self.get_by_student_id(student_id)

        if student is None:
            raise Exception("There is no such student.")

        student.balance += balance
        student = self.update_balance(student.studentID, student.balance)
        return student
