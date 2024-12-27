# Samad Reservation Food System

This project is a **basic food reservation system for university students** developed as part of a database design course. It uses **PostgreSQL** as the database management system and implements a command-line interface for all operations. The project aims to familiarize students with raw SQL queries, foundational database concepts, and effective database design.

## Features

### Database Tables
The system includes the following tables:
1. **Students**
   - Tracks student details such as ID, name, major, date of birth, and account balance.
   - Automatically updates records when students graduate.
   - Ensures valid and consistent data entries.

2. **Foods**
   - Manages the details of available meals, including name, date, price, and inventory count.
   - Automatically updates inventory based on reservations.
   - Ensures accurate timestamps for meal availability.

3. **Reservations**
   - Records reservations made by students for specific meals.
   - Updates food inventory and student balance after each reservation.
   - Prevents negative balances or overbooking meals.

4. **Transactions**
   - Tracks changes to reservations (e.g., new, updated, or canceled).
   - Logs reservation details, ensuring data consistency and traceability.

### Operations
The system supports the following key functionalities:
1. **Student Management**
   - Add or remove students.
   - Update account balances.
   - Validate student details to prevent invalid entries.

2. **Food Management**
   - Add or remove meal entries.
   - Update inventory counts and validate meal availability.

3. **Reservations**
   - Students can reserve meals based on account balance and inventory.
   - Automatically logs transactions for every reservation.

4. **Reservation Modifications**
   - Modify existing reservations or cancel them.
   - Ensure accurate transaction records and database updates.

### Command-Line Interface
- The project uses the **`argparse`** library for CLI implementation.
- Provides easy-to-use commands for all operations, ensuring an intuitive user experience.

### Development Guidelines
1. **Database Management**
   - Uses **PostgreSQL** for database setup and management.
   - All SQL queries are written in raw SQL, without ORM or additional tools.

2. **Error Handling**
   - Comprehensive error management ensures data integrity.
   - Displays user-friendly error messages for invalid inputs or operations.

3. **No GUI**
   - This project is CLI-only, focusing on database and backend logic.

4. **Project Constraints**
   - All queries and operations must be written manually in raw SQL.
   - No use of ORM tools such as SQLAlchemy or Django ORM.

## Installation and Setup

### Prerequisites
- **Python 3.9+**
- **PostgreSQL**
- Basic understanding of SQL and Python programming.

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/Samad-Reservation-Food-Basic-Python-Database-Postgres-Basic-Project.git
