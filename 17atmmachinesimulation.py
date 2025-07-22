# Transaction class (optional)
class Transaction:
    def __init__(self, txn_type, amount, note=""):
        self.txn_type = txn_type
        self.amount = amount
        self.note = note

    def __str__(self):
        return f"{self.txn_type}: ₹{self.amount} {self.note}"
        

# Account class with encapsulation
class Account:
    def __init__(self, name, pin, initial_balance=0):
        self.name = name
        self.__pin = pin
        self.__balance = initial_balance
        self.transactions = []

    def __authenticate(self, pin):
        return self.__pin == pin

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.transactions.append(Transaction("Deposit", amount))
            return True
        return False

    def withdraw(self, *args):
        # Method overloading simulated using *args
        if len(args) == 2:
            amount, note = args
        elif len(args) == 1:
            amount, note = args[0], ""
        else:
            raise ValueError("Invalid withdraw call")

        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.transactions.append(Transaction("Withdraw", amount, note))
            return True
        else:
            return False

    def get_balance(self, pin):
        if self.__authenticate(pin):
            return self.__balance
        else:
            return "❌ Invalid PIN"

    def get_statement(self, pin):
        if self.__authenticate(pin):
            return [str(txn) for txn in self.transactions]
        else:
            return ["❌ Invalid PIN"]

    def validate_pin(self, pin):
        return self.__authenticate(pin)

# ATM machine using static method
class ATM:
    @staticmethod
    def authenticate(account, pin):
        return account.validate_pin(pin)

    def __init__(self, account):
        self.account = account

    def show_balance(self, pin):
        return self.account.get_balance(pin)

    def deposit(self, amount):
        if self.account.deposit(amount):
            return "✅ Deposit successful"
        return "❌ Invalid amount"

    def withdraw(self, *args):
        if self.account.withdraw(*args):
            return "✅ Withdrawal successful"
        return "❌ Insufficient balance or invalid request"

# Create account
acc1 = Account("Raj", pin=4321, initial_balance=5000)
atm = ATM(acc1)

# Authenticate
if ATM.authenticate(acc1, 4321):
    print(atm.show_balance(4321))  # ✅ Show balance
    print(atm.deposit(1500))       # ✅ Deposit
    print(atm.withdraw(2000))      # ✅ Withdraw with 1 arg
    print(atm.withdraw(500, "Grocery"))  # ✅ Withdraw with 2 args
    print(atm.show_balance(4321))  # ✅ Final balance
    print("📄 Statement:")
    for line in acc1.get_statement(4321):
        print(" ", line)
else:
    print("❌ Invalid PIN")
