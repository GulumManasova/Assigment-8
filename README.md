# Employee Management System
This is a Python-based application for managing employee records in a relational database. It uses SQLite for database operations and implements CRUD (Create, Read, Update, Delete) functionality.

Overview
The project consists of three main components:

Employee class: Defines the employee entity.

EmployeeDAO class: Handles CRUD operations with the database.

Test script: Validates CRUD operations.

Database Schema
employee table with the following columns:

id (INTEGER, Primary Key, Auto Increment)

name (TEXT)

position (TEXT)

salary (REAL)

hire_date (TEXT)

Key Features
Create: Add new employees to the database.

Read: Fetch employee details by ID or list all employees.

Update: Modify an employee’s details.

Delete: Remove an employee’s record.
