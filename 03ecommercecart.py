# Base Product class
class Product:
    def __init__(self, name, price, category="General"):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name} ({self.category}) - ₹{self.price:.2f}"

# Cart class with dunder methods
class Cart:
    def __init__(self):
        self.items = {}  # Product: quantity

    def add_item(self, product, quantity=1):
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def remove_item(self, product):
        if product in self.items:
            del self.items[product]

    def total_cost(self):
        return sum(product.price * qty for product, qty in self.items.items())

    def __add__(self, other):  # Add carts
        new_cart = Cart()
        new_cart.items = self.items.copy()
        for product, qty in other.items.items():
            new_cart.add_item(product, qty)
        return new_cart

    def __getitem__(self, index):  # Access nth item
        return list(self.items.items())[index]

    def __contains__(self, product):  # Check if product in cart
        return product in self.items

    def __str__(self):
        result = "\n🛒 Cart Items:\n"
        for product, qty in self.items.items():
            result += f"{product.name} x {qty} = ₹{product.price * qty:.2f}\n"
        result += f"Total: ₹{self.total_cost():.2f}"
        return result

# User class
class User:
    def __init__(self, name):
        self.name = name
        self.cart = Cart()

    def add_to_cart(self, product, qty=1):
        self.cart.add_item(product, qty)

    def remove_from_cart(self, product):
        self.cart.remove_item(product)

# Order class
class Order:
    def __init__(self, user):
        self.user = user
        self.cart = user.cart
        self.discount = 0.1  # 10%

    @staticmethod
    def calculate_tax(amount):
        return amount * 0.18  # 18% GST

    def final_total(self):
        subtotal = self.cart.total_cost()
        discount_amt = subtotal * self.discount
        tax_amt = Order.calculate_tax(subtotal - discount_amt)
        total = subtotal - discount_amt + tax_amt
        return {
            "Subtotal": subtotal,
            "Discount": discount_amt,
            "Tax": tax_amt,
            "Total": total
        }

    def summary(self):
        print(f"\n🧾 Order Summary for {self.user.name}")
        print(self.cart)
        totals = self.final_total()
        print(f"\nSubtotal: ₹{totals['Subtotal']:.2f}")
        print(f"Discount: ₹{totals['Discount']:.2f}")
        print(f"Tax: ₹{totals['Tax']:.2f}")
        print(f"Grand Total: ₹{totals['Total']:.2f}")


# Products
p1 = Product("Laptop", 50000, "Electronics")
p2 = Product("Book", 500, "Stationery")
p3 = Product("Shoes", 2500, "Fashion")

# User and Cart
u1 = User("Ravi")
u1.add_to_cart(p1)
u1.add_to_cart(p2, 2)

# Cart check
print(p1 in u1.cart)         # True
print(u1.cart[1])            # (Book, 2)

# Order
order = Order(u1)
order.summary()
