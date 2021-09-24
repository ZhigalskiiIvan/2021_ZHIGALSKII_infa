import turtle as t

t.shape('turtle')
t.speed(0)

for k in range(300):
    delta = (k / 10)
    t.forward(delta)
    t.left(10)

t.exitonclick()
