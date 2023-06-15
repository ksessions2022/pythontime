#!/usr/bin/python3
import random
from number_art import number

HARD_LEVEL_DIFFICULTY = 5
EASY_LEVEL_DIFFICULTY = 10

def guess():
    while True:
        try:
            make_a_guess = int(input("Make a guess: "))
            return make_a_guess
        except ValueError:
            print("Invalid Input. Try Again.")

def choose_difficulty():
    choose_a_difficulty = str.lower(input("Choose a difficulty. Type 'easy' or 'hard': "))
    if choose_a_difficulty == "easy":
        return EASY_LEVEL_DIFFICULTY
    elif choose_a_difficulty == "hard":
        return HARD_LEVEL_DIFFICULTY
    else:
        print("Invalid Input")
        exit()

def check_guesses(answer, turns, user_guess):
    if user_guess == answer:
        print(f"You got it! The answer is {answer}! ")
        exit()
    if user_guess > answer:
        print("Too High.")
        
    if user_guess < answer:
        print("Too Low")

    print("Guess Again")
    return turns - 1

def main():
    print(number)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1,100)
    turns = choose_difficulty()
    while turns != 0:
        print(f"You have {turns} attempts to guess the number")
        user_guess = guess()
        turns = check_guesses(answer, turns, user_guess)
    print("You ran out of guesses. You lose!")

main()