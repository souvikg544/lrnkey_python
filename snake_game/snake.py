import turtle
import random

w=500
h=500
food_size=10
delay = 100

# (x,y)
offset={
    "up":(0,20),   # (x,y)
    "down":(0,-20),
    "left":(-20,0),
    "right":(20,0)

}
# Space for definitions

# Reset ---> move ---> collision -----> Food function ---->Distance between snake and food
def reset():
    global snake,snake_dir,food_position,pen
    snake=[[0,0],[0,20],[0,40],[0,60],[0,80]]
    snake_dir="up"
    food_position=get_random_food_pos()
    food.goto(food_position)
    move_snake()

def move_snake():
    global snake_dir
    new_head=snake[-1].copy()
    new_head[0]=snake[-1][0]+ offset[snake_dir][0]
    new_head[1] = snake[-1][1] + offset[snake_dir][1]

    if new_head
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
