import turtle as t

t.shape('turtle')
t.speed(10)


def paintfigure(n):
    figureangle = 180 - 360 / n
    anglewthvert = 90 - figureangle / 2
    rotateangle = 360 / n
    anglewthhorizont = figureangle / 2
    line = 10 * n
    t.left(90 + anglewthvert)
    for _ in range(n - 1):
        t.forward(line)
        t.left(rotateangle)
    t.forward(line)
    t.penup()
    t.right(anglewthhorizont)
    t.forward(10 * n / 3)
    t.pendown()


for i in range(10):
    paintfigure((i + 3))

t.exitonclick()
