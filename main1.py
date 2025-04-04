from employee import Employee
from employee_dao import EmployeeDAO

def main():
    dao = EmployeeDAO()

    # Insert test employee
    emp = Employee(None, "Alice Example", "Manager", 70000, "2025-04-04")
    dao.insert(emp)

    # Get and print all employees
    print("\nAll employees:")
    employees = dao.get_all()
    for e in employees:
        print(e)

if __name__ == "__main__":
    main()

