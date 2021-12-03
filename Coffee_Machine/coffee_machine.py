from menu import MENU
from menu import resources
from menu import coins_values


def stock(money):
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']

    print(f"\nWater: {water}ml")
    print(f'Milk: {milk}ml')
    print(f'Coffee {coffee}ml')
    print(f"Money: ${money}")


def check_coins(quarters, dimes, nickels, pennies, desired_item, request):
    print("Please insert coins.")
    print(f"Price: ${desired_item['cost']}")
    inserted_coins = 0
    money = 0

    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    inserted_coins = round(
        quarters * coins_values['quarter'] + dimes * coins_values['dime'] + nickels * coins_values['nickel'] + pennies *
        coins_values['penny'], 3)

    print(f"Here is {inserted_coins} in change.")

    if inserted_coins < desired_item['cost']:
        print("Sorry that's not enough money. Money refunded.")
    elif inserted_coins >= desired_item['cost']:
        print(f'Here is your {request} ☕. Enjoy!')
        money += inserted_coins


def order(quarters, dimes, nickels, pennies, desired_item, request, money):
    request = input("\nWhat would you like? (espresso/latte/cappuccino).To exit type 'exit': ")

    if request == 'report':
        password = input('Pass the password: ')
        if password == '1234':
            stock(money)
            order(quarters, dimes, nickels, pennies, desired_item, request, money)
        else:
            print("\nWrong password!")
            order(quarters, dimes, nickels, pennies, desired_item, request, money)
    elif request == 'espresso' or request == 'latte' or request == 'cappuccino':
        desired_item = MENU[request]


        for item in desired_item["ingredients"]:
            resources[item] -= desired_item["ingredients"][item]
            if resources[item] < 0:
                resources[item] += desired_item["ingredients"][item]
                print(f"Sorry there is not enough {item}")
                order(quarters, dimes, nickels, pennies, desired_item, request, money)

        check_coins(quarters, dimes, nickels, pennies, desired_item, request)

        order(quarters, dimes, nickels, pennies, desired_item, request, money)
    else:
        print("\nSee you later. Goodbye!")
        quit()


order(quarters=0, dimes=0, nickels=0, pennies=0, desired_item='', request='', money=0)