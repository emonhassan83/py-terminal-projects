from user import UserManager, Customer, Seller
from product import ProductManager
from order import OrderManager

def run_app():
    user_mgr = UserManager()
    product_mgr = ProductManager()
    order_mgr = OrderManager()

    while True:
        print("\n" + "=" * 45)
        print("          E-SHOPPING SYSTEM (OOP)          ")
        print("=" * 45)
        print("1. Register Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Select Option (1-3): ").strip()
        if choice == '1':
            print("\n--- Register ---")
            email = input("Enter Email: ").strip()
            password = input("Enter Password: ").strip()
            role = input("Enter Role (customer/seller): ").strip().lower()

            try:
                user_mgr.register_user(email, password, role)
                print("🎉 Account registered successfully! Please login.")
            except ValueError as e:
                print(f"❌ Error: {e}")

        elif choice == '2':
            print("\n--- Login ---")
            email = input("Enter Email: ").strip()
            password = input("Enter Password: ").strip()

            current_user = user_mgr.login(email, password)

            if not current_user:
                print("❌ Invalid Email or Password!")
                continue
            print(f"\nWelcome, {current_user.email} [{current_user.role}]")

            # --- SELLER MENU ---
            if isinstance(current_user, Seller):
                while True:
                    print("\n--- SELLER DASHBOARD ---")
                    print("1. Publish New Product")
                    print("2. Logout")

                    seller_choice = input("Select Option: ").strip()

                    if seller_choice == "1":
                        name = input("Product Name: ").strip()
                        try:
                            price = float(input("Product Price ($): "))
                            stock = int(input("Stock Quantity: "))
                            product_mgr.add_product(name, price, stock, current_user.email)
                            print(f"✅ Product '{name}' published successfully!")
                        except ValueError:
                            print("❌ Invalid price or stock amount!")

                    elif seller_choice == "2":
                        break

            # --- CUSTOMER MENU ---
            elif isinstance(current_user, Customer):
                while True:
                    print("\n--- CUSTOMER DASHBOARD ---")
                    print("1. View Available Products")
                    print("2. Place Order")
                    print("3. My Orders")
                    print("4. Logout")

                    cust_choice = input("Select Option: ").strip()

                    if cust_choice == "1":
                        products = product_mgr.get_available_products()
                        print("\n--- AVAILABLE PRODUCTS ---")
                        if not products:
                            print("No products available (or all stock out).")
                        else:
                            for p in products:
                                print(f"ID: {p.product_id} | Name: {p.name:<15} | Price: ${p.price:<7} | Stock Left: {p.stock}")

                    elif cust_choice == "2":
                        pid = input("Enter Product ID to Buy: ").strip()
                        product = product_mgr.find_product_by_id(pid)

                        if not product:
                            print("❌ Invalid Product ID or Product Stock Out!")
                            continue

                        try:
                            qty = int(input(f"Enter Quantity for '{product.name}' (Available {product.stock}): "))
                            order = order_mgr.place_order(current_user, product, qty)
                            print(f"\n🎉 Order Placed Successfully!")
                            order.display_order()
                        except ValueError as e:
                            print(f"❌ Error: {e}")

                    elif cust_choice == "3":
                        my_orders = order_mgr.get_orders_by_customer(current_user.email)
                        print("\n--- MY ORDERS ---")
                        if not my_orders:
                            print("No orders placed yet.")
                        else:
                            for o in my_orders:
                                o.display_order()

                    elif cust_choice == "4":
                        break

        elif choice == "3":
            print("\nThank you for visiting! Goodbye.")
            break
        else:
            print("❌ Invalid selection!")


if __name__ == "__main__":
    run_app()