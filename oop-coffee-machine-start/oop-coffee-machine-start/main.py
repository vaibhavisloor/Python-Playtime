from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
menu_items =menu.get_items()
menu_drinks =menu_items.split('/')
print(menu_drinks)
print('In our menu we today have ')
for dish in menu_drinks:
    print(dish)

machine = True

while machine == True:

    choice=input("Check if we have the drink of your choice today !\n")

    drink = menu.find_drink(choice)

    money = MoneyMachine()
    coffee = CoffeeMaker()

    for item in menu.menu:
        if item.name == choice:
            cost = item.cost

    if money.make_payment(cost) == True:
        coffee.is_resource_sufficient(drink)
        coffee.make_coffee(drink)

one_more = input("Do you want to order again ?? 'yes' or 'no'") 

if one_more == 'yes':
    machine = True
else:
    machine=False    