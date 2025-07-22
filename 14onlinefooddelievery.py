# Base User class
class User:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.name} ({self.phone})"

# Customer inherits from User
class Customer(User):
    def __init__(self, name, phone, address):
        super().__init__(name, phone)
        self.address = address

# Restaurant class
class Restaurant:
    def __init__(self, name, location, menu):
        self.name = name
        self.location = location
        self.menu = menu  # dict of {item: price}

    def show_menu(self):
        return "\n".join([f"{item}: ₹{price}" for item, price in self.menu.items()])

    def __str__(self):
        return f"{self.name} - {self.location}"

# Order aggregates restaurant and customer
class Order:
    def __init__(self, customer, restaurant, items):
        self.customer = customer
        self.restaurant = restaurant
        self.items = items  # list of item names
        self.total = sum(restaurant.menu[item] for item in items)

    def summary(self):
        items_list = ", ".join(self.items)
        return (f"🧾 Order Summary:\nCustomer: {self.customer.name}\n"
                f"Restaurant: {self.restaurant.name}\nItems: {items_list}\nTotal: ₹{self.total}")

# Polymorphic base delivery class
class Delivery:
    def deliver(self, order):
        raise NotImplementedError("Subclasses must override deliver()")

# Subclasses with polymorphism
class BikeDelivery(Delivery):
    def deliver(self, order):
        return f"🏍️ Bike Delivery assigned to {order.customer.name} at {order.customer.address}"

class DroneDelivery(Delivery):
    def deliver(self, order):
        return f"🚁 Drone Delivery zooming to {order.customer.address} for {order.customer.name}"

# Menu of the restaurant
menu = {
    "Pizza": 250,
    "Burger": 120,
    "Pasta": 180
}

# Create instances
resto = Restaurant("Food Corner", "Anna Nagar", menu)
cust = Customer("Ravi", "9876543210", "T Nagar, Chennai")

# Place order
items = ["Pizza", "Burger"]
order = Order(cust, resto, items)

# Show summary
print(order.summary())

# Choose delivery mode (polymorphism)
delivery_agent = BikeDelivery()
print(delivery_agent.deliver(order))

print("\n🔄 Switching to Drone Delivery...\n")
delivery_agent = DroneDelivery()
print(delivery_agent.deliver(order))
