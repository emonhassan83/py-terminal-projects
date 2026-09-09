class Menu:
    def __init__(self):
        self.items = [] # List to store menu items treat as db

    def add_menu_item(self, item):
        self.items.append(item)
        print(f"Menu item {item.name} added successfully.")

    def find_items(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None

    def remove_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                self.items.remove(item)
                print(f"Menu item {item.name} removed successfully.")
                return
        print(f"Menu item {item_name} not found.")

    def show_menu(self):
        print("\n***********Menu***********")
        print("Name\tPrice\tQuantity")
        if not self.items:
            print("Menu is empty.")
        else:
            for item in self.items:
                print(f"{item.name}\t${item.price:.2f}\t{item.quantity}")
