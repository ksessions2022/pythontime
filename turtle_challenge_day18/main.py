#!/usr/bin/python3
from turtle import Turtle, Screen
import random

tim = Turtle(shape="turtle")
screen = Screen()


def random_color():
    colors = ["cyan", "purple", "black", "blue", "red", "pink", "green", "brown"]
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
    triangle = Shape(3)
    square = Shape(4)
    pentagon = Shape(5)
    hexagon = Shape(6)
    heptagon = Shape(7)
    octagon = Shape(8)
    nonagon = Shape(9)
    decagon = Shape(10)

    triangle.draw()
    square.draw()
    pentagon.draw()
    hexagon.draw()
    heptagon.draw()
    octagon.draw()
    nonagon.draw()
    decagon.draw()
    screen.exitonclick()


main()
