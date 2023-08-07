from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
scoreboard = Scoreboard()

# Creating the Screen
screen.setup(width=1600, height=1200)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-750, 0))
r_paddle = Paddle((750, 0))
ball = Ball()

screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

game_is_ongoing = True
while game_is_ongoing:
    time.sleep(0.015)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 580 or ball.ycor() < -580:
        ball.bounce_y()

    # Detect collision with r_pad and l pad
    if ball.distance(r_paddle) < 60 and ball.xcor() > 720:
        new_x = ball.xcor() - 20
        ball.goto(new_x, ball.ycor())
        ball.bounce_x()

    if ball.distance(l_paddle) < 60 and ball.xcor() < -720:
        new_x = ball.xcor() + 20
        ball.goto(new_x, ball.ycor())
        ball.bounce_x()

    # Detect R paddle miss
    if ball.xcor() > 2350:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.l_paddle_score()
        
    # Detect L paddle miss
    if ball.xcor() < -2350:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.r_paddle_score()


screen.exitonclick()