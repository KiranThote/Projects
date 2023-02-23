from turtle import Turtle, Screen
import datetime

window = Screen()
window.title("Analog Clock")
window.bgcolor("black")
window.setup(width = 1000,height=700)

circle = Turtle()
circle.penup()
circle.pencolor('#118893')
circle.speed(0)
circle.pensize(25)
circle.hideturtle()
circle.goto(0,-390)
circle.pendown()
circle.fillcolor("#17202A")
circle.begin_fill()
circle.circle(400)
circle.end_fill()

hHand = Turtle()
hHand.shape("arrow")
hHand.color("Red")
hHand.speed(10)
hHand.shapesize(stretch_wid=0.4, stretch_len=18)

mHand = Turtle()
mHand.shape("arrow")
mHand.color("Blue")
mHand.speed(10)
mHand.shapesize(stretch_wid=0.4, stretch_len=26)

sHand = Turtle()
sHand.shape("arrow")
sHand.color("White")
sHand.speed(10)
sHand.shapesize(stretch_wid=0.4, stretch_len=36)

centerCircle = Turtle()
centerCircle.shape("circle")
centerCircle.color("Green")
centerCircle.shapesize(stretch_wid=1.5, stretch_len=1.5)

pen = Turtle()
pen.speed(0)
pen.color("White")

pen.penup()
pen.hideturtle()
pen.goto(170,260)
pen.write("1", align="center",font=("Algerain", 50,"bold"))

pen.penup()
pen.hideturtle()
pen.goto(300,140)
pen.write("2", align="center",font=("Algerain", 50,"bold"))

pen.penup()
pen.hideturtle()
pen.goto(340,-30)
pen.write("3", align="center",font=("Algerain", 50,"bold"))

pen.penup()
pen.hideturtle()
pen.goto(300,-200)
pen.write("4", align="center",font=("Algerain", 50,"bold"))

pen.penup()
pen.hideturtle()
pen.goto(170,-325)
pen.write("5", align="center",font=("Algerain", 50,"bold"))

pen.penup()
pen.hideturtle()
pen.goto(0,-370)
pen.write("6", align="center",font=("Algerain", 50,"bold"))

pen.penup()
pen.hideturtle()
pen.goto(-170,-325)
pen.write("7", align="center",font=("Algerain", 50,"bold"))

pen.penup()
pen.hideturtle()
pen.goto(-300,-200)
pen.write("8", align="center",font=("Algerain", 50,"bold"))

pen.penup()
pen.hideturtle()
pen.goto(-340,-30)
pen.write("9", align="center",font=("Algerain", 50,"bold"))

pen.penup()
pen.hideturtle()
pen.goto(-280,140)
pen.write("10", align="center",font=("Algerain", 50,"bold"))

pen.penup()
pen.hideturtle()
pen.goto(-160,260)
pen.write("11", align="center",font=("Algerain", 50,"bold"))

pen.penup()
pen.hideturtle()
pen.goto(0,300)
pen.write("12", align="center",font=("Algerain", 50,"bold"))

def movehHand():
    currentHourInternal = datetime.datetime.now().hour
    degree =(currentHourInternal - 15) * -30
    currentminuteInternal = datetime.datetime.now().minute
    degree = degree + -0.5* currentminuteInternal
    hHand.setheading(degree)
    window.ontimer(movehHand,60000)

def movemHand():
    currentminuteInternal = datetime.datetime.now().minute
    degree =(currentminuteInternal - 15) * -6
    currentsecondInternal = datetime.datetime.now().second
    degree = degree + (-currentsecondInternal*0.1)
    mHand.setheading(degree)
    window.ontimer(movemHand,1000)

def movesHand():
    currentsecondInternal = datetime.datetime.now().second
    degree = (currentsecondInternal - 15) * -6
    sHand.setheading(degree)
    window.ontimer(movesHand, 1000)

window.ontimer(movehHand, 1)
window.ontimer(movemHand, 1)
window.ontimer(movesHand, 1)
window.exitonclick()