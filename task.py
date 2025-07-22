# Task 1: Car Class
class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: ₹{self.price}")

car1 = Car("Toyota", "Innova", 2500000)
car2 = Car("Honda", "City", 1500000)
car1.display()
car2.display()
print("-" * 50)

# Task 2: BankAccount Class
class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited. Current balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn. Remaining balance: ₹{self.balance}")
        else:
            print("Insufficient balance!")

    def check_balance(self):
        return self.balance

account = BankAccount("Ganesh")
account.deposit(1000)
account.withdraw(400)
print("Final Balance:", account.check_balance())
print("-" * 50)

# Task 3: Student Class
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

student = Student("Ravi", 16, "10th")
print(f"Name: {student.name}, Age: {student.age}, Grade: {student.grade}")
print("-" * 50)

# Task 4: Circle Class
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

circle = Circle(5)
print("Area:", circle.area())
print("Circumference:", circle.circumference())
print("-" * 50)

# Task 5: Book Class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")

book = Book("Python Basics", "John Doe")
book.display_info()
print("-" * 50)

# Task 6: Laptop Class with Class Variable
class Laptop:
    warranty_period = "2 years"  # Class variable

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

l1 = Laptop("Dell", "Inspiron")
l2 = Laptop("HP", "Pavilion")
print(l1.brand, l1.model, "Warranty:", l1.warranty_period)
print(l2.brand, l2.model, "Warranty:", l2.warranty_period)
print("-" * 50)

# Task 7: Movie Class with Instance Count
class Movie:
    count = 0

    def __init__(self, title):
        self.title = title
        Movie.count += 1

m1 = Movie("Inception")
m2 = Movie("Interstellar")
print("Total movies created:", Movie.count)
print("-" * 50)

# Task 8: Product Class - Instance vs Class Variable
class Product:
    tax = 0.18  # Class variable

    def __init__(self, name, price):
        self.name = name
        self.price = price

p1 = Product("Shampoo", 120)
p2 = Product("Soap", 40)
print(f"{p1.name}: ₹{p1.price}, Tax: {Product.tax}")
print(f"{p2.name}: ₹{p2.price}, Tax: {Product.tax}")
print("-" * 50)

# Task 9: Employee Class with __str__
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __str__(self):
        return f"Employee Name: {self.name}, Position: {self.position}"

e = Employee("Sita", "Manager")
print(e)
print("-" * 50)

# Task 10: Rectangle Class with __eq__
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def __eq__(self, other):
        return self.length == other.length and self.breadth == other.breadth

r1 = Rectangle(10, 5)
r2 = Rectangle(10, 5)
r3 = Rectangle(8, 6)
print("r1 == r2:", r1 == r2)
print("r1 == r3:", r1 == r3)


# Task 11: Vehicle base class and Car, Bike, Truck subclasses
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show(self):
        print(f"Vehicle Brand: {self.brand}")

class Car(Vehicle):
    def drive(self):
        print("Driving a car.")

class Bike(Vehicle):
    def drive(self):
        print("Riding a bike.")

class Truck(Vehicle):
    def drive(self):
        print("Driving a truck.")

c = Car("Toyota")
b = Bike("Honda")
t = Truck("Tata")

c.show(); c.drive()
b.show(); b.drive()
t.show(); t.drive()
print("-" * 50)

# Task 12: Using super() in child class
class Animal:
    def __init__(self, species):
        self.species = species
        print(f"Animal: {self.species}")

class Dog(Animal):
    def __init__(self, breed):
        super().__init__("Dog")  # call parent constructor
        self.breed = breed
        print(f"Breed: {self.breed}")

d = Dog("Labrador")
print("-" * 50)

# Task 13: Shape with method overriding in Square and Triangle
class Shape:
    def area(self):
        print("Calculating area...")

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

s = Square(4)
t = Triangle(3, 6)
print("Square Area:", s.area())
print("Triangle Area:", t.area())
print("-" * 50)

# Task 14: Multi-level Inheritance: Person → Employee → Manager
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department

    def show(self):
        print(f"Manager: {self.name}, ID: {self.emp_id}, Dept: {self.department}")

m = Manager("Priya", 101, "HR")
m.show()
print("-" * 50)

# Task 15: Multiple Inheritance
class Father:
    def skills(self):
        print("Father: Driving, Cooking")

class Mother:
    def skills(self):
        print("Mother: Painting, Singing")

class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Child: Coding")

c = Child()
c.skills()
print("-" * 50)

# Task 16: Hierarchical Inheritance: Teacher → MathTeacher, ScienceTeacher
class Teacher:
    def teach(self):
        print("Teaching subjects...")

class MathTeacher(Teacher):
    def subject(self):
        print("Teaches Mathematics.")

class ScienceTeacher(Teacher):
    def subject(self):
        print("Teaches Science.")

m = MathTeacher()
s = ScienceTeacher()
m.teach(); m.subject()
s.teach(); s.subject()
print("-" * 50)

# Task 17: Using isinstance()
class Animal:
    pass

class Cat(Animal):
    pass

kitty = Cat()
print("Is kitty an instance of Cat?", isinstance(kitty, Cat))
print("Is kitty an instance of Animal?", isinstance(kitty, Animal))
print("-" * 50)

# Task 18: Using issubclass()
print("Is Cat subclass of Animal?", issubclass(Cat, Animal))
print("Is Animal subclass of Cat?", issubclass(Animal, Cat))
print("-" * 50)

# Task 19: E-commerce Product hierarchy
class Product:
    def __init__(self, name):
        self.name = name

class ElectronicProduct(Product):
    def __init__(self, name, warranty):
        super().__init__(name)
        self.warranty = warranty

class MobilePhone(ElectronicProduct):
    def __init__(self, name, warranty, brand):
        super().__init__(name, warranty)
        self.brand = brand

    def details(self):
        print(f"Product: {self.name}, Brand: {self.brand}, Warranty: {self.warranty} years")

phone = MobilePhone("Smartphone", 2, "Samsung")
phone.details()
print("-" * 50)

# Task 20: Method Resolution Order (MRO)
class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):  # MRO: D → B → C → A
    pass

obj = D()
obj.show()
print("MRO of class D:", [cls.__name__ for cls in D.__mro__])

# Task 21: Student class with private attributes and getter/setter
class Student:
    def __init__(self, name, marks):
        self._name = name
        self._marks = marks

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_marks(self):
        return self._marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self._marks = marks
        else:
            print("Invalid marks. Must be between 0 and 100.")

s = Student("Ravi", 85)
print("Name:", s.get_name())
print("Marks:", s.get_marks())
s.set_marks(95)
print("Updated Marks:", s.get_marks())
print("-" * 50)

# Task 22: BankAccount with private balance
class BankAccount:
    def __init__(self, owner):
        self.__balance = 0
        self.owner = owner

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.__balance

acc = BankAccount("Ganesh")
acc.deposit(1000)
acc.withdraw(300)
print("Balance:", acc.get_balance())
print("-" * 50)

# Task 23: UserProfile with email and phone, validation in setters
class UserProfile:
    def __init__(self):
        self.__email = None
        self.__phone = None

    def set_email(self, email):
        if "@" in email and "." in email:
            self.__email = email
        else:
            print("Invalid email format.")

    def get_email(self):
        return self.__email

    def set_phone(self, phone):
        if phone.isdigit() and len(phone) == 10:
            self.__phone = phone
        else:
            print("Invalid phone number. Must be 10 digits.")

    def get_phone(self):
        return self.__phone

u = UserProfile()
u.set_email("test@example.com")
u.set_phone("9876543210")
print("Email:", u.get_email())
print("Phone:", u.get_phone())
print("-" * 50)

# Task 24: Employee with private salary and access via getter/setter
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary >= 0:
            self.__salary = new_salary
        else:
            print("Salary can't be negative.")

emp = Employee("Meena", 30000)
print("Name:", emp.name)
print("Salary:", emp.get_salary())
emp.set_salary(35000)
print("Updated Salary:", emp.get_salary())
print("-" * 50)

# Task 25: Locker system with private PIN, changeable only through method
class Locker:
    def __init__(self, pin):
        self.__pin = pin

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            print("PIN changed successfully.")
        else:
            print("Incorrect old PIN.")

    def access(self, pin):
        if pin == self.__pin:
            print("Access granted.")
        else:
            print("Access denied.")

locker = Locker("1234")
locker.access("1234")
locker.change_pin("1234", "5678")
locker.access("5678")
print("-" * 50)

from abc import ABC, abstractmethod

# Task 26: Abstract class Payment with abstract method pay()
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")

class UpiPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")

cc = CreditCardPayment()
upi = UpiPayment()
cc.pay(500)
upi.pay(200)
print("-" * 50)

# Task 27: Abstract Shape with abstract method area() and concrete method describe()
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def describe(self):
        print("This is a geometric shape.")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rect = Rectangle(4, 5)
rect.describe()
print("Area:", rect.area())
print("-" * 50)

# Task 28: Abstract Animal class with abstract speak() method
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Dog says: Woof!")

class Cat(Animal):
    def speak(self):
        print("Cat says: Meow!")

d = Dog()
c = Cat()
d.speak()
c.speak()
print("-" * 50)

# Task 29: Transport template with abstract methods
class Transport(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Transport):
    def start_engine(self):
        print("Car engine started.")

    def stop_engine(self):
        print("Car engine stopped.")

vehicle = Car()
vehicle.start_engine()
vehicle.stop_engine()
print("-" * 50)

# Task 30: Appliance base class with power_consumption() as abstract
class Appliance(ABC):
    @abstractmethod
    def power_consumption(self):
        pass

class Fridge(Appliance):
    def power_consumption(self):
        return "Fridge consumes ~150W."

class WashingMachine(Appliance):
    def power_consumption(self):
        return "Washing Machine consumes ~500W."

f = Fridge()
w = WashingMachine()
print(f.power_consumption())
print(w.power_consumption())
print("-" * 50)

# Task 31: Method Overriding (Runtime Polymorphism)
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

a = Animal()
d = Dog()
a.speak()  # Output: Animal makes a sound
d.speak()  # Output: Dog barks
print("-" * 50)

# Task 32: Duck Typing Polymorphism (no inheritance required)
class Circle:
    def draw(self):
        print("Drawing a circle")

class Square:
    def draw(self):
        print("Drawing a square")

def render(shape):
    shape.draw()

c = Circle()
s = Square()
render(c)  # Duck typing: only needs draw()
render(s)
print("-" * 50)

# Task 33: Simulate Method Overloading using default arguments
class Calculator:
    def add(self, a=0, b=0, c=0):
        return a + b + c

calc = Calculator()
print("Add 2 numbers:", calc.add(10, 20))
print("Add 3 numbers:", calc.add(5, 15, 25))
print("Add 0 numbers:", calc.add())
print("-" * 50)

# Task 34: Simulate overloading using *args
class Sum:
    def add(self, *nums):
        return sum(nums)

s = Sum()
print("Sum of 2:", s.add(10, 20))
print("Sum of 3:", s.add(1, 2, 3))
print("Sum of many:", s.add(5, 10, 15, 20))
print("-" * 50)

# Task 35: Notification system using polymorphism
class Notification:
    def send(self, msg):
        print("Sending notification:", msg)

class SMS(Notification):
    def send(self, msg):
        print(f"SMS: {msg}")

class Email(Notification):
    def send(self, msg):
        print(f"Email: {msg}")

class PushNotification(Notification):
    def send(self, msg):
        print(f"Push Notification: {msg}")

def notify_user(notifier, message):
    notifier.send(message)

sms = SMS()
email = Email()
push = PushNotification()

notify_user(sms, "Your OTP is 123456")
notify_user(email, "Welcome to our platform!")
notify_user(push, "You have a new message")
print("-" * 50)

# Task 36: Override __add__ in a Vector class
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 1)
v3 = v1 + v2
print(v3)  # Output: Vector(6, 4)
print("-" * 50)

# Task 37: Override __len__ in a Playlist class
class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

p = Playlist(["Song A", "Song B", "Song C"])
print("Playlist length:", len(p))  # Output: 3
print("-" * 50)

# Task 38: __getitem__ and __setitem__ in ShoppingCart
class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def __getitem__(self, item):
        return self.cart.get(item, 0)

    def __setitem__(self, item, quantity):
        self.cart[item] = quantity

    def __str__(self):
        return str(self.cart)

shop = ShoppingCart()
shop["apple"] = 3
shop["banana"] = 2
print("Apples in cart:", shop["apple"])
print("Full cart:", shop)
print("-" * 50)

# Task 39: Override __contains__ in Inventory
class Inventory:
    def __init__(self, items):
        self.items = items

    def __contains__(self, item):
        return item in self.items

inv = Inventory(["pen", "notebook", "eraser"])
print("pen" in inv)        # True
print("pencil" in inv)     # False
print("-" * 50)

# Task 40: Money class with __eq__, __gt__, __lt__
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __gt__(self, other):
        return self.amount > other.amount

    def __lt__(self, other):
        return self.amount < other.amount

    def __str__(self):
        return f"₹{self.amount}"

m1 = Money(500)
m2 = Money(300)
m3 = Money(500)

print(f"m1 == m2? {m1 == m2}")
print(f"m1 > m2? {m1 > m2}")
print(f"m2 < m1? {m2 < m1}")
print(f"m1 == m3? {m1 == m3}")
print("-" * 50)


# Task 41: Car class using Composition with Engine
class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition

    def drive(self):
        self.engine.start()
        print("Car is moving.")

car = Car()
car.drive()
print("-" * 50)

# Task 42: Library class with Book objects (Aggregation)
class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self, books):
        self.books = books  # Aggregation

    def display_books(self):
        for book in self.books:
            print("Book:", book.title)

b1 = Book("Python Basics")
b2 = Book("OOP Concepts")
lib = Library([b1, b2])
lib.display_books()
print("-" * 50)

# Task 43: University with Department objects (Composition)
class Department:
    def __init__(self, name):
        self.name = name

class University:
    def __init__(self):
        self.departments = [Department("CS"), Department("Maths")]  # Composition

    def show_departments(self):
        for dept in self.departments:
            print("Department:", dept.name)

uni = University()
uni.show_departments()
print("-" * 50)

# Task 44: Company with aggregated Employee instances
class Employee:
    def __init__(self, name):
        self.name = name

class Company:
    def __init__(self, employees):
        self.employees = employees  # Aggregation

    def list_employees(self):
        for emp in self.employees:
            print("Employee:", emp.name)

e1 = Employee("John")
e2 = Employee("Alice")
comp = Company([e1, e2])
comp.list_employees()
print("-" * 50)

# Task 45: Flight with Pilot, CabinCrew, Passenger
class Pilot:
    def __init__(self, name):
        self.name = name

class CabinCrew:
    def __init__(self, name):
        self.name = name

class Passenger:
    def __init__(self, name):
        self.name = name

class Flight:
    def __init__(self, pilot, crew_list, passengers):
        self.pilot = pilot
        self.crew_list = crew_list
        self.passengers = passengers

    def flight_info(self):
        print("Pilot:", self.pilot.name)
        print("Crew:", [c.name for c in self.crew_list])
        print("Passengers:", [p.name for p in self.passengers])

flight = Flight(
    Pilot("Captain Ravi"),
    [CabinCrew("Kiran"), CabinCrew("Meena")],
    [Passenger("Rahul"), Passenger("Priya")]
)
flight.flight_info()
print("-" * 50)


# Task 46: Banking System
class Customer:
    def __init__(self, name):
        self.name = name

class Account:
    def __init__(self, acc_no, balance=0):
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

class Transaction:
    def __init__(self, account):
        self.account = account

    def perform(self, type, amount):
        if type == "deposit":
            self.account.deposit(amount)
        elif type == "withdraw":
            self.account.withdraw(amount)

acc = Account(12345, 1000)
txn = Transaction(acc)
txn.perform("deposit", 500)
txn.perform("withdraw", 200)
print(f"Account Balance: ₹{acc.balance}")
print("-" * 50)

# Task 47: Quiz Application
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

class Option:
    def __init__(self, choices):
        self.choices = choices

class Quiz:
    def __init__(self, questions):
        self.questions = questions

    def start(self):
        score = 0
        for q in self.questions:
            print(q.text)
            ans = input("Your answer: ")
            if ans.lower() == q.answer.lower():
                score += 1
        print("Score:", score)

# q1 = Question("Capital of India?", "Delhi")
# quiz = Quiz([q1])
# quiz.start()  # Uncomment to run
print("Quiz setup ready (commented to avoid input interruption).")
print("-" * 50)

# Task 48: Hotel Management System
class Room:
    def __init__(self, number):
        self.number = number
        self.is_booked = False

class Booking(Room):
    def book(self):
        if not self.is_booked:
            self.is_booked = True
            print(f"Room {self.number} booked.")
        else:
            print("Already booked.")

class Customer(Booking):
    def __init__(self, name, number):
        super().__init__(number)
        self.name = name

cust = Customer("Arun", 101)
cust.book()
print("-" * 50)

# Task 49: School Management System
from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def role(self): pass

class Teacher(Person):
    def role(self):
        return "Teaching"

class Student(Person):
    def role(self):
        return "Learning"

class Course:
    def __init__(self, name):
        self.name = name

class Grade:
    def __init__(self, student, grade):
        self.student = student
        self.grade = grade

teacher = Teacher()
student = Student()
print("Teacher Role:", teacher.role())
print("Student Role:", student.role())
print("-" * 50)

# Task 50: Library System
class Book:
    def __init__(self, title):
        self.title = title
        self.available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        self.books.append(Book(title))

    def borrow(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print(f"{title} borrowed.")
                return
        print("Book not available.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.available = True
                print(f"{title} returned.")
                return

    def search(self, title):
        found = any(book.title == title for book in self.books)
        print(f"{title} found: {found}")

lib = Library()
lib.add_book("Python 101")
lib.borrow("Python 101")
lib.return_book("Python 101")
lib.search("Python 101")
print("-" * 50)
