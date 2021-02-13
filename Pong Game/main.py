from turtle import Screen
from paddle import Paddle
from ball import Ball
# import pandas as pd
# from matplotlib import pyplot as plt
#
# df = pd.read_clipboard()
# plt.plot(df,5)
# import random
#
# for _ in range(100):
#     print(random.randint(1,50))
#
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1280, height=1024)
screen.title("PONG da GAME!")
screen.tracer(0)

screen.listen()

r_paddle = Paddle((600,0))
l_paddle = Paddle((-600, 0))
print(l_paddle.position())
ball = Ball()
ball.start()


screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")



game_is_on=True

while game_is_on:
    screen.update()
    ball.move()
    time.sleep(0.027)
    print(ball.position())


    if ball.ycor() > 512 or ball.ycor() < - 512:
        ball.collision()

    if ball.xcor() > 600 and  ball.distance(l_paddle) < 50:
        ball.collision()
        print("hit")
    if ball.xcor < -600 and  ball.distance(l_paddle) < 50:
        print("hit")
        ball.collision()


    # Collect food
#     if ball.head.distance(food) < 25:
#         food.refresh()
#         ball.extend()
#         counter += 1
#     #Hit da wall
#
#     if ball.head.xcor()> 280 or ball.head.xcor() < -280 or ball.head.ycor() > 280 or ball.head.ycor() < - 280:
#         game_is_on=False
#         score.game_over()
#
#     # Hit tail
#     for segment in ball.segments[1::]:
#         if ball.head.distance(segment) <10:
#             game_is_on = False
#             score.game_over()
#
# screen.exitonclick()
