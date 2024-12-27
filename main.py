import argparse

from database import Database
from foods import Foods
from reservations import Reservations
from students import Students
from transactions import Transactions

database = Database()
if database.connection is None:
    exit()

students = Students(database)
foods = Foods(database)
transactions = Transactions(database)
reservations = Reservations(database, students, foods, transactions)

actions = ['add_student', 'del_student', 'add_balance',
           'add_food', 'del_food',
           'add_res', 'del_res', 'update_res']

help_message = ''' examples:
    
    add_student 12345 cs 2010-1-1 ali rahimi 500
    del_student 12345
    add_balance 12345 1500
    
    add_food soup 2024-10-1:1:00 100 10
    del_food 1
    
    add_res 12345 1
    del_res 12345 1
    update_res 12345 1 2 '''


def main():
    parser = argparse.ArgumentParser()
    parser.error = lambda err: {print(help_message), exit()}
    parser.add_argument("action", choices=actions, help="Input action")
    parser.add_argument("args", nargs=argparse.REMAINDER, help="Input arguments")

    args = parser.parse_args()
    action = args.action.lower()
    args = args.args

    if action == 'add_student':
        # example:
        # add_student 12345 cs 2010-1-1 ali rahimi 500
        student = students.insert(args[0], args[1], args[2], args[3], args[4], args[5])
        print('This student is added:')
        print(student)
        return

    if action == 'del_student':
        # example:
        # del_student 12345
        student_id = args[0]
        student = students.get_by_student_id(student_id)
        students.delete_by_student_id(student_id)
        print('This student is deleted:')
        print(student)
        return

    if action == 'add_balance':
        # example:
        # add_balance 12345 1500
        student_id = args[0]
        balance = int(args[1])
        student = students.add_balance(student_id, balance)
        print('This student balance is updates:')
        print(student)
        return

    if action == 'add_food':
        # example:
        # add_food soup 2024-10-1:1:00 100 10
        food = foods.insert(args[0], args[1], args[2], args[3])
        print('This food is added:')
        print(food)
        return

    if action == 'del_food':
        # example:
        # del_food 1
        food_id = args[0]
        food = foods.get(food_id)
        foods.delete(food_id)
        print('This food is deleted:')
        print(food)
        return

    if action == 'add_res':
        # example:
        # add_res 12345 1
        student_id = args[0]
        food_id = args[1]
        reservations.insert_reservation(student_id, food_id)
        student = students.get_by_student_id(student_id)
        food = foods.get(food_id)
        print('The food is reserved for the student.')
        print(student)
        print(food)
        return

    if action == 'del_res':
        # example:
        # del_res 12345 1
        student_id = args[0]
        food_id = args[1]
        reservations.delete_reservation(student_id, food_id)
        student = students.get_by_student_id(student_id)
        food = foods.get(food_id)
        print('The food reservation is removed for the student.')
        print(student)
        print(food)
        return

    if action == 'update_res':
        # example:
        # update_res 12345 1 2
        student_id = args[0]
        food_id = args[1]
        new_food_id = args[2]
        reservations.update_reservation(student_id, food_id, new_food_id)
        student = students.get_by_student_id(student_id)
        food = foods.get(food_id)
        new_food = foods.get(new_food_id)
        print('The reservation is updated for the student.')
        print(student)
        print(food)
        print(new_food)
        return


if __name__ == '__main__':
    try:
        database.start_transaction()
        main()
        database.commit()
    except Exception as error:
        print(error)
    finally:
        database.close_connection()
