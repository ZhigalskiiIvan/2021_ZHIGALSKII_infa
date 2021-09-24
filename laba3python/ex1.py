import random as rnd
import turtle

turtle.shape('turtle')
turtle.speed(7)

def binchislo():    
    return round(rnd.random())

def angle():
    return 180 * rnd.random()

def chislo():
    return 40 * rnd.random()

def deistvie():
    turtle.forward(chislo())
    if binchislo() == 1:
        turtle.left(angle())
    else:
        turtle.right(angle())

while True:
    deistvie()

turtle.exitonclick()
