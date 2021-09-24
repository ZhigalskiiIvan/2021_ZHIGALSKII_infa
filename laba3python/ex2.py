import turtle

lenbit = 20
diagonal = (2 ** 0.5)*lenbit
dlinlenbin = 2 * lenbit

def printzero():
    global lenbit
    global diagonal
    global dlinlenbin
    turtle.pendown()
    turtle.forward(lenbit)
    turtle.right(90)
    turtle.forward(dlinlenbin)
    turtle.right(90)
    turtle.forward(lenbit)
    turtle.right(90)
    turtle.forward(dlinlenbin)
    turtle.right(90)
    turtle.penup()
    turtle.forward(dlinlenbin)

def printone():
    global lenbit
    global diagonal
    global dlinlenbin
    turtle.right(90)
    turtle.forward(lenbit)
    turtle.pendown()
    turtle.left(135)
    turtle.forward(diagonal)
    turtle.right(135)
    turtle.forward(dlinlenbin)
    turtle.penup()
    turtle.left(180)
    turtle.forward(dlinlenbin)
    turtle.right(90)
    turtle.forward(lenbit)

def printtwo():
    global lenbit
    global diagonal
    global dlinlenbin
    turtle.pendown()
    turtle.forward(lenbit)
    turtle.right(90)
    turtle.forward(lenbit)
    turtle.right(45)
    turtle.forward(diagonal)
    turtle.left(135)
    turtle.forward(lenbit)
    turtle.penup()
    turtle.left(90)
    turtle.forward(dlinlenbin)
    turtle.right(90)
    turtle.forward(lenbit)

def printthree():
    global lenbit
    global diagonal
    global dlinlenbin
    turtle.pendown()
    turtle.forward(lenbit)
    turtle.right(135)
    turtle.forward(diagonal)
    turtle.left(135)
    turtle.forward(lenbit)
    turtle.right(135)
    turtle.forward(diagonal)
    turtle.penup()
    turtle.right(135)
    turtle.forward(dlinlenbin)
    turtle.right(90)
    turtle.forward(dlinlenbin)

def printfour():
    global lenbit
    global diagonal
    global dlinlenbin
    turtle.right(90)
    turtle.pendown()
    turtle.forward(lenbit)
    turtle.left(90)
    turtle.forward(lenbit)
    turtle.right(90)
    turtle.forward(lenbit)
    turtle.left(180)
    turtle.forward(dlinlenbin)
    turtle.penup()
    turtle.right(90)
    turtle.forward(lenbit)

def printfive():
    global lenbit
    global diagonal
    global dlinlenbin
    turtle.forward(lenbit)
    turtle.pendown()
    turtle.right(180)
    turtle.forward(lenbit)
    turtle.left(90)
    turtle.forward(lenbit)
    turtle.left(90)
    turtle.forward(lenbit)
    turtle.right(90)
    turtle.forward(lenbit)
    turtle.right(90)
    turtle.forward(lenbit)
    turtle.right(180)
    turtle.penup()
    turtle.forward(lenbit)
    turtle.left(90)
    turtle.forward(dlinlenbin)
    turtle.right(90)
    turtle.forward(lenbit)

def printsix():
    global lenbit
    global diagonal
    global dlinlenbin
    turtle.forward(lenbit)
    turtle.pendown()
    turtle.right(135)
    turtle.forward(diagonal)
    turtle.left(45)
    turtle.forward(lenbit)
    turtle.left(90)
    turtle.forward(lenbit)
    turtle.left(90)
    turtle.forward(lenbit)
    turtle.left(90)
    turtle.forward(lenbit)
    turtle.right(135)
    turtle.penup()
    turtle.forward(diagonal)
    turtle.right(45)
    turtle.forward(lenbit)

def printseven():
    global lenbit
    global diagonal
    global dlinlenbin
    turtle.pendown()
    turtle.forward(lenbit)
    turtle.right(135)
    turtle.forward(diagonal)
    turtle.left(45)
    turtle.forward(lenbit)
    turtle.penup()
    turtle.left(180)
    turtle.forward(dlinlenbin)
    turtle.right(90)
    turtle.forward(dlinlenbin)

def printeight():
    global lenbit
    global diagonal
    global dlinlenbin
    turtle.pendown()
    turtle.right(90)
    turtle.forward(dlinlenbin)
    turtle.left(90)
    turtle.forward(lenbit)
    turtle.left(90)
    turtle.forward(lenbit)
    turtle.left(90)
    turtle.forward(lenbit)
    turtle.right(180)
    turtle.forward(lenbit)
    turtle.left(90)
    turtle.forward(lenbit)
    turtle.left(90)
    turtle.forward(lenbit)
    turtle.right(180)
    turtle.penup()
    turtle.forward(dlinlenbin)

def printnine():
    global lenbit
    global diagonal
    global dlinlenbin
    turtle.forward(lenbit)
    turtle.right(90)
    turtle.forward(lenbit)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(lenbit)
    turtle.right(90)
    turtle.forward(lenbit)
    turtle.right(90)
    turtle.forward(lenbit)
    turtle.right(90)
    turtle.forward(lenbit)
    turtle.right(45)
    turtle.forward(diagonal)
    turtle.left(135)
    turtle.penup()
    turtle.forward(lenbit)
    turtle.left(90)
    turtle.forward(dlinlenbin)
    turtle.right(90)
    turtle.forward(lenbit)

def printnumber(k):
    if k == 0:
        printzero()
    elif k == 1:
        printone()
    elif k == 2:
        printtwo()
    elif k == 3:
        printthree()
    elif k == 4:
        printfour()
    elif k == 5:
        printfive()
    elif k == 6:
        printsix()
    elif k == 7:
        printseven()
    elif k == 8:
        printeight()
    elif k == 9:
        printnine()



index = tuple(input())

turtle.shape('turtle')
turtle.speed(4)
turtle.penup()


try:
    for k in index:
        printnumber(int(k))
except:
    print("ошибка")

turtle.hideturtle()

turtle.exitonclick()
