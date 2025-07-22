from abc import ABC, abstractmethod

# Abstract base vehicle class
class Vehicle(ABC):
    def __init__(self, vehicle_id, brand, base_rate):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.base_rate = base_rate
        self.available = True

    @abstractmethod
    def calculate_rent(self, days):
        pass

    def __str__(self):
        return f"{self.vehicle_id} - {self.brand} | Rate: ₹{self.base_rate}/day | {'Available' if self.available else 'Rented'}"

# Bike subclass
class Bike(Vehicle):
    def calculate_rent(self, days):
        return self.base_rate * days

# Car subclass
class Car(Vehicle):
    def calculate_rent(self, days):
        return (self.base_rate * days) + 500  # fixed surcharge

# Customer class
class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.rented_vehicle = None

    def __str__(self):
        return f"Customer: {self.name} (ID: {self.customer_id})"

# Rental system
class Rental:
    vehicles = []

    @classmethod
    def add_vehicle(cls, vehicle):
        cls.vehicles.append(vehicle)

    @classmethod
    def show_available_vehicles(cls):
        print("\n🚗 Available Vehicles:")
        for v in cls.vehicles:
            if v.available:
                print(" -", v)

    @staticmethod
    def calculate_tax(amount):
        return amount * 0.18  # 18% GST

    def rent_vehicle(self, customer, vehicle_id, days):
        for v in Rental.vehicles:
            if v.vehicle_id == vehicle_id and v.available:
                rent_amount = v.calculate_rent(days)
                tax = self.calculate_tax(rent_amount)
                total = rent_amount + tax
                v.available = False
                customer.rented_vehicle = v
                print(f"\n✅ {customer.name} rented {v.brand} for {days} days.")
                print(f"Rent: ₹{rent_amount} + Tax: ₹{tax:.2f} = Total: ₹{total:.2f}")
                return
        print("❌ Vehicle not available!")

    def return_vehicle(self, customer):
        v = customer.rented_vehicle
        if v:
            v.available = True
            print(f"\n✅ {customer.name} returned {v.brand}")
            customer.rented_vehicle = None
        else:
            print("❌ No vehicle to return!")

# Add vehicles to system
Rental.add_vehicle(Bike("B101", "Yamaha", 300))
Rental.add_vehicle(Car("C202", "Honda City", 1200))
Rental.add_vehicle(Car("C203", "Hyundai Creta", 1500))

# Create customer
cust1 = Customer("Ravi", "C001")

# Show available
Rental.show_available_vehicles()

# Create rental system and rent a vehicle
rental_sys = Rental()
rental_sys.rent_vehicle(cust1, "C202", 3)

# Show available after rent
Rental.show_available_vehicles()

# Return vehicle
rental_sys.return_vehicle(cust1)

# Show available after return
Rental.show_available_vehicles()
