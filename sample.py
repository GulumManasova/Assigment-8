from employee import Employee
from employee_dao import EmployeeDAO

# Initialize DAO
dao = EmployeeDAO()

# Insert new employees
print("🔹 Inserting employees...")
dao.insert(Employee(None, "Aliya Aman", "Manager", 60000, "2022-03-10"))
dao.insert(Employee(None, "Bekzat Omarov", "Receptionist", 35000, "2023-01-15"))

# Display all employees
print("\n📋 All Employees:")
for emp in dao.get_all():
    print(emp)

# Get employee by ID
print("\n🔎 Get Employee by ID = 1:")
emp = dao.get_by_id(1)
if emp:
    print(emp)

# Update an employee
print("\n✏️ Updating Employee ID = 1...")
emp.name = "Aliya A."
emp.salary = 62000
dao.update(emp)
print("Updated:", dao.get_by_id(1))

# Delete an employee
print("\n🗑️ Deleting Employee ID = 2...")
dao.delete(2)

# Final list
print("\n📋 Final Employees:")
for emp in dao.get_all():
    print(emp)
