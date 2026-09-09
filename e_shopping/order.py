class Order:
    def __init__(self, order_id, customer_email, product_name, quantity, total_price):
        self.order_id = order_id
        self.customer_email = customer_email
        self.product_name = product_name
        self.quantity = quantity
        self.total_price = total_price

    def display_order(self):
        print(f"Order ID: {self.order_id} | Product: {self.product_name} | Qty: {self.quantity} | Total: ${self.total_price:.2f}")


class OrderManager:
    def __init__(self):
        self.__orders = []
        self.__next_order_id = 5001

    def place_order(self, customer_email, product_name, product, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero!")

        # reduce product stock
        product.reduce_stock(quantity)

        total_price = product.price * quantity
        order_id = str(self.__next_order_id)
        order = Order(order_id, customer_email, product_name, quantity, total_price)
        self.__orders.append(order)
        self.__next_order_id += 1
        return order

    def get_order_by_customer(self, customer_email):
        return [order for order in self.__orders if order.customer_email == customer_email]