class Account :
    def __init__(self,name):
        self.name = name
        self.balance =0
        self.tranaction_history = []
        self.acc_history = []


    def deposit(self,amount):
        self.balance += amount 
        self.acc_history.append(f"Deposited ${amount}")

    def withdraw(self,amount):
        if amount > self.balance:
          print("Insufficient funds.")
          return -1
        self.balance -= amount 
        self.acc_history.append(f"Withdrawn ${amount}")
    
    def transfer(self,amount, other_account):
        if amount > self.balance:
           print("Insufficient funds.")
           return -1
        self.balance -= amount
        other_account.balance += amount
        self.tranaction_history.append({"From":self.name , "To" : other_account.name , "Amount" : amount})


    def show_balance(self):
           return F"Balance : {self.balance}" 
    
    def show_tranaction_history(self):
           for transaction in self.tranaction_history:
                print(f"From:{transaction['From'] }\nTO: {transaction['To'] } \nAmount: {transaction['Amount'] }")
                print("------------------------------")
           print("------------------------------------------------------------------------")

    def show_acc_history(self):
           for action in self.acc_history:
                print(action)
                print("------------------------------")
           print("------------------------------------------------------------------------")

    
    def __str__(self):
         return f"Name:{self.name }\nBalance: {self.balance} "

    def __eq__(self, other):
        if isinstance(other, Account):
           return self.name == other.name
        return False
