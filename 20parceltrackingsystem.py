import random
import string

# Base Person class
class Person:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def __str__(self):
        return f"{self.name}, {self.address}, 📞 {self.phone}"


# Sender and Receiver classes using inheritance
class Sender(Person):
    pass

class Receiver(Person):
    pass


# Tracking class with static methods
class Tracking:
    @staticmethod
    def generate_id():
        return "TRK" + ''.join(random.choices(string.digits, k=7))

    @staticmethod
    def validate_id(tracking_id):
        return tracking_id.startswith("TRK") and len(tracking_id) == 10


# Parcel class using composition
class Parcel:
    def __init__(self, sender, receiver, weight):
        self.sender = sender                  # Composition
        self.receiver = receiver              # Composition
        self.weight = weight
        self.tracking_id = Tracking.generate_id()
        self.status = "In Transit"

    def update_status(self, new_status):
        self.status = new_status

    def display_details(self):
        print(f"📦 Tracking ID: {self.tracking_id}")
        print(f"Weight: {self.weight} kg")
        print(f"Status: {self.status}")
        print(f"From: {self.sender}")
        print(f"To:   {self.receiver}")

# Create sender and receiver objects
sender = Sender("Ravi Kumar", "Chennai", "9876543210")
receiver = Receiver("Priya Sharma", "Mumbai", "9123456780")

# Create a parcel
parcel = Parcel(sender, receiver, weight=2.5)

# Display parcel details
parcel.display_details()

# Update status
parcel.update_status("Delivered")

print("\n🔄 Updated Status:")
parcel.display_details()

# Validate tracking ID
print("\n✅ Valid Tracking ID?", Tracking.validate_id(parcel.tracking_id))
