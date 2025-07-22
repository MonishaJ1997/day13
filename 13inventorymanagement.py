# Item class
class Item:
    def __init__(self, item_id, name, quantity, price):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"[{self.item_id}] {self.name} - {self.quantity} pcs @ ₹{self.price}"

# Supplier class with encapsulation
class Supplier:
    def __init__(self, name, contact):
        self.__name = name
        self.__contact = contact

    def get_details(self):
        return f"Supplier: {self.__name}, Contact: {self.__contact}"

    def set_contact(self, new_contact):
        self.__contact = new_contact

# Inventory class using dunder methods
class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.item_id] = item

    def update_item(self, item_id, quantity=None, price=None):
        if item_id in self.items:
            if quantity is not None:
                self.items[item_id].quantity = quantity
            if price is not None:
                self.items[item_id].price = price

    def remove_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]

    def __getitem__(self, item_id):
        return self.items.get(item_id, "Item not found")

    def __contains__(self, item_id):
        return item_id in self.items

    def __str__(self):
        output = "📦 Inventory:\n"
        for item in self.items.values():
            output += str(item) + "\n"
        return output.strip()

# Create items
item1 = Item(101, "Mouse", 25, 499)
item2 = Item(102, "Keyboard", 15, 799)

# Create supplier
supplier = Supplier("Tech Supplies Co.", "9876543210")

# Create inventory
inv = Inventory()
inv.add_item(item1)
inv.add_item(item2)

# Print inventory
print(inv)
print()

# Access item using dunder __getitem__
print("Get item 101:", inv[101])

# Check item using __contains__
print("Is item 102 in inventory?", 102 in inv)

# Update item
inv.update_item(102, quantity=20)

# Remove item
inv.remove_item(101)

print("\nAfter updates:")
print(inv)

# Show supplier info securely
print("\n🔐", supplier.get_details())
