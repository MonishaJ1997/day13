# Base Person class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Trainer class
class Trainer(Person):
    def __init__(self, name, age, specialty):
        super().__init__(name, age)
        self.specialty = specialty

    def __str__(self):
        return f"{self.name} ({self.specialty})"

# Member class with class variable and *args
class Member(Person):
    total_members = 0  # class variable

    def __init__(self, name, age):
        super().__init__(name, age)
        self.sessions = []
        Member.total_members += 1  # increment count

    def register_sessions(self, *sessions):
        for s in sessions:
            self.sessions.append(s)
        print(f"✅ {self.name} registered for {len(sessions)} session(s).")

    def __str__(self):
        return f"{self.name} (Age: {self.age})"

# Schedule class
class Schedule:
    def __init__(self, time_slot, session_name):
        self.time_slot = time_slot
        self.session_name = session_name

    def __str__(self):
        return f"{self.session_name} at {self.time_slot}"

# Subscription class to assign trainer
class Subscription:
    def __init__(self, member, trainer):
        self.member = member
        self.trainer = trainer

    def show_details(self):
        print(f"📋 Subscription Info")
        print(f"Member: {self.member}")
        print(f"Trainer: {self.trainer}")
        print("Sessions:")
        for s in self.member.sessions:
            print(f" - {s}")

# Create trainer
trainer1 = Trainer("Raj", 35, "Cardio")
trainer2 = Trainer("Anu", 28, "Strength")

# Create schedule sessions
s1 = Schedule("6 AM", "Yoga")
s2 = Schedule("7 AM", "Crossfit")
s3 = Schedule("8 AM", "Zumba")

# Create member and register sessions
m1 = Member("Kiran", 25)
m1.register_sessions(s1, s3)

m2 = Member("Deepa", 32)
m2.register_sessions(s2)

# Assign subscriptions
sub1 = Subscription(m1, trainer1)
sub2 = Subscription(m2, trainer2)

# Show subscription details
sub1.show_details()
print()
sub2.show_details()

# Total members
print(f"\n🏋️ Total Gym Members: {Member.total_members}")
