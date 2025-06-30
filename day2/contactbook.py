import os 
contacts =[]


def load_contacts():
    if os.path.exists("contacts.txt")and os.stat("contacts.txt").st_size > 0:
       with open("contacts.txt","r") as file:
          for line in file:
              saved= line.strip().split("   ") 
              try:
                  name = saved[0].split(" : ")[1].strip()
                  number = saved[1].split(" : ")[1].strip()
              except IndexError:
                  continue  
              contacts.append({ "name": name, "number" : number})

load_contacts()
print(contacts)

def add_contact(name, number):
    for contact in contacts:
        if contact["name"] == name:
            print(f"{name} already exists.")
            return
    contacts.append({"name": name, "number": number})
    with open("contacts.txt", 'a') as file:
        file.write(f"name : {name}   number : {number}\n")




def view_contact():
    print(f"--------- contacts ---------\n")
    for contact in contacts:
        print(f"name : {contact['name']:7}   number : {contact['number']:7}")


def search_contact(name):
    for contact in contacts:
        if contact["name"] == name:
            return contact['number']
    print(f"{name} doesn't exist")
    return -1

def delete_contact(name):
   for contact in contacts:
        if contact["name"] == name:
           contacts.remove(contact)
           overwrite_file()
           return
   print(f"{name} doesn't exist")
   return -1

def overwrite_file():
    with open("contacts.txt","w") as file:
        for contact in contacts:
           file.write(f"name : {contact['name']}   number : {contact['number']}\n")


print("---------------------------")
print("|       Contact Book      |")
print("---------------------------")


print("1. Add Contact")
print("2. View all Contact")
print("3. Search Contact")
print("4. Delete Contact")
print("5. Exit")

while True:
    try:
      option = int(input("Choose an option: "))
    except ValueError:
      print("Please enter a valid number.")
      option = -1
    match option:
        case 1:
           name = input("enter the name: ")
           number = input("enter the number: ")
           add_contact(name,number)
        case 2:
            view_contact()
        case 3:
            name = input("Enter the name to search: ")
            number = search_contact(name)
            if number != -1 :
               print(f"name : {name}   number : {number}")

        case 4:
            name = input("Enter the name to delete: ")
            delete_contact(name)
        case 5:
            print("thanks for using the program :)")
            break
