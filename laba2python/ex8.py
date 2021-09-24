import turtle as t

t.shape('turtle')
t.speed(0.6)

for k in range(300):
    delta = (10 * k)
    t.forward(delta)
    t.left(90)

t.exitonclick()
