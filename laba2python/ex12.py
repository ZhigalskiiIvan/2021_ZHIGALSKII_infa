import turtle as t

t.shape('turtle')
t.speed(0)
t.left(90)


def paintpoluokr(n, razmer, napravlenie):
    startrazmer = 0
    if napravlenie == "left":
        for i in range(n):
            t.forward(startrazmer + razmer)
            t.left(180 / n)
    else:
        for i in range(n):
            t.forward(startrazmer + razmer)
            t.right(180 / n)


def paintzveno(n, razmer):
    paintpoluokr(n, razmer, "right")
    paintpoluokr(n // 3, razmer / 3, "right")


n = 100
razmer = 1.5

for i in range(4):
    paintzveno(n, razmer)

paintpoluokr(n, razmer, "right")

t.exitonclick()
