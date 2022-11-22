from turtle import *
from random import randint
from time import *

finish = 400

t1 = Turtle()
t1.shape('turtle')
t1.color('red')
t1.penup()
t1.goto(-400, 20)
t1.pendown()
t1.speed(0.1)

t2 = Turtle()
t2.shape('turtle')
t2.color('blue')
t2.penup()
t2.goto(-400, -80)
t2.pendown()
t2.speed(0.1)

def razmetka():
    t = Turtle()
    t.speed(0)
    for i in range(1, 41):
        t.penup()
        t.goto(-400 + i * 20, 50)
        t.pendown()
        t.goto(-400 + i * 20, -100)
    t.hideturtle()

razmetka()

def catch1(x,y):
    t1.write('Ouch!', font = ('Arial', 14, 'normal'))
    t1.fd(randint(20,35))

def catch2(x,y):
    t2.write('Ой, как больно!', font = ('Arial', 14, 'normal'))
    t2.fd(randint(20,35))

t1.onclick(catch1)
t2.onclick(catch2)

while t1.xcor()<finish and t2.xcor()<finish:
    t1.forward(randint(2,7))
    t2.forward(randint(2,7))
    sleep(0.05)