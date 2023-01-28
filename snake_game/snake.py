import turtle
import random

w=500
h=500
food_size=10
delay = 100

# (x,y)
offset={
    "up":(0,20),
    "down":(0,-20),
    "left":(-20,0),
    "right":(20,0)

}
# Space for definitions

#Reset ---> move ---> collision -----> Food function ---->Distance between snake and food

# Utilize all the functions below

#Go up
# Go down
#  Go left
# Go right


# Making our screen
screen=turtle.Screen()
screen.setup(w,h)
screen.title("Our Snake Game")
screen.bgcolor("blue")
screen.setup(500,500)
screen.tracer(0)



pen=turtle.Turtle("square")
pen.penup()

food=turtle.Turtle()
food.shape("square")
food.color("green")
food.shapesize(food_size/20)
food.penup()


turtle.done()
