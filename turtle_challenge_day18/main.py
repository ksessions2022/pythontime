#!/usr/bin/python3
from turtle import Turtle, Screen
import random

tim = Turtle(shape="turtle", visible=False)
screen = Screen()


def random_color():
    colors = ["cyan", "purple", "black", "blue", "red", "pink", "green", "brown", "blue violet", "chartreuse",
              "deep pink", "tomato", "teal"]
    chosen_color_for_shape = tim.color(random.choice(colors))
    return chosen_color_for_shape


def angle_formula(number_of_sides):
    """
    This calculates the angle of each corner of the shape and returns the angle.
    """
    angle = (360 / number_of_sides)
    return angle


def turtle_position():
    """
    Set's the starting position for the turtle Tim
    """

    offset = -75
    tim.penup()
    tim.goto(offset, screen.window_height() / 2 + offset)
    tim.pendown()
    tim.showturtle()


class Shape:

    def __init__(self, number_of_sides):
        self.length_of_side = 150
        self.number_of_sides = number_of_sides
        self.angle = angle_formula(number_of_sides)

    def draw(self):
        random_color()
        for _ in range(self.number_of_sides):
            tim.forward(self.length_of_side)
            tim.right(self.angle)


def main():
    turtle_position()
    for i in range(3, 11):
        shape = Shape(i)
        shape.draw()
    screen.exitonclick()

main()
