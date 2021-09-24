import turtle
import math

def rad_in_deg (angle):
    angle = 180 * angle / math.pi
    return angle

def angle(v_x, v_y, v1_x, v1_y):
    angle1 = math.atan(v1_y/v1_x)
    angle = math.atan(v_y/v_x)
    dalpha = abs(angle1 - angle)
    return dalpha

def alphaudar(v_x, v_y, v1_x, v1_y):
    alpha1 = math.atan(v1_y / v1_x)
    alpha = math.atan(v_y / v_x)
    povorot = alpha - alpha1
    return povorot

razmerpola = 1000
zapas = 350
v0_y = 50
v0_x = 15
k_lost = 0.8
x = -350
y = 0

v_x = v0_x
v_y = v0_y 
a_y = -10
angle_0 = math.atan(v0_y/v0_x)
angle_0 = rad_in_deg(angle_0)

countjump = 20

dt = 0.08

turtle.speed(0)
turtle.forward(razmerpola)
turtle.left(180)
turtle.forward(2*razmerpola)
turtle.left(180)
turtle.forward(razmerpola-zapas)
turtle.left(angle_0)

for i in range(countjump):
    while y >= 0:
        v1_x = v_x
        v1_y = v_y
        x += v_x * dt
        y += v_y *dt + (a_y*dt**2)/2
        v_y += a_y*dt
        turtle.goto(x, y)
        dalpha = angle(v_x, v_y, v1_x, v1_y)
        dalpha = rad_in_deg(dalpha)
        turtle.right(dalpha)

    y = 0
    v1_x = v_x
    v1_y = v_y
    v_y = -(k_lost*v_y)
    dalpha = alphaudar(v_x, v_y, v1_x, v1_y) 
    dalpha = rad_in_deg(dalpha)
    turtle.left(dalpha)

turtle.exitonclick()