#!/usr/bin/python3
from hlart import logo, vs
from data import data
import random

pick_random_number = random.randint(0,49)
current_score = 0
person_a = (data[pick_random_number])
person_b = (data[pick_random_number])

def random_person_selection():
    pick_random_number = random.randint(0,49)
    person = (data[pick_random_number])
    return person

def who_has_more_followers(person1, person2):
    if person1['follower_count'] > person2['follower_count']:
        return person1['name']
    else:
        return person2['name']
    
def is_the_user_correct(most_popular, persons_guess):
    global current_score
    if most_popular == persons_guess:
        current_score += 1
        print(f"You're right! Current score: {current_score}")
        main()
    else:
        print(f"Sorry, that's wrong. Final score: {current_score}")
        exit()
    
def guess():   
    print(logo)
    print(f"Compare A: {person_a['name']}, {person_a['description']}, {person_a['country']}")
    print(vs)
    print(f"Compare B: {person_b['name']}, {person_b['description']}, {person_b['country']}")
    guess = str.lower(input("Who has more followers? Type 'A' or 'B': "))
    return guess


def main():
    guess()
    most_popular = (who_has_more_followers(person_a, person_b))
    if guess() == "a":
        persons_guess = person_a['name']
        is_the_user_correct(most_popular, persons_guess)
    elif guess() == "b":
        persons_guess = person_b['name']
        is_the_user_correct(most_popular, persons_guess)
    else:
        print("Invalid Input.")
        exit()
    
main()
