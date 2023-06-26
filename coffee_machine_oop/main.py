#!/usr/bin/python
from turtle import Screen
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
my_menu = Menu()


user_request = str.lower(input(f"What would you like? ({my_menu.get_items()}): "))
requested_item = (my_menu.find_drink(user_request))
# coffee_machine.report()
if coffee_machine.is_resource_sufficient(requested_item):
    print("yay")
else:
    print("nay")