import turtle as t

t.shape('turtle')
t.speed(0)
t.width(1)


def paintokr(n, razmer, napravlenie):
    if napravlenie == "left":
        for i in range(n):
            t.left(360 / n)
            t.forward(razmer)

    else:
        for i in range(n):
            t.right(360 / n)
            t.forward(razmer)


def paintpoluokr(n, razmer, napravlenie):
    if napravlenie == "left":
        for i in range(n):
            t.forward(razmer)
            t.left(180 / n)
    else:
        for i in range(n):
            t.forward(razmer)
            t.right(180 / n)


def printeye(n, razmer, napravlenie):
    t.pendown()
    t.begin_fill()
    paintokr(n, razmer / 2, napravlenie)
    t.color("blue")
    t.end_fill()
    t.color("black")
    t.penup()


def printface(n, razmer, napravlenie):
    t.pendown()
    t.begin_fill()
    paintokr(n, 4 * razmer, napravlenie)
    t.color("yellow")
    t.end_fill()
    t.color("black")
    t.penup()


def printnose(nosesize):
    t.pendown()
    t.width(7)
    t.forward(nosesize)
    t.width(1)
    t.penup()


def printmouth(n, razmer, napravlenie):
    t.pendown()
    t.width(8)
    t.color("red")
    paintpoluokr(n, razmer, napravlenie)
    t.color("black")
    t.width(1)
    t.penup()


n = 100
razmer = 2
nosesize = 40

t.penup()
t.left(90)
t.forward(90)
t.left(90)
printface(n, razmer, "left")
t.left(90)
t.forward(80)
t.right(90)
t.forward(35)
t.right(90)
printeye(n, razmer, "left")
t.right(90)
t.forward(70)
t.left(90)
printeye(n, razmer, "right")
t.left(90)
t.forward(35)
t.left(90)
t.forward(30)
printnose(nosesize)
t.forward(15)
t.left(90)
t.forward(65)
t.right(90)
printmouth(n, razmer, "right")
t.shape("classic")
t.color("red")
t.forward(1000000)

t.exitonclick()
