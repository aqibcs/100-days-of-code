class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def login(self):
        print(f"{self.name} has logged in")

class Customer(User):
    def __init__(self, name, email, customer_id):
        super().__init__(name, email)
        self.customer_id = customer_id
        self.cart = []

    def add_to_cart(self, item):
        self.cart.append(item)
        print(f"{item} added to cart")

class Admin(User):
    def __init__(self, name, email, admin_id):
        super().__init__(name, email)
        self.admin_id = admin_id

    def add_product(self, product):
        print(f"Product {product} added to store")

# Creating objects
customer = Customer("Bob", "bob@example.com", 101)
admin = Admin("Alice", "alice@example.com", 1)

# Interacting with objects
customer.login()
customer.add_to_cart("Laptop")

admin.login()
admin.add_product("New Phone")
