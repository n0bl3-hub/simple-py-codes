shopping_list = []
list("car, bus, train")
def show_menu():
    print("\n1. add item")
    print("2. remove item")
    print("3. view list")
    print("4. exit")

def add_item():
    item = input("enter item to add:")
    shopping_list.append(item)
    print(f"{item} added to the list.")    
def remove_item():
    item = input("enter item to remove:")
    if item in shopping_list:
        shopping_list.remove(item) 
        print(f"{item} not found in the list.")
    else:
        print(f"{item} not found in the list")

def view_list():
    if shopping_list:
        print("\nshopping list.")
        for item in shopping_list:
            print(f"-{item}")
    else:
        print("the list is empty")
while True:
    show_menu()
    choice = input("choose an option:")
    if choice == "1":
        add_item()
    elif choice == "2":
        remove_item
    elif choice == "3":
        view_list()
    elif choice == "4":
        print("good bye!")
        break
    else:
        print("invalid option. please try again.")


            
    
