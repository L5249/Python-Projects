class BankAccount: 
    def __init__(self, account_id, name, balance = 0.0):
        self.account_id = account_id
        self.name = name 
        self.balance = balance
    
    def deposit(self,amount):
        if amount <= 0: 
            print("Amount must be greater than zero")
        else:
            self.balance += amount
            print(f"Amount deposited: £{amount}. New Balance: £{self.balance}")
    
    def withdraw(self,amount):
        if amount <= 0: 
            print("Amount must be greater than zero")
        else:
            self.balance -= amount
            print(f"Amount deposited: £{amount}. New Balance: £{self.balance}")
    
    def get_balance(self):
        print(f"Current Balance: £{self.balance}")
    
    def display_account_info(self):
        print(f"Account ID: {self.account_id}\nName: {self.name}\nBalance: £{self.balance}")
    
bank1 = BankAccount(1,"Lewis",100.50)
bank1.display_account_info()
