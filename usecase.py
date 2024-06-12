class Bank:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance

    def verify_pin(self, entered_pin):
        return entered_pin == self.pin
# function to withdrawal of money
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
            return

        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal successful: ${amount}")
            self.display_balance()
        else:
            print("Insufficient balance.")
#function to deposit the money
    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount.")
            return

        self.balance += amount
        print(f"Deposit successful: ${amount}")
        self.display_balance()
#function to display the balance
    def display_balance(self):
        print(f"Current Balance: ${self.balance}")

#given input
bank = Bank(pin="2612", balance=8000)

#conditional statements to get the money

entered_pin = input("Enter your ATM PIN: ")
if bank.verify_pin(entered_pin):
    print("PIN verified successfully.")
    print("1. Withdrawal")
    print("2. Deposit")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        withdrawal_amount = float(input("Enter withdrawal amount: $"))
        bank.withdraw(withdrawal_amount)
    elif choice == "2":
        deposit_amount = float(input("Enter deposit amount: $"))
        bank.deposit(deposit_amount)
    else:
        print("Invalid choice.")
else:
    print("Invalid PIN. Access denied.")