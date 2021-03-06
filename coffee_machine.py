import math
from coffee_machine_data import MENU, resources

money = 0.00
water = 300
milk = 200
coffee = 100

espresso = "espresso"
latte = "latte"
cappuccino = "cappuccino"






next_customer = True
while next_customer:
    order = input(f"What would you like? \n{espresso}, {latte}, or a {cappuccino} ").lower()
    print(order)
    report = resources

    if order == "report":
        print(f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g \nMoney: ${money}")
    elif order == "off":
        exit("powering down")
    elif order == "espresso":
        water -= 50
        coffee -= 18
        print("")
    elif order == "latte":
        water -= 200
        milk -= 150
        coffee -= 24
        print("")
    elif order == "cappuccino":
        water -= 250
        milk -= 100
        coffee -= 24
        print("")


def sufficient_resources():
    if order == "espresso" and water >= 50 and coffee >= 18 and money >= 3.00:

    elif order == "latte" and water >= 200 and milk >= 150 and coffee >= 24 and money >= 3.50:
                    # make drink
    elif order == "cappuccino" and water >= 250 and milk >= 100 and coffee >= 24 and money >= 4.00:
