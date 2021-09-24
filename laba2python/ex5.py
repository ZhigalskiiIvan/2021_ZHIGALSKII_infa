import turtle as t

t.shape('turtle')
t.speed(0.5)

for k in range(10):
    i = 16 * (k + 1)
    t.forward(i)
    t.left(90)
    t.forward(i)
    t.left(90)
    t.forward(i)
    t.left(90)
    t.forward(i)

    t.penup()

    t.forward(8)
    t.right(90)
    t.forward(8)
    t.right(180)

    t.pendown()
