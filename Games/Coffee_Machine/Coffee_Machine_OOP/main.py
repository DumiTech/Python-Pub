from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu_item import MenuItem
from menu import Menu

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    menu_list = menu.get_items()
    choice = input(f"\nWhat would you like? {menu_list}: ")
    
    if choice == 'off':
        money_machine.off()
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
            
        