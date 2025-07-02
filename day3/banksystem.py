from account import Account

class Banksystem :

    def __init__(self):
        self.account_dect = []
    
    def create_account(self,name):
        acc = Account(name)
        self.account_dect.append(acc)
        print(f"Account for {name} created successfully.")

    def find_account(self , name):
        for account in self.account_dect:
            if account.name == name :
                return account
        return None
    
    def deposit_money(self,name,amount):
        acc = self.find_account(name)
        if acc!= None :
            acc.deposit(amount)
            print("Deposit successful.")
        else:
             print(f"{name} doesn't exist.")


    def withdraw_money(self,name,amount):
        acc = self.find_account(name)
        if acc!= None :
            result= acc.withdraw(amount)
            if  result !=-1:
               print("Withdraw successful.")
        else:
             print(f"{name} doesn't exist.")

    def transfer_money(self,name,amount,otheracc):
        acc = self.find_account(name)
        receiver = self.find_account(otheracc)
        if acc!= None and receiver!= None:
            result= acc.transfer(amount,receiver)
            if result!= -1:
               print("transfer successful.")
        elif acc == None :
            print(f"{name} doesn't exist.")
        elif receiver == None :
            print(f"{otheracc} doesn't exist.")
