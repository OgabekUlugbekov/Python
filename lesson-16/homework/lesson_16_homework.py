# 1. Task: SQL Server Database Creation and Population
import pyodbc

# Replace with your SQL Server connection details
conn_str = (
    "DRIVER={SQL Server};"
    "SERVER=your_server_name;"  # e.g., localhost or your server name
    "DATABASE=your_database_name;"  # e.g., SchoolDB
    "Trusted_Connection=yes;"  # Use Windows Authentication, or provide UID and PWD
    # "UID=your_username;PWD=your_password;"  # Uncomment if using SQL Server Authentication
)

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='students' AND xtype='U')
    CREATE TABLE students (
        id INT PRIMARY KEY,
        name VARCHAR(50),
        age INT,
        grade INT
    )
''')

# Populate table with data
students_data = [(1, "Alice", 20, 85), (2, "Bob", 21, 90), (3, "Charlie", 19, 78)]
for student in students_data:
    cursor.execute("IF NOT EXISTS (SELECT 1 FROM students WHERE id = ?) "
                   "INSERT INTO students (id, name, age, grade) VALUES (?, ?, ?, ?)",
                   (student[0], *student))
conn.commit()
conn.close()

# 2. Task: Querying the Database
import pyodbc

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
cursor.execute("SELECT * FROM students WHERE grade > 80")
results = cursor.fetchall()
for row in results:
    print(row)
conn.close()

# 3. Task: Updating and Deleting Records
import pyodbc

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
cursor.execute("UPDATE students SET grade = 95 WHERE name = 'Alice'")
cursor.execute("DELETE FROM students WHERE name = 'Charlie'")
conn.commit()
conn.close()

# 4. Task: Employee Management System
import pyodbc

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Create employees table if it doesn't exist
cursor.execute('''
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='employees' AND xtype='U')
    CREATE TABLE employees (
        id INT PRIMARY KEY,
        name VARCHAR(50),
        department VARCHAR(50),
        salary INT
    )
''')

def add_employee(id, name, department, salary):
    cursor.execute("INSERT INTO employees (id, name, department, salary) VALUES (?, ?, ?, ?)",
                   (id, name, department, salary))
    conn.commit()

def view_employees():
    cursor.execute("SELECT * FROM employees")
    return cursor.fetchall()

def update_salary(id, new_salary):
    cursor.execute("UPDATE employees SET salary = ? WHERE id = ?", (new_salary, id))
    conn.commit()

def delete_employee(id):
    cursor.execute("DELETE FROM employees WHERE id = ?", (id,))
    conn.commit()

# Test the Employee Management System
add_employee(1, "John", "HR", 50000)
add_employee(2, "Jane", "IT", 60000)
print(view_employees())
update_salary(1, 55000)
delete_employee(2)
print(view_employees())
conn.close()