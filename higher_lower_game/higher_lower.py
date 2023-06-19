#!/usr/bin/python3
from hlart import logo, vs
from data import data
import random

def random_person_selection():
    pick_random_number = random.randint(0,49)
    person = (data[pick_random_number])
    return person

def extract_information():
    person = random_person_selection()
    name = person['name']
    number_of_followers = person['follower_count']
    description = person['description']
    country = person['country']
    return name, number_of_followers, description, country

def who_has_more_followers(person1, person2):
    if person1[1] > person2[1]:
        return person1[0]
    else:
        return person2[0]
    
def is_the_user_correct(most_popular, persons_guess):
    if most_popular == persons_guess:
        return True
    else:
        return False
    
def main():
    print(logo)
    person_a = extract_information()
    person_b = extract_information()
    print(f"Compare A: {person_a[0]}, {person_a[2]}, {person_a[3]}")
    print(vs)
    print(f"Compare B: {person_b[0]}, {person_b[2]}, {person_b[3]}")
    guess = str.lower(input("Who has more followers? Type 'A' or 'B': "))
    most_popular = (who_has_more_followers(person_a, person_b))
    if guess == "a":
        persons_guess = person_a[0]
        is_the_user_correct(most_popular, persons_guess)
    elif guess == "b":
        persons_guess = person_b[0]
        is_the_user_correct(most_popular, persons_guess)
    else:
        print("Invalid Input.")
        exit()
    
main()
