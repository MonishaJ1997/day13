# Attendee class
class Attendee:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} ({self.email})"


# Session class
class Session:
    def __init__(self, title, speaker, time):
        self.title = title
        self.speaker = speaker
        self.time = time

    def __str__(self):
        return f"Session: {self.title} by {self.speaker} at {self.time}"


# Event class with multiple sessions
class Event:
    def __init__(self, name):
        self.name = name
        self.sessions = []

    def add_session(self, session):
        self.sessions.append(session)

    def show_sessions(self):
        for session in self.sessions:
            print(session)


# Registration class (Aggregation)
class Registration:
    total_attendees = 0
    registrations = []

    def __init__(self, attendee, session):
        self.attendee = attendee
        self.session = session
        Registration.registrations.append(self)
        Registration.total_attendees += 1

    def __str__(self):
        return f"{self.attendee} registered for '{self.session.title}'"

    @classmethod
    def get_total_attendees(cls):
        return cls.total_attendees

    @classmethod
    def list_all(cls):
        return [str(reg) for reg in cls.registrations]

# Create sessions
s1 = Session("AI in 2025", "Dr. Meena", "10:00 AM")
s2 = Session("Cybersecurity Trends", "Mr. Ravi", "11:30 AM")

# Create event and add sessions
conf = Event("TechConf 2025")
conf.add_session(s1)
conf.add_session(s2)

# Create attendees
a1 = Attendee("Kumar", "kumar@email.com")
a2 = Attendee("Latha", "latha@email.com")

# Register attendees
r1 = Registration(a1, s1)
r2 = Registration(a2, s2)
r3 = Registration(a1, s2)  # same attendee for another session

# Show total attendees
print(f"👥 Total Registrations: {Registration.get_total_attendees()}")
print("📋 All Registrations:")
for record in Registration.list_all():
    print("  ", record)

# Show sessions
print("\n📅 Conference Sessions:")
conf.show_sessions()
