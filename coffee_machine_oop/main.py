#!/usr/bin/python
from turtle import Screen
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
my_menu = Menu()
atm = MoneyMachine()

while True:
    user_request = str.lower(input(f"What would you like? ({my_menu.get_items()}): "))
    if user_request == "report":
        coffee_machine.report()
        atm.report()
    elif user_request == "off":
        exit()
    else:
        requested_item = (my_menu.find_drink(user_request))
        if coffee_machine.is_resource_sufficient(requested_item):
            if atm.make_payment(requested_item.cost):
                coffee_machine.make_coffee(requested_item)
        else:
            print("Not enough resources")