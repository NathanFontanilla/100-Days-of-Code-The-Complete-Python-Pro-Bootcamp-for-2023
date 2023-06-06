# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
#
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }
#
# #from coffee_machine_info import *
# #from coffee_machine import *
# def refill_machine():
#     global water
#     global milk
#     global coffee
#     global money
#
#     water = 100
#     milk = 50
#     coffee = 76
#     money = 2.5
# def print_report(w, m, c, money):
#     print("Water:", w, "ml")
#     print("Milk:", m, "ml")
#     print("Coffee", c, "g")
#     print("Money: $", money)
#
# def check_resources(drink_choice ):
#     global water
#     if drink_choice == 'espresso':
#         print("Yr")
#         if (MENU['espresso']['ingredients']['water'] - water) > 0:
#             print("Yerrrr")
#     elif drink_choice == 'latte':
#         pass
#     elif drink_choice == 'cappuccino':
#         pass
#     else:
#         print("Invalid Input")
#
#
# #from coffee_machine_info import MENU
# #from coffee_machine_functions import *
#
# # TODO: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# order = input('What would you like? (espresso/latte/cappuccino):')
#
# # TODO: Create Vairibles.
# # Coins Price
# QUARTER = 0.25
# DIME = 0.10
# NICKLE = 0.05
# PENNY = 0.01
#
# # Coins in machine
# quarter = 0.0
# dime = 0.0
# nickle = 0.05
# penny = 0.01
#
# # Resources
# water = 100.0
# milk = 50.0
# coffee = 76.0
# money = 2.5
#
# # Misc
# #refill_machine()
#
# # TODO: Turn off the Coffee Machine by entering “off”to the prompt.
#
# # TODO: Print report. (Done)
# #print_report(water, milk, coffee, money)
#
# # TODO: Check resources sufficient?
# check_resources(order)
# # TODO: Process coins.
# # TODO: Check transaction successful?
# # TODO: Make Coffee.
#
#
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,  # 300
    "milk": 200,
    "coffee": 100,  # 100
}

# TODO: Create Vairibles.
# Coins Price
QUARTER = 0.25
DIME = 0.10
NICKLE = 0.05
PENNY = 0.01

# Coins in machine
quarter = 0.25
dime = 0.10
nickle = 0.05
penny = 0.01

# Resources
money = 2.5


def get_money(drink_choice):
    global money

    print("Please insert coins.")
    q = int(input("how many quarters?: "))
    d = int(input("how many dimes?: "))
    n = int(input("how many nickles?: "))
    p = int(input("how many pennies?: "))

    # TODO: convert into preices
    q = q * quarter
    d = d * dime
    n = n * nickle
    p = p * penny

    tender = q + d + n + p

    # TODO: Check is enough movey for drink
    if tender >= MENU[drink_choice]['cost']:
        # TODO: Add money in coffee machine
        change = tender - MENU[drink_choice]['cost']
        money = money + (tender - change)
        print("Money in machine:", money)
        print("Your change is ", round(change, 2))

        return True

    else:
        print("You don't have enough money broke boi")
        return False  # DONE


def refill_machine():
    resources['water'] = + 100
    resources['milk'] = + 50
    resources['coffee'] = + 50


def print_report():
    global money

    print("Water:", resources['water'], "ml")
    print("Milk:", resources['milk'], "ml")
    print("Coffee", resources['coffee'], "g")
    print("Money: $", money)


def check_ingredient(drink_choice, ingredient):
    # Check if a specific there is enough of a specific ingrediant

    diff = resources[ingredient] - MENU[drink_choice]['ingredients'][ingredient]

    if diff > 0:
        # print('enough')
        return True
    else:
        # print('not enough')
        return False


def check_resources(drink_choice):
    low_resources = []

    if drink_choice == 'espresso':

        if (check_ingredient(drink_choice, 'water') and check_ingredient(drink_choice, 'coffee')):
            return True
            print("enough resources for espresso")
        else:
            if check_ingredient(drink_choice, 'water') == False:
                low_resources.append('water')

            if check_ingredient(drink_choice, 'coffee') == False:
                low_resources.append('coffee')

            print("sorry there is not enough", low_resources)

            return False




    elif drink_choice == 'latte':

        if (check_ingredient(drink_choice, 'water') and check_ingredient(drink_choice, 'coffee') and check_ingredient(
                drink_choice, 'milk')):
            print("enough resources for latte")
            return True
        else:
            if check_ingredient(drink_choice, 'water') == False:
                low_resources.append('water')

            if check_ingredient(drink_choice, 'coffee') == False:
                low_resources.append('coffee')

            if check_ingredient(drink_choice, 'milk') == False:
                low_resources.append('milk')

            print("sorry there is not enough", low_resources)

            return False

    elif drink_choice == 'cappuccino':

        if (check_ingredient(drink_choice, 'water') and check_ingredient(drink_choice, 'coffee') and check_ingredient(
                drink_choice, 'milk')):
            print("enough resources for cuppuccino")
            return True
        else:
            if check_ingredient(drink_choice, 'water') == False:
                low_resources.append('water')

            if check_ingredient(drink_choice, 'coffee') == False:
                low_resources.append('coffee')

            if check_ingredient(drink_choice, 'milk') == False:
                low_resources.append('milk')

            print("sorry there is not enough", low_resources)

            return False



    else:
        print("Invalid Input")


def run_coffee_machine():
    """
    1. Get Coffee Order
    2. See if there is enough ingrediantes
    3. Get money
    4. make coffee (subtract resources)
    5. Give coffee
    """

    # 1. Get Coffee Order
    order = input('What would you like? (espresso: $1.5 /latte: $2.5 /cappuccino: $3):')

    # 2. See if there is enough ingrediantes

    if check_resources(order) == True:
        if get_money(order) == True:
            print("Here is your", order, "☕️. Enjoy!")


run_coffee_machine()





