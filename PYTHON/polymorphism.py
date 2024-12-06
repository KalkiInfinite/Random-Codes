class Account:
    def __init__(self, customer_name, account_number, account_type):
        self.customer_name = customer_name
        self.account_number = account_number
        self.account_type = account_type
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} into account. New balance: {self.balance}")

    def display_balance(self):
        print(f"Current balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            print(f"Withdrew {amount} from account. New balance: {self.balance}")
        else:
            print("Insufficient funds.")

class CurrentAccount(Account):
    MIN_BALANCE = 1000

    def compute_interest(self):
        interest = self.balance * 0.05  # 5% interest rate
        self.balance += interest
        print(f"Computed and deposited {interest} interest. New balance: {self.balance}")

    def check_minimum_balance(self):
        if self.balance < self.MIN_BALANCE:
            penalty = self.MIN_BALANCE - self.balance
            self.balance -= penalty
            print(f"Imposed a penalty of {penalty} due to low balance. New balance: {self.balance}")

class SavingsAccount(Account):
    MIN_BALANCE = 5000

    def compute_interest(self):
        interest = self.balance * 0.08  # 8% interest rate
        self.balance += interest
        print(f"Computed and deposited {interest} interest. New balance: {self.balance}")

    def check_minimum_balance(self):
        if self.balance < self.MIN_BALANCE:
            penalty = self.MIN_BALANCE - self.balance
            self.balance -= penalty
            print(f"Imposed a penalty of {penalty} due to low balance. New balance: {self.balance}")

current_account = CurrentAccount("John Doe", "12345", "Current")
current_account.deposit(2000)
current_account.display_balance()
current_account.withdraw(1500)
current_account.compute_interest()
current_account.check_minimum_balance()

savings_account = SavingsAccount("Jane Smith", "54321", "Savings")
savings_account.deposit(10000)
savings_account.display_balance()
savings_account.withdraw(8000)
savings_account.compute_interest()
savings_account.check_minimum_balance()