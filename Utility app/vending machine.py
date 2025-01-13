#vending machine drinks nested dictionary
VM_DRINKS = {'A1': {'name' : 'Orange Fizzy Drink', 'price' : 8, 'stock' : 5 },
             'A2': {'name' : 'Grape Fizzy Drink', 'price' : 8, 'stock' : 5},
             'A3': {'name' : 'Chocolate Milk', 'price' : 2, 'stock' : 3},
             'B1': {'name' : 'Strawberry Milk', 'price' : 2, 'stock' : 4},
             'B2': {'name' : 'Mango Juicebox', 'price' : 2, 'stock' : 5},
             'B3': {'name' : 'Apple Juicebox', 'price' : 2, 'stock' : 4}
             }

#vending machine snacks nested dictionary
VM_SNACKS = {'C1': {'name' : 'Chocolate Biscuits', 'price' : 3, 'stock' : 5 },
             'C2': {'name' : 'Vanilla Biscuits', 'price' : 3, 'stock' : 5},
             'C3': {'name' : 'Strawberry Biscuits', 'price' : 3, 'stock' : 3},
             'D1': {'name' : 'Salty Chips', 'price' : 3, 'stock' : 4},
             'D2': {'name' : 'Cheesy Chips', 'price' : 3, 'stock' : 5},
             'D3': {'name' : 'Spicy Chips', 'price' : 3, 'stock' : 4}
             }

#Display greeting/art
print ("""
██╗░░░██╗███████╗███╗░░██╗██████╗░██╗███╗░░██╗░██████╗░
██║░░░██║██╔════╝████╗░██║██╔══██╗██║████╗░██║██╔════╝░
╚██╗░██╔╝█████╗░░██╔██╗██║██║░░██║██║██╔██╗██║██║░░██╗░
░╚████╔╝░██╔══╝░░██║╚████║██║░░██║██║██║╚████║██║░░╚██╗
░░╚██╔╝░░███████╗██║░╚███║██████╔╝██║██║░╚███║╚██████╔╝
░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░

███╗░░░███╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗███████╗██╗
████╗░████║██╔══██╗██╔══██╗██║░░██║██║████╗░██║██╔════╝██║
██╔████╔██║███████║██║░░╚═╝███████║██║██╔██╗██║█████╗░░██║
██║╚██╔╝██║██╔══██║██║░░██╗██╔══██║██║██║╚████║██╔══╝░░╚═╝
██║░╚═╝░██║██║░░██║╚█████╔╝██║░░██║██║██║░╚███║███████╗██╗
╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝╚═╝""")

print("\n")
print('------This is what we have to offer------')
print("\n")

#function to display vending machine list properly
def print_display(header, section):
    print(f"{header}")
    print("-" * 50)
    print(f"{'ID':<10} {'Name':<25} {'Price':<10} {'Stock'}")
    print("-" * 50)
#for loop to print table rows neatly
    for ID, specifics in section.items():
        print(f"{ID:<10} {specifics['name']:<25} AED{specifics['price']:<10} {specifics['stock']}")
    
    print("\n")

#print for vending machine drinks
print_display("Vending Machine Drinks", VM_DRINKS)

#print for vending machine snacks
print_display("Vending Machine Snacks", VM_SNACKS)

#Function for user purchase
def user_purchase(code, money, section):
    if code in section:
        item = section[code]
        if item['stock'] > 0:
            if money >= item['price']:
                item['stock'] -= 1
                user_change = money - item['price'] 
                print(f"{item['name']} has been dispensed.") #dispensed item message
                print(f"Your change: AED{user_change}") #user change return message
            else:
                print("Not enough money has been inserted.") #insufficient funds error
        else:
            print("Item is out of stock.") #insufficient stock error
    else:
        print("This code doesn't exist.") #unavailable item code error


#function to start the vending machine program
def start_app():
    print("""
    1. Insert money and buy an item
    2. Exit vending machine""") #user vending machine options
    print('\n')
    while True:
        option = input("What do you want to do? (1 or 2): ")
        if option == '1':
            code = input("Please enter the code of the item you want: ").upper() #user code input
            if code in VM_DRINKS or code in VM_SNACKS:
                section = VM_DRINKS if code in VM_DRINKS else VM_SNACKS
                item = section[code]
                if item['stock'] > 0:
                    money = input("Insert money here (AED): ") #user purchase input
                    if money.isdigit():
                        money = int(money)
                        if money > 0:
                            user_purchase(code, money, section)
                        else:
                            print("Sorry! Not enough money.") #insufficient funds error 
                    else:
                        print("Error! Invalid number. Please try again.") #invalid funds error
                else:
                    print("Item is out of stock.") #insufficient stock error
            else:
                print("Error! That's not an existing code, please try again.") #invalid item code error
        elif option == '2':
            print("Exited.") #exit message
            break
        else:
            print("That's not an option.") #invalid option error

#run the program
start_app()