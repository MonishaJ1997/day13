# Seat class
class Seat:
    def __init__(self, seat_no):
        self.seat_no = seat_no
        self.booked = False

    def book(self):
        if not self.booked:
            self.booked = True
            return True
        return False

    def cancel(self):
        self.booked = False

    def is_available(self):
        return not self.booked

# Movie class
class Movie:
    def __init__(self, title, show_time, total_seats):
        self.title = title
        self.show_time = show_time
        self.seats = [Seat(i+1) for i in range(total_seats)]

    @staticmethod
    def check_availability(seats):
        return [seat for seat in seats if seat.is_available()]

    def get_seat(self, seat_no):
        if 0 < seat_no <= len(self.seats):
            return self.seats[seat_no - 1]
        return None

    def __str__(self):
        return f"🎬 {self.title} at {self.show_time}"

# User class
class User:
    def __init__(self, name):
        self.name = name

# Ticket class
class Ticket:
    def __init__(self, user, movie, seat):
        self.user = user
        self.movie = movie
        self.seat = seat

    def __str__(self):
        return (f"🎟️ Ticket\n"
                f"Name     : {self.user.name}\n"
                f"Movie    : {self.movie.title}\n"
                f"Time     : {self.movie.show_time}\n"
                f"Seat No. : {self.seat.seat_no}")



# Create movie
m1 = Movie("Avengers", "6:00 PM", 5)
m2 = Movie("Interstellar", "9:00 PM", 3)

# Create user
u1 = User("Karthik")
u2 = User("Neha")

# Book ticket
seat_to_book = m1.get_seat(3)
if seat_to_book and seat_to_book.book():
    ticket1 = Ticket(u1, m1, seat_to_book)
    print(ticket1)
else:
    print("❌ Seat not available.")

print()

# Book another seat
seat_to_book2 = m2.get_seat(2)
if seat_to_book2 and seat_to_book2.book():
    ticket2 = Ticket(u2, m2, seat_to_book2)
    print(ticket2)
else:
    print("❌ Seat not available.")

print()

# Show available seats
available = Movie.check_availability(m1.seats)
print(f"Available Seats for {m1.title}: {[seat.seat_no for seat in available]}")
