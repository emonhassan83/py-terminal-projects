class Order:
    def __init__(self):
        self._items = {}

    def items(self):
        return self._items.items()

    def add_item(self, item):
        if item in self._items:
            self._items[item] += item.quantity
        else:
            self._items[item] = item.quantity

    def remove(self, item):
        if item in self._items:
            del self._items[item] # Remove item from the order
        else:
            print(f"Item {item.name} not found in the order.")

    def total_price(self):
        total = 0
        for item, quantity in self._items.items():
            total += item.price * quantity # Calculate total price of the order
        return total

    def clear_order(self):
        self._items = {} # Clear all items from the order
        print("Order cleared successfully.")