#!/usr/bin/python

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip Calculator.")

#This asks how much the bill is
total_bill = input("What was the total bill? $")

#This variable asks for what percentage you want to tip
percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")

#This asks for how many people are splitting the bill
people = input("How many people to split the bill? ")

#This multiplies the total bill with the percentage
cost_multiply = float(total_bill) * int(percentage)

#This divides cost_multiply by 100 to see how much the tip is. It rounds to the nearest 2 decimals
cost_divide = round(cost_multiply / 100, 2)

#This adds the total_bill to the cost_divide to find the total cost owed to the resturaunt
total_cost = float(cost_divide) + float(total_bill)

#This take the total cost owed and divides it evenly between all the people at the resturaunt
person_each = float(total_cost) / float(people)

#This prints out how much everyone owes
print(f"Each person should pay: ${person_each}")
