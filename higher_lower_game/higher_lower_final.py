#!/usr/bin/python3
from hlart import logo, vs
from data import data
import random, os


# This grabs a random person from the data.py list
def grab_random_person_from_list():
    random_number = random.randint(0, 49)
    person_selected = (data[random_number])
    return person_selected


# This function gives 2 new people or the previous person and a new person
def get_next_person(person_a, person_b):
    if person_b == "":
        person_b = grab_random_person_from_list()
    if person_a == "":
        person_a = grab_random_person_from_list()
    else:
        person_a = person_b
        person_b = grab_random_person_from_list()
    return person_a, person_b


# This function compares the follower count between the two people
def who_has_more_followers(person1, person2):
    if person1['follower_count'] > person2['follower_count']:
        return person1['name']
    else:
        return person2['name']


# This function shows the logos, the people, and prompts user for their guess
def guess(person_a, person_b, current_score):
    print(logo)
    if current_score > 0:
        print(f"You're right! Current score: {current_score}")
    print(f"Compare A: {person_a['name']}, {person_a['description']}, {person_a['country']}")
    print(vs)
    print(f"Compare B: {person_b['name']}, {person_b['description']}, {person_b['country']}")
    guess = str.lower(input("Who has more followers? Type 'A' or 'B': "))
    if guess == 'a' or guess == 'b':
        return guess
    else:
        print("Invalid Input. Exiting Program......")
        print(f"Your score was {current_score}")
        exit()


# This function checks to see if the guess is right
def is_the_user_correct(most_popular, persons_guess):
    if most_popular == persons_guess:
        return True
    else:
        return False


# This function is the main function and runs the whole program
def main():
    person_a = ""
    person_b = ""
    current_score = 0
    state_of_user = True
    while state_of_user == True:
        person_a, person_b = get_next_person(person_a, person_b)
        most_popular = (who_has_more_followers(person_a, person_b))
        users_guess = guess(person_a, person_b, current_score)
        if users_guess == "a":
            persons_guess = person_a['name']
        elif users_guess == "b":
            persons_guess = person_b['name']
        else:
            print("Invalid Input.")
            exit()
        state_of_user = is_the_user_correct(most_popular, persons_guess)
        if state_of_user == True:
            current_score += 1
        os.system('clear')
    print(f"Sorry, that's wrong. Final score: {current_score}")


# Calling of Function
main()
