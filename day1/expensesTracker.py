categories={}

def add_category(category,amount):
    if category in categories:
        categories[category]+=amount  # updates the value directly
    else:
        categories[category] =amount
    #   this was my original approch but chat said that the later is more clear and pythonic 
    #   so i update it but this still does work so that's that  
    # if category in categories:
    #     amount += categories.get(category)
    # categories.update({category: amount})

def show_expenses():
    for key , value in categories.items():
        print(f"{key}: {value:.2f}")

def total_spent():
    total=0.0
    for value in categories.values():
        total+=value
    return total
print("---------------------------")
print("|     expenses tracker    |")
print("---------------------------")


print("1. Add Expense")
print("2. Show All Expenses")
print("3. Show Total Spent")
print("4. Exit")

while True:
    option =int(input("Choose an option: "))
    match option:
        case 1:
            category=input("Enter category: ")
            price=int(input("Enter amount: "))
            add_category(category,price)
        case 2:
            print("All Expenses: ")
            show_expenses()
        case 3:
            total=  total_spent()
            print(f"Total Spent: {total:.2f}")
            
        case 4:
            print("thanks for using the program :)")
            break