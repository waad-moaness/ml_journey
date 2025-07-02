from banksystem import Banksystem

print("---------------------------------")
print("|      Welcome to Waad's bank    |")
print("---------------------------------")

bank = Banksystem()

print("1. Create Account")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Transfer Money")
print("5. View Account Details")
print("6. View Transaction History")
print("7. Exit")

while True:
    try:
      option = int(input("Choose an option: "))
    except ValueError:
      print("Please enter a valid number.")
      option = -1
    match option:
        case 1:
            name = input("enter your name: ")
            bank.create_account(name)
        case 2:
            name = input("enter your name: ")
            amount = int(input("enter the amount: "))
            bank.deposit_money(name,amount)
        case 3:
           name = input("enter your name: ")
           amount = int(input("enter the amount: "))
           bank.withdraw_money(name,amount)
        case 4:
            name = input("enter your name: ")
            athername = input("enter the resiver name: ")
            amount = int(input("enter the amount: "))
            bank.transfer_money(name,amount,athername)
        case 5:
            name = input("Enter your name: ")
            acc = bank.find_account(name)
            if acc:
               print(acc) 
        case 6:
            name = input("Enter your name: ")
            acc = bank.find_account(name)
            if acc:
               print("---------account history----------")
               acc.show_acc_history()
               print("---------transaction hestory----------")
               acc.show_tranaction_history()

        case 7:
            print("thanks for using the program :)")
            break
