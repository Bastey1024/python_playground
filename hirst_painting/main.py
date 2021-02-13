#####Turtle Intro######

import turtle as t
import random
import colorgram

color_list=[]

def color_thiev(image):
    colors = colorgram.extract(image, 8)
    for color in colors:
      color=color.rgb
      red = color.r
      green = color.g
      blue = color.b
      new_color=(red,green,blue)
      color_list.append(new_color)

timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

t.colormode(255)
color_thiev('image.jpg')
direction=[90,180,270,360]

screen=t.TurtleScreen()
screen.screensize(600,600)
timmy_the_turtle.goto(-600, -600)

def random_walk():

  timmy_the_turtle.forward(10)
  timmy_the_turtle.setheading(random.choice(direction))
  timmy_the_turtle.pencolor(random.choice(color_list))
def draw_heist():
    timmy_the_turtle.dot(20)

    for _ in range(11):
        timmy_the_turtle.pencolor(random.choice(color_list))

        timmy_the_turtle.forward(10)





while True:
  draw_heist()





def formes(corners):
  angle = 360 / corners
  for i in range(1,corners):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.rt(angle)
  timmy_the_turtle.forward(100)
  timmy_the_turtle.rt(angle)


#
#
#   import turtle as turtle_module
# import random
#
# turtle_module.colormode(255)
# tim = turtle_module.Turtle()
# tim.speed("fastest")
# tim.penup()
# tim.hideturtle()
# color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# number_of_dots = 100
#
# for dot_count in range(1, number_of_dots + 1):
#     tim.dot(20, random.choice(color_list))
#     tim.forward(50)
#
#     if dot_count % 10 == 0:
#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)
#
#
#
#
#
#
#
#
#
# screen = turtle_module.Screen()
# screen.exitonclick()
