#!/usr/bin/python3
import random
from number_art import number

answer = random.randint(1,100)

def game(number_of_guesses):
    global answer
    for _ in range(1, number_of_guesses+1):
        if number_of_guesses == 0:
            break
        print(f"You have {number_of_guesses} attempts to guess the number")
        while True:
            try:
                make_a_guess = int(input("Make a guess: "))
                break
            except ValueError:
                print("Invalid Input. Try Again.")
        if make_a_guess == answer:
            print(f"You got it! The answer was {answer}")
            exit()
        if make_a_guess > answer:
            print("Too High.")
            print("Guess again.")
            number_of_guesses -= 1
        if make_a_guess < answer:
            print("Too Low.")
            print("Guess Again.")
            number_of_guesses -= 1
    print("You've run out of guesses, you lose.")
    exit()           
    
#Start of Script
print(number)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

choose_a_difficulty = str.lower(input("Choose a difficulty. Type 'easy' or 'hard': "))

if choose_a_difficulty == 'easy':
    game(10)
if choose_a_difficulty == 'hard':
    game(5)
else:
    print("Invalid Input")
    exit()