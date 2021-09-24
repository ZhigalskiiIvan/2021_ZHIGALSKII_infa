import random
import turtle
import math

number_of_turtles = 20
steps_of_time_number = 10000000
r = 300
beginspeed = 400
dt = 0.01
k_hitforce = 1000000
weight = 0.0001
k_gravityforce = 10000
deggravity = 1
hitdistanse = 15

pool = [turtle.Turtle(shape = "circle") for i in range(number_of_turtles)]
for unit in pool:
    unit.speed(0)
pool[0].penup()
pool[0].goto(-r, -r)
pool[0].pendown()
pool[0].goto(-r, r)
pool[0].goto(r, r)
pool[0].goto(r, -r)
pool[0].goto(-r, -r)
for unit in pool:
    unit.speed(100)

def randbegincor():
    return random.randint(-r, r)

def randbeginxspeed():
    return random.randint(-beginspeed, beginspeed)

coor = [[0, 0] for i in range(number_of_turtles)]
speed = [[0, 0] for i in range(number_of_turtles)]
acs = [[0,0] for i in range(number_of_turtles)]
gravityforce = [[0,0] for i in range(number_of_turtles)]
hitforce = [[0,0] for i in range(number_of_turtles)]
m = [weight for i in range(number_of_turtles)]

gforce = 100000

for i in range(len(pool)):
    unit = pool[i]
    unit.penup()
    speed[i][0] = (-1) ** (random.randint(0, 1)) * random.random() * beginspeed
    speed[i][1] = (-1) ** (random.randint(0, 1)) * math.sqrt(beginspeed ** 2 - speed[i][0] ** 2)
    coor[i][0] = randbegincor()
    coor[i][1] = randbegincor()
    unit.goto(tuple(coor[i]))

    
for i in range(steps_of_time_number):
    for j in range(len(pool)):

        unit = pool[j]

        for k in range(len(coor)):
            if k == j:
                pass
            else:
                x1 = coor[j][0]
                y1 = coor[j][1]
                m1 = m[j]
                m2 = m[k]
                x2 = coor[k][0]
                y2 = coor[k][1]
                m2 = m[k]
                rast = math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
                if rast <= 1.5 * hitdistanse:
                    sinalpha = (y1 - y2) / rast
                    cosalpha = (x1 - x2) / rast
                    udarforce = k_gravityforce
                    udarforceX = udarforce * cosalpha
                    udarforceY = udarforce * sinalpha
                    gravityforce[j][0] = udarforceX
                    gravityforce[j][1] = udarforceY
                    gravityforce[k][0] = -udarforceX
                    gravityforce[k][1] = -udarforceY



        if -(coor[j][0] - r) <= hitdistanse:
            try:
                hitforce[j][0] = -gforce
            except:
                pass
        elif coor[j][0] + r <= hitdistanse:
            hitforce[j][0] = gforce
        else:
            hitforce[j][0] = 0

        if -(coor[j][1] - r) <= hitdistanse:
            try:
                hitforce[j][1] = -gforce
            except:
                pass
        elif coor[j][1] + r <= hitdistanse:
            hitforce[j][1] = gforce
        else:
            hitforce[j][1] = 0
        
        acs[j][0] = (gravityforce[j][0] + hitforce[j][0]) / m[j]
        acs[j][1] = (gravityforce[j][1] + hitforce[j][1]) / m[j]

        gravityforce[j][1] = 0
        gravityforce[j][0] = 0
        
        speed[j][0] += acs[j][0] * dt
        speed[j][1] += acs[j][1] * dt

        if abs(acs[j][0]) > 0 or abs(acs[j][1]) > 0:
            while speed[j][0] ** 2 + speed[j][1] ** 2 < beginspeed ** 2:
                speed[j][0] += acs[j][0] * dt
                speed[j][1] += acs[j][1] * dt
        
        if (speed[j][0] ** 2 + speed[j][1] ** 2) >= beginspeed ** 2:
            otnoshenie = math.sqrt(beginspeed ** 2 / (speed[j][0] ** 2 + speed[j][1] ** 2))
            speed[j][0] *= otnoshenie
            speed[j][1] *= otnoshenie

        coor[j][0] += speed[j][0] * dt 
        coor[j][1] += speed[j][1] * dt 
        
        unit.goto(coor[j][0], coor[j][1])


turtle.exitonclick()