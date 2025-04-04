import sqlite3
from employee import Employee
class EmployeeDAO:
    def __init__(self,db_name='database.sqlite'):
        self.conn=sqlite3.connect(db_name)
        self.cursor=self.conn.cursor()
    def insert (self,employee):
        self.cursor.execute('INSERT INTO employee(name,position,salary,hire_date) VALUES (?,?,?,?)',
                            (employee.name,employee.position,employee.salary,employee.hire_date))
        self.conn.commit()
    def get_by_id(self,id):
        self.cursor.execute('SELECT * FROM employee WHERE id=?',(id,))
        row=self.cursor.fetchone()
        return Employee(*row) if row else None
    def get_all(self):
        self.cursor.execute("SELECT * FROM employee")
        rows=self.cursor.fetchall()
        return [Employee(*row) for row in rows]
    def update(self,employee):
        self.cursor.execute('UPDATE employee SET name=?,position=?,salary=?,hire_date=? WHERE id=?',
                            (employee.name,employee.position,employee.salary,employee.hire_date ))
        self.conn.commit()
    def delete(self,id):
        self.cursor.execute('DELETE FROM employee WHERE id=?',(id,))
        self.conn.commit()