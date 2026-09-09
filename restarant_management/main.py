from food_item import FoodItem
from menu import Menu
from users import Customer, Employee, Admin
from restaurant import Restaurant
from orders import Order

my_restaurant = Restaurant("My Restaurant")

def customer_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    address = input("Enter your address: ")

    customer = Customer(name, email, phone, address)
    while True:
        print(f"Welcome {customer.name}!")
        print("\n***********Customer Menu***********")
        print("1. View Menu")
        print("2. Add Item to Cart")
        print("3. View Cart")
        print("4. Pay Bill")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            customer.view_menu(my_restaurant)
        elif choice == '2':
            item_name = input("Enter the name of the item: ")
            quantity = int(input("Enter the quantity: "))
            customer.add_to_cart(my_restaurant, item_name, quantity)
        elif choice == '3':
            customer.view_cart()
        elif choice == '4':
            customer.pay_bill()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def admin_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    address = input("Enter your address: ")

    admin = Admin(name, email, phone, address)
    while True:
        print(f"Welcome {admin.name}!")
        print("\n***********Admin Menu***********")
        print("1. Add new item to the menu")
        print("2. Add new employee")
        print("3. View employees")
        print("4. View menu")
        print("5. Delete item from the menu")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item_name = input("Enter the name of the item: ")
            item_price = float(input("Enter the price of the item: "))
            item_quantity = int(input("Enter the quantity of the item: "))
            item = FoodItem(item_name, item_price, item_quantity)
            admin.add_menu_item(my_restaurant, item)
        elif choice == '2':
            emp_name = input("Enter employee name: ")
            emp_email = input("Enter employee email: ")
            emp_phone = input("Enter employee phone: ")
            emp_address = input("Enter employee address: ")
            emp_age = int(input("Enter employee age: "))
            emp_designation = input("Enter employee designation: ")
            emp_salary = float(input("Enter employee salary: "))
            employee = Employee(emp_name, emp_email, emp_phone, emp_address, emp_age, emp_designation, emp_salary)
            admin.add_employee(my_restaurant, employee)
        elif choice == '3':
            admin.view_employees(my_restaurant)
        elif choice == '4':
            admin.view_menu(my_restaurant)
        elif choice == '5':
            item_name = input("Enter the name of the item to delete: ")
            admin.remove_item(my_restaurant, item_name)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")


while True:
    print("\n***********Welcome to the Restaurant Management System***********")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

    user_type = input("Enter your choice: ")

    if user_type == '1':
        customer_menu()
    elif user_type == '2':
        admin_menu()
    elif user_type == '3':
        break
    else:
        print("Invalid choice. Please try again.")