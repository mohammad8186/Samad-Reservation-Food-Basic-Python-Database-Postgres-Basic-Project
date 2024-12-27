# 🍴 Samad Reservation Food System

This project is a **comprehensive food reservation system** tailored for university students, designed as part of a database design course. It utilizes **PostgreSQL** as the database management system and a **command-line interface (CLI)** for user interactions. The primary objective is to enhance familiarity with **raw SQL queries**, foundational database principles, and effective system design practices.

---

## ✨ Features

### 📊 Database Tables
The system includes the following core tables:

1. **👩‍🎓 Students**
   - Stores detailed student information such as ID, name, major, date of birth, and account balance.
   - Automatically updates records upon student graduation.
   - Enforces data integrity and validity checks.

2. **🍽️ Foods**
   - Maintains information on available meals, including name, date, price, and inventory.
   - Updates inventory dynamically based on reservations.
   - Tracks accurate timeframes for meal availability.

3. **📜 Reservations**
   - Logs reservations made by students for specific meals.
   - Updates food inventory and student balances post-reservation.
   - Prevents overbooking and negative account balances.

4. **💳 Transactions**
   - Captures changes to reservations (e.g., creation, modification, cancellation).
   - Provides a detailed audit trail to ensure data consistency and transparency.

---

### ⚙️ Core Operations
The system supports the following functionalities:

1. **👥 Student Management**
   - Add, update, or remove student records.
   - Modify account balances with validation to prevent inconsistencies.
   - Ensure all student data entries are valid and complete.

2. **🥗 Food Management**
   - Add or delete food items with real-time inventory tracking.
   - Validate availability and pricing of meals dynamically.

3. **📅 Meal Reservations**
   - Enable students to reserve meals based on their account balance and food availability.
   - Automatically log all reservation activities in the transaction table.

4. **🔄 Modify Reservations**
   - Support for altering or canceling existing reservations.
   - Synchronize transaction logs and database tables seamlessly.

---

### 🛠️ Development Standards

1. **📂 Database Design**
   - Leverages **PostgreSQL** for robust database management.
   - Emphasizes the use of **raw SQL queries** to deepen understanding.

2. **🚨 Error Handling**
   - Implements comprehensive error management to maintain data integrity.
   - Displays clear, user-friendly messages for invalid operations.

3. **❌ No GUI**
   - Operates entirely via CLI, focusing on backend and database functionalities.

4. **📜 Project Constraints**
   - All queries are hand-crafted in SQL without using ORM tools (e.g., SQLAlchemy or Django ORM).

---

## 🚀 Installation and Setup

### Prerequisites
- 🐍 **Python 3.9+**
- 🐘 **PostgreSQL**
- Basic knowledge of SQL and Python programming.

### Installation Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/mohammad8186/Samad-Reservation-Food-Basic-Python-Database-Postgres-Basic-Project.git

