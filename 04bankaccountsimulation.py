# Base Account class
class Account:
    def __init__(self, name, account_number, initial_balance=0):
        self.name = name
        self.account_number = account_number
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited into {self.account_number}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn from {self.account_number}")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"{self.name} (Acc: {self.account_number}) - Balance: ₹{self.__balance:.2f}"

# Savings Account with overridden withdrawal limit
class SavingsAccount(Account):
    def withdraw(self, amount):
        if amount > 25000:
            print("SavingsAccount: Withdrawal limit ₹25,000 exceeded")
        else:
            super().withdraw(amount)

# Current Account with higher limit
class CurrentAccount(Account):
    def withdraw(self, amount):
        if amount > 100000:
            print("CurrentAccount: Withdrawal limit ₹1,00,000 exceeded")
        else:
            super().withdraw(amount)

# Transaction class to handle transfers
class Transaction:
    @staticmethod
    def transfer(from_account, to_account, amount):
        print(f"\n💸 Transferring ₹{amount} from {from_account.account_number} to {to_account.account_number}")
        if from_account.get_balance() >= amount:
            from_account.withdraw(amount)
            to_account.deposit(amount)
            print("✅ Transfer complete")
        else:
            print("❌ Transfer failed: Insufficient funds")


# Create accounts
acc1 = SavingsAccount("Arun", "SA123", 50000)
acc2 = CurrentAccount("Divya", "CA456", 100000)

# Operations
acc1.deposit(5000)
acc1.withdraw(20000)     # OK
acc1.withdraw(30000)     # Exceeds limit

acc2.withdraw(95000)     # OK
acc2.withdraw(150000)    # Exceeds limit

# Transfer between accounts
Transaction.transfer(acc2, acc1, 10000)  # From Current to Savings
Transaction.transfer(acc1, acc2, 70000)  # Fail - insufficient funds

# Final balances
print("\n📄 Final Account Status")
print(acc1)
print(acc2)
