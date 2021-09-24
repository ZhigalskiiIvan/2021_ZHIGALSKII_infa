import turtle as t

t.shape('turtle')
t.speed(2)
t.width(1)


def printstar(n):
    t.pendown()
    for i in range(n):
        starangle = 180 / n
        rotateangle = 180 - starangle
        printlines(n, rotateangle)
    if n % 2 == 0:
        printlines(n, rotateangle)
    t.penup()


def printlines(n, angle):
    global razmer
    t.forward(razmer)
    t.left(angle)


n = 100
razmer = 200

t.penup()
t.right(180)
t.forward(200)
t.left(180)
printstar(5)
t.forward(300)
printstar(14)

t.exitonclick()
