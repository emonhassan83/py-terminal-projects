class Product:
    def __init__(self, product_id, name, price, stock, seller_email):
        self.__product_id = product_id
        self.name = name
        self.price = price
        self.__stock = stock
        self.seller_email = seller_email

    @property
    def product_id(self):
        return self.__product_id

    @property
    def stock(self):
        return self.__stock

    def reduce_stock(self, quantity):
        if quantity > self.__stock:
            raise ValueError("Insufficient stock!")
        self.__stock -= quantity

class ProductManager:
    def __init__(self):
        self.__products = []
        self.__next_id = 101

    def add_product(self, name, price, stock, seller_email):
        prod_id = str(self.__next_id)
        prod = Product(prod_id, name, price, stock, seller_email)
        self.__products.append(prod)
        self.__next_id += 1
        return prod

    def get_available_products(self):
        return [prod for prod in self.__products if prod.stock > 0]

    def find_product_byId(self, product_id):
        for prod in self.__products:
            if prod.product_id == product_id and prod.stock > 0:
                return prod
            return None