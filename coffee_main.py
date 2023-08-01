import sys
from coffee_e import drink_ready
# Define dictionaries for the drinks and report

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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

'''Loop the wellcome message:
 “What would you like? (espresso/latte/cappuccino):” '''


choices = ["espresso","latte", "cappuccino", "report", "off"]

# Copy resources dictionary so that everytime we start the game the resources are the same
resources2 = resources
resources2.update({"money": 0.00})
def process_coins():
'''count the ammount of inserted money'''
    print("Please insert coins.")
    quarters = float(input("how many quarters? :")) * 0.25
    dimes = float(input("how many dimes? :")) * 0.10
    nickles = float(input("how many nickles? :")) * 0.05
    pennies = float(input("how many pennies? :")) * 0.01
    inserted_money = quarters + dimes + nickles + pennies
    return round(inserted_money, 2)


def change_or_not(inserted_money, choice):
'''calculate if enough money was inserted and if we need to return change'''
    if inserted_money == MENU[choice]["cost"]:
        returned_money = 0
        resources2["money"] = resources2["money"] + inserted_money
        print(f"Here is ${returned_money} in change")
        print(f"Here is your {choice} {drink_ready}. Enjoy!")
    elif inserted_money < MENU[choice]["cost"]:
        print("Sorry, that's not enough money. Money refunded.")
    elif inserted_money > MENU[choice]["cost"]:
        returned_money = inserted_money - MENU[choice]["cost"]
        resources2["money"] = resources2["money"] + MENU[choice]["cost"]
        print(f"Here is ${round(returned_money,2)} in change")
        print(f"Here is your {choice} {drink_ready}. Enjoy!")


stop_game = True

while stop_game:
    def check_resources(choice):
'''check if there are enough resources to make a drink and process'''
        if choice in ["report", "off"]:
            return False

        if MENU[choice]["ingredients"]["water"] > resources2["water"]:
            print(resources2["water"])
            print("Sorry there is not enough water")
            return False
        elif MENU[choice]["ingredients"]["coffee"] > resources2["coffee"]:
            print("Sorry there is not enough coffee")
            return False
        else:
            resources2["water"] = resources2["water"] - MENU[choice]["ingredients"]["water"]
            resources2["coffee"] = resources2["coffee"] - MENU[choice]["ingredients"]["coffee"]
            if choice in ["latte", "cappuccino"]:
                resources2["milk"] = resources2["milk"] - MENU[choice]["ingredients"]["milk"]
            return True
        ''' Prompt user by asking “What would you like?
        Turn off the Coffee Machine by entering “off” to the prompt.
        Print report'''
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice in choices:
        is_enough = check_resources(choice)
        if is_enough is True:
            print("we can do that")
            inserted_money = process_coins()
            change_or_not(inserted_money, choice)
        elif choice == "off":
            stop_game = False
        elif choice == "report":
            for key, value in resources2.items():
                print(key, value)
            # money also needs to be added





