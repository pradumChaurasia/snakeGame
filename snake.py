import os
import turtle
import time
import random

Score = 0
High_score = 0
delay = 0.1

wn = turtle.Screen()

wn.title("snake game")
wn.bgcolor("green")
wn.setup(width = 600, height = 600)
wn.tracer(0)


head = turtle.Turtle()

head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

def go_up():
    if head.direction != "Down":
        head.direction = "up"

def go_Down():
    if head.direction != "up":
        head.direction = "Down"

def go_Left():
    if head.direction != "Right":
        head.direction = "Left"

def go_Right():
    if head.direction != "Left":
        head.direction = "Right"


food = turtle.Turtle()

food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)
food.direction = "stop"

segments =[]

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("circle")
pen.color("pink")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score : 0 High score : 0",align = "center", font = ("Courier",24, "normal"))


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction == "Down":
        y = head.ycor()
        head.sety(y-20)

    if head.direction == "Left":
        x = head.xcor()
        head.setx(x-20)

    if head.direction == "Right":
        x = head.xcor()
        head.setx(x+20)

wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_Down, "s")
wn.onkeypress(go_Right, "d")
wn.onkeypress(go_Left, "a")


while True:
    wn.update()

    #check for collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

    #check for collision with food
    if head.distance(food) < 20:
        #move the food at the random spot on screen
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        #add a segment in body of snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)


        #shorten the delay
        delay -= 0.001



        #increase the score
        Score += 10

        if Score >High_score:
            High_score = Score

        pen.clear()
        pen.write("Score : {} High score : {} ".format(Score,High_score),align = "center", font = ("Courier",24,"normal"))


    #move the end segments first in reverse
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    #move segments 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)



    move()

    #check for  head collision
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # clear the segemnts list
            segments.clear()

            #reset the score
            Score = 0

            #reset the delay
            delay = 0.1

            pen.clear()
            pen.write("Score : {} High score : {} ".format(Score, High_score), align="center",
                      font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()