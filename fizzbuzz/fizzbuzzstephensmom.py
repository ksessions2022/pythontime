#!/usr/bin/python3

for i in range(1,100000001):
    isDivisableBy3 = i % 3 == 0
    isDivisableBy5 = i % 5 == 0

    if (isDivisableBy3 and isDivisableBy5):
        print("FIZZBUZZ")
    elif (isDivisableBy3):
        print("FIZZ")
    elif (isDivisableBy5):
        print("BUZZ")
    else:
        print(i)