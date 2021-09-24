import turtle as t

t.shape('turtle')
t.speed(0)
n = 200
for i in range(n):
    t.forward(500 / n)
    t.left(360 / n)

t.exitonclick()
