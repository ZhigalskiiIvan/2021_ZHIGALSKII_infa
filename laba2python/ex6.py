import turtle as t

n = int(input("Ввод: "))

t.shape('turtle')
t.speed(0.5000000000005)

for k in range(n):
    t.forward(40)
    t.stamp()
    t.right(180)
    t.forward(40)
    t.left(180 - 360 / n)

t.exitonclick()
