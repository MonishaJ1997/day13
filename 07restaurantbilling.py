# MenuItem class
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ₹{self.price}"

# Customer class
class Customer:
    def __init__(self, name, mobile):
        self.name = name
        self.mobile = mobile

    def __str__(self):
        return f"{self.name} ({self.mobile})"

# Order class (composition)
class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"✅ Added: {item.name}")

    def remove_item(self, item_name):
        for i in self.items:
            if i.name == item_name:
                self.items.remove(i)
                print(f"❌ Removed: {i.name}")
                return
        print("⚠️ Item not found!")

    def total_amount(self):
        return sum(i.price for i in self.items)

    def __len__(self):
        return len(self.items)

# Bill class
class Bill:
    tax_rate = 0.05  # 5% tax

    @staticmethod
    def calculate_tax(amount):
        return amount * Bill.tax_rate

    @classmethod
    def generate_bill(cls, order):
        print("\n🧾 BILL")
        print("-" * 30)
        print(f"Customer: {order.customer}")
        for item in order.items:
            print(f" - {item.name}: ₹{item.price}")
        subtotal = order.total_amount()
        tax = cls.calculate_tax(subtotal)
        total = subtotal + tax
        print("-" * 30)
        print(f"Subtotal: ₹{subtotal}")
        print(f"Tax @ {cls.tax_rate*100:.0f}%: ₹{tax:.2f}")
        print(f"Total Amount: ₹{total:.2f}")
        print("-" * 30)

# Menu Items
menu = [
    MenuItem("Dosa", 60),
    MenuItem("Pizza", 150),
    MenuItem("Coffee", 40),
    MenuItem("Burger", 120)
]

# Show menu
print("📜 MENU:")
for item in menu:
    print(" -", item)

# Create customer and order
cust = Customer("Kumar", "9876543210")
order = Order(cust)

# Add items to order
order.add_item(menu[0])
order.add_item(menu[2])
order.add_item(menu[3])

# Remove one item
order.remove_item("Pizza")  # not added
order.remove_item("Coffee")

# Re-add something
order.add_item(menu[1])

# Generate bill
Bill.generate_bill(order)
