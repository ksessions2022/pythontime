#!/usr/bin/python3

def what_would_you_like():
    coffee_drink_wanted = str.lower(int(input(("What would you like? (espresso/latte/cappuccino): "))
    return coffee_drink_wanted

def please_insert_coins():
    print("Please insert coins.")
    number_of_quarters = int(input(("how many quarters?: ")))
    quarter_value = (number_of_quarters * 0.25)
    number_of_dimes = int(input(("how many dimes?: ")))
    dime_value = (number_of_dimes * 0.10)
    number_of_nickles = int(input(("how many nickels?: ")))
    nickle_value = (number_of_nickles * 0.05)
    number_of_pennies = int(input(("how many pennies?: ")))
    pennies_value = (number_of_pennies * 0.01)
    sum_of_coins = quarter_value + dime_value + nickle_value + pennies_value
    return sum_of_coins
    

please_insert_coins()





































