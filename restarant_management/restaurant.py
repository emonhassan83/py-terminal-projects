from menu import Menu

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.employees = [] # List to store employees treat as db
        self.menu = Menu() # Menu class to manage food items

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Employee {employee.name} added successfully.")

    def view_employees(self):
            if not self.employees:
                print("No employees found.")
            else:
                for emp in self.employees:
                    print(f"Name: {emp.name}, Email: {emp.email}, Phone: {emp.phone}, Address: {emp.address}, Age: {emp.age}, Designation: {emp.designation}, Salary: {emp.salary}")
