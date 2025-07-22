# Seat class
class Seat:
    def __init__(self, number):
        self.number = number
        self.available = True

    def reserve(self):
        if self.available:
            self.available = False
            return True
        return False

    def __str__(self):
        return f"Seat {self.number} - {'Available' if self.available else 'Booked'}"

# Passenger class
class Passenger:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, Age: {self.age}"

# Bus class
class Bus:
    def __init__(self, bus_no, total_seats):
        self.bus_no = bus_no
        self.seats = [Seat(i+1) for i in range(total_seats)]

    def get_available_seats(self):
        return [seat for seat in self.seats if seat.available]

    def find_seat(self, number):
        for seat in self.seats:
            if seat.number == number:
                return seat
        return None

    def __str__(self):
        return f"🚌 Bus No: {self.bus_no}"

# Booking class
class Booking:
    def __init__(self, passenger, bus, seat_number):
        self.passenger = passenger
        self.bus = bus
        self.seat = self.bus.find_seat(seat_number)
        if not self.seat or not self.seat.reserve():
            raise Exception("Seat not available or invalid!")

    def __eq__(self, other):
        return (self.passenger.name == other.passenger.name and
                self.bus.bus_no == other.bus.bus_no and
                self.seat.number == other.seat.number)

    def __str__(self):
        return (f"🎫 Ticket:\nPassenger: {self.passenger}\n"
                f"{self.bus}\nSeat No: {self.seat.number}")

# Create a bus with 5 seats
bus1 = Bus("TN-07-AB-1234", 5)

# Show available seats
print("Available Seats:")
for seat in bus1.get_available_seats():
    print(seat)

# Create passengers
p1 = Passenger("Arun", 28)
p2 = Passenger("Divya", 22)

# Book tickets
booking1 = Booking(p1, bus1, 2)
booking2 = Booking(p2, bus1, 4)

# Display tickets
print("\n" + str(booking1))
print("\n" + str(booking2))

# Attempt to compare
print("\nAre bookings same?", booking1 == booking2)

# Show remaining available seats
print("\nRemaining Seats:")
for seat in bus1.get_available_seats():
    print(seat)
