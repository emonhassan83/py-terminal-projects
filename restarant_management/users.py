# Customer, Employee, and Admin classes for user management

from abc import ABC
from orders import Order

class User(ABC):
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

class Customer(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        self.cart = Order()  # Initialize an empty cart for the customer

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()

    def add_to_cart(self, restaurant, item_name, quantity):
        item = restaurant.menu.find_items(item_name)

        if item:
            if quantity > item.quantity:
                print(f"Only {item.quantity} of {item.name} available. Cannot add {quantity}.")
                return
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print(f"Added {quantity} of {item.name} to the cart.")
        else:
            print(f"Item {item_name} not found in the menu.")

    def view_cart(self):
        if self.cart:
            print("\n***********Cart***********")
            print("Name\tPrice\tQuantity")
            for item, quantity in self.cart.items():
                print(f"{item.name}\t${item.price:.2f}\t{quantity}")
                print(f"Total Price: ${self.cart.total_price():.2f}")
        else:
            print("Cart is empty.")

    def pay_bill(self):
        print(f"Total bill amount: ${self.cart.total_price():.2f}")
        self.cart.clear_order()

class Employee(User):
    def __init__(self, name, email, phone, address, age, designation, salary):
        super().__init__(name, email, phone, address)
        self.age = age
        self.designation = designation
        self.salary = salary

class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)

    def add_employee(self, restaurant, employee):
        restaurant.add_employee(employee)

    def view_employees(self, restaurant):
        restaurant.view_employees()

    def add_menu_item(self, restaurant, item):
        restaurant.menu.add_menu_item(item)

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()

    def remove_item(self, restaurant, item_name):
        restaurant.menu.remove_item(item_name)

