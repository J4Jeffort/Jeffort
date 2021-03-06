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
espresso = "espresso"
latte = "latte"
cappuccino = "cappuccino"
money = 0


def sufficient_resources(order_ingredients):
    """Returns true if enough resources. false if short."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}. ")
            return False
    return True


def is_transaction_successful(money_received, drink_cost):
    """Return true if enough money. False if short"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change. ")
        global money
        money = + drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def process_change():
    """Returns sum of coins"""
    print("Please insert change")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def make_coffee(drink_name, order_ingredients):
    """deduct ingredients from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ")


is_on = True

while is_on:
    order = input(f"What would you like? \n{espresso}, {latte}, or a {cappuccino} ").lower()
    if order == "off":
        is_on = False
    elif order == "report":
        print(f"Water:{resources['water']}ml")
        print(f"Milk:{resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        drink = MENU[order]
        if sufficient_resources(drink["ingredients"]):
            payment = process_change()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(order, drink["ingredients"])
