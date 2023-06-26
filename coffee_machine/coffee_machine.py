#!/usr/bin/python3

# Resources that the Coffee Machine has in Stock
water = 300
milk = 200
coffee = 100
money = 0

def money_formatter(x):
    money_formatted = '${:,.2f}'.format(x)
    return money_formatted

coffee_ingredients = [
    {'coffee_type': 'espresso', 'amount_of_water': 50, 'amount_of_milk': 0, 'amount_of_coffee': 18, 'cost_of_coffee': 1.50},
    {'coffee_type': 'latte', 'amount_of_water': 200, 'amount_of_milk': 150, 'amount_of_coffee': 24, 'cost_of_coffee': 2.50},
    {'coffee_type': 'cappuccino', 'amount_of_water': 250, 'amount_of_milk': 100, 'amount_of_coffee': 24, 'cost_of_coffee': 3}]

def what_would_you_like():
    coffee_drink_options = ""
    while coffee_drink_options != "espresso" and coffee_drink_options != "latte" and coffee_drink_options != "cappuccino":
        coffee_drink_options = str.lower(input("What would you like? (espresso/latte/cappuccino): "))
        if coffee_drink_options != "espresso" and coffee_drink_options != "latte" and coffee_drink_options != "cappuccino" and coffee_drink_options != "report" and coffee_drink_options != "off":
            print("Invalid Input, try again")
        elif coffee_drink_options == "report":
            print(f"Water: {water}ml")
            print(f"Milk: {milk}ml")
            print(f"Coffee: {coffee}g")
            print(f"Money: {money_formatter(money)}")
        elif coffee_drink_options == "off":
            exit()
        else:
            if coffee_drink_options == "espresso":
                return coffee_ingredients[0]
            elif coffee_drink_options == "latte":
                return coffee_ingredients[1]
            else:
                return coffee_ingredients[2]
def inserted_coins():
    print("Please insert coins.")
    number_of_quarters = int(input("how many quarters?: ")) * 0.25
    number_of_dimes = int(input("how many dimes?: ")) * 0.10
    number_of_nickles = int(input("how many nickels?: ")) * 0.05
    number_of_pennies = int(input("how many pennies?: ")) * 0.01
    sum_of_coins = number_of_quarters + number_of_dimes + number_of_nickles + number_of_pennies
    return sum_of_coins

def check_money_paid(price, paid):
    customer_change = paid - price
    if price > paid:
        return False, float(customer_change)
    else:
        return True, float(customer_change)

def check_resources(resources):
    if resources['amount_of_water'] > water:
        message = "water"
        return False, message
    elif resources['amount_of_milk'] > milk:
        message = "milk"
        return False, message
    elif resources['amount_of_coffee'] > coffee:
        message = "coffee"
        return False, message
    else:
        message = ""
        return True, message

def main():
    global water, milk, coffee, money
    while True:
        while True:
            customers_choice = what_would_you_like()
            enough_machine_resources, not_enough_of_ingredient = check_resources(customers_choice)
            if not enough_machine_resources:
                print(f"Sorry, there is not enough {not_enough_of_ingredient}")
                break
            money_paid = inserted_coins()
            coffee_chosen = customers_choice['coffee_type']
            price_of_coffee = customers_choice['cost_of_coffee']
            enough_money, customers_needed_change = check_money_paid(price_of_coffee, money_paid)
            if enough_money:
                print(f"Here is {money_formatter(customers_needed_change)} in change.")
                print(f"Here is your {coffee_chosen} Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
            money += (money_paid - customers_needed_change)
            water -= customers_choice['amount_of_water']
            milk -= customers_choice['amount_of_milk']
            coffee -= customers_choice['amount_of_coffee']
main()
