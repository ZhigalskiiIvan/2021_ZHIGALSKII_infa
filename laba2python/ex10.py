import turtle as t

t.shape('turtle')
t.speed(10)


def paintfigure(n, napravlenie):
    for i in range(n):
        t.forward(500 / n)
        if napravlenie == "left":
            t.left(360 / n)
        else:
            t.right(360 / n)


for i in range(3):
    paintfigure(100, "left")
    paintfigure(100, "right")
    t.left(60)

t.exitonclick()
