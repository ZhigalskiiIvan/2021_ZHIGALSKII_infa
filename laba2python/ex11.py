import turtle as t

t.shape('turtle')
t.speed(0)
t.left(90)


def paintfigure(n, razmer, napravlenie):
    startrazmer = 20 / n
    if napravlenie == "left":
        for i in range(n):
            t.forward(startrazmer + razmer)
            t.left(360 / n)
    else:
        for i in range(n):
            t.forward(startrazmer + razmer)
            t.right(360 / n)


def paintkrilia(n, razmer):
    paintfigure(n, razmer, "left")
    paintfigure(n, razmer, "right")


n = 100
razmer = 3

for i in range(10):
    paintkrilia(n, razmer)
    razmer += 0.5

t.exitonclick()
