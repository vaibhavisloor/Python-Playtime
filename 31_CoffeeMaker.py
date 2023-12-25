MENU = {
    "Espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 150,
    },
    "Latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 250,
    },
    "Cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300,
    }
}


profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def order_placed(choice):
    value_of_order = MENU[choice]['cost']
    print(f"Your bill is {value_of_order}")
    money = int(input("Please enter the money : ₹ "))

    if money == value_of_order:
        resources['water']-=MENU[choice]['ingredients']['water']
        resources['milk']-=MENU[choice]['ingredients']['milk']
        resources['coffee']-=MENU[choice]['ingredients']['coffee']
        print("Your order has been placed.")

    elif money < value_of_order:
        print("The money you gave was lesser than the bill amount. Money refunded")  

    elif money > value_of_order:
        resources['water']-=MENU[choice]['ingredients']['water']
        resources['milk']-=MENU[choice]['ingredients']['milk']
        resources['coffee']-=MENU[choice]['ingredients']['coffee']
        print(f"Your order has been placed and your change is : ₹ {money-value_of_order}")



print("Welcome to Isloor's Espresso Bar")
for key in MENU:
    print(key+ " costs ₹ " + str(MENU[key]["cost"]))

choice = input("What would you like to have ?? 'expresso' or 'latte' or 'cappuccino' : ").capitalize()

order_placed(choice)

view_report = input("Type 'report' to view the remaning ingredients : ")

if view_report == 'report':
    print(resources)
# elif choice == 'latte':

# elif choice == 'cappuccino'        




