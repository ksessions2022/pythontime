#!/usr/bin/python3
import random
from blackjack_art import blackjack_logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Functions

def main():
    do_you_want_to_play = str.lower(input("Do you want to play a game of Blackjack? Type 'y' or 'n': "))
    if do_you_want_to_play == "y":
        blackjack_game()
    else:
        print("Exiting Game......")
        exit()

def deal_cards(x):
   for _ in range(2):
       random_cards = random.choice(cards)
       x.append(random_cards)
   return x

def hit(x):
    random_cards = random.choice(cards)
    x.append(random_cards)
    return x

def calculate_current_score(cards):
    current_score = sum(cards)
    return current_score

def win_or_lose(comment):
    print(comment)
    main()

def blackjack_game():
    print(blackjack_logo)
    user_cards = []
    computer_cards = []
    user_random_cards = deal_cards(user_cards)
    computer_random_cards = deal_cards(computer_cards)
    user_current_score = calculate_current_score(user_random_cards)
    computer_current_score = calculate_current_score(computer_random_cards)
    if user_current_score == 21:
        print("You have a blackjack! You win!")
        exit()
    if computer_current_score == 21:
        print("The computer has a blackjack. you lose!")
        exit()
    while sum(computer_cards) < 17:
        hit(computer_cards)    
    print(f"Your cards: {user_cards} current score: {user_current_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    another_card = str.lower(input("Type 'y' to get another card, type 'n' to pass: "))
    while another_card == "y":
        hit(user_cards)
        user_current_score = calculate_current_score(user_cards)
        if user_current_score > 21:
            break
        print(f"Your cards: {user_cards} current score: {user_current_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        another_card = str.lower(input("Type 'y' to get another card, type 'n' to pass: "))
    
    print(f"Your final hand: {user_cards} final score: {user_current_score}")
    print(f"Computer's final hand: {computer_cards} final score: {computer_current_score}")

    if computer_current_score > 21:
        win_or_lose("opponent went over. You win")
    elif user_current_score > 21:
        win_or_lose("you went over, you lose!")
    elif user_current_score >= computer_current_score and user_current_score < 21:
        win_or_lose("You Win!")
    else:
        win_or_lose("You Lose!")

#Start of script
main()