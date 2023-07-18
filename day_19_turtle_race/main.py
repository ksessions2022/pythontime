from turtle import Turtle, Screen
import random

# screen setup
is_race_ongoing = False
all_competitors = {}

screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("black")

character_names = ["casey", "raphael", "leonardo", "donatello", "michelangelo"]
character_colors = ["white", "red", "blue", "purple", "orange"]
user_bet = ""
y_point = -100


while user_bet != "casey" and user_bet != "raphael" and user_bet != "leonardo" and user_bet != "donatello" and user_bet != "michelangelo":
    user_bet = str.lower(screen.textinput(title="Make your bet", prompt="Which Ninja Turtle will win the race? Enter Raphael, Leonardo, Donatello, Michelangelo, or Casey: "))

# This generates the characters as objects and assigns them a name and a color
for i in range(5):
    character = character_names[i]
    if character == "casey":
        character = Turtle(shape="circle")
    else:
        character = Turtle(shape="turtle")
    character.color(character_colors[i])
    character.penup()
    character.goto(x=-230, y=y_point)
    all_competitors[character] = character_names[i]
    y_point += 50

if user_bet:
    is_race_ongoing = True

while is_race_ongoing:
    for racer in all_competitors:
        random_distance = random.randint(0, 10)
        racer.forward(random_distance)
        if racer.xcor() > 230:
            winning_character = all_competitors[racer]
            is_race_ongoing = False

if winning_character == user_bet:
    print(f"You've won! {winning_character[0].upper() + winning_character[1:]} is the winner!")
else:
    print(f"You've lost! {winning_character[0].upper() + winning_character[1:]} is the winner!")

screen.exitonclick()