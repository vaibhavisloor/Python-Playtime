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

print("Welcome to Isloor's Bistro ")

print("Today we have :")

for drink in MENU:
    print(drink,end=" / ")

choice = input("What would you like to have ??  :  ").capitalize()

if resources['water'] - MENU[choice]["ingredients"]["water"] > 0 and resources['milk'] - MENU[choice]["ingredients"]["milk"] > 0 and resources['coffee'] - MENU[choice]["ingredients"]["coffee"] > 0 :
    
    resources['water'] -= MENU[choice]["ingredients"]["water"]
    resources['milk'] -= MENU[choice]["ingredients"]["milk"]
    resources['coffee'] -= MENU[choice]["ingredients"]["coffee"]
    print(resources)
    cost = MENU[choice]['cost']
    pay_bill = int(input(f"Your bill is Rs.{cost}"))

    if pay_bill > cost:
        print(f"Rs {pay_bill - cost } is your change. Here is your {drink}")
    elif pay_bill < cost:
        print("Insufficient money, Money refunded")    
    elif pay_bill == cost:
        print(f"Here is your {drink}")

else:
    print("Sorry..insufficient resources")



