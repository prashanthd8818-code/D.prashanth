class BankAccount:
    
    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance
        
    def Deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount Deposited.")
        else:
            print("Invalid amount.")
            
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
            
        elif amount > self.balance:
            print("Insufficient balance.")
            
        else:
            self.balance -= amount
            print("Amount withdrawn.")
    
    def show_balance(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)
        
    def show_balance(self):
        print("balance:", self.balance)
        
name = input("enter your name:")

account = BankAccount(name)

while True:
    print("\n--- BANKING SYSTEM ---")
    print("1. Deposit")
    print("2. withdraw")
    print("3. check balance")
    print("4. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        amount = float(input("Enter amount: "))
        account.Deposit(amount)
        
    elif choice == "2":
        amount = float(input("Enter amount: "))
        account.withdraw(amount)
        
    elif choice == "3":
        account.show_balance()
        
    elif choice == "4":
        break   