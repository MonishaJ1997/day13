# Base Employee class
class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def calculate_salary(self):
        raise NotImplementedError("Subclasses must override this method.")

    def __str__(self):
        return f"{self.emp_id} - {self.name}"

# Full-time employee subclass
class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, daily_rate, days_worked):
        super().__init__(emp_id, name)
        self.daily_rate = daily_rate
        self.days_worked = days_worked

    def calculate_salary(self):
        return self.daily_rate * self.days_worked

# Part-time employee subclass
class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        super().__init__(emp_id, name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

# Payroll class
class Payroll:
    @staticmethod
    def calculate_tax(gross_salary):
        if gross_salary <= 10000:
            return 0
        elif gross_salary <= 20000:
            return gross_salary * 0.1
        else:
            return gross_salary * 0.2

    def process_payroll(self, employees):
        print("📋 Payroll Summary:")
        for emp in employees:
            gross = emp.calculate_salary()
            tax = Payroll.calculate_tax(gross)
            net = gross - tax
            print(f"\n🧑 {emp}")
            print(f"   Gross Salary: ₹{gross}")
            print(f"   Tax Deducted: ₹{tax}")
            print(f"   Net Pay: ₹{net}")

# Sample employees
emp1 = FullTimeEmployee(101, "Suresh", daily_rate=800, days_worked=25)
emp2 = PartTimeEmployee(102, "Meena", hourly_rate=150, hours_worked=60)
emp3 = FullTimeEmployee(103, "Kumar", daily_rate=1000, days_worked=20)

# Process payroll
payroll = Payroll()
payroll.process_payroll([emp1, emp2, emp3])
