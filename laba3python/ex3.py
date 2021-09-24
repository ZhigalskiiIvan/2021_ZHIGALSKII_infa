import turtle


lenbit = 20
diagonal = (2 ** 0.5)*lenbit
dlinlenbin = 2 * lenbit


def readF (filenumber):
    filename = "laba3python/digits/" + str(filenumber) + ".txt"
    with open(filename, "r") as F:
        for line in F.readlines():
            eval(line)

def printdigit(k):
    if k == 0:
        readF(0)
    if k == 1:
        readF(1)
    if k == 2:
        readF(2)
    if k == 3:
        readF(3)
    if k == 4:
        readF(4)
    if k == 5:
        readF(5)
    if k == 6:
        readF(6)
    if k == 7:
        readF(7)
    if k == 8:
        readF(8)
    if k == 9:
        readF(9)
    
    

index = tuple(input())

turtle.shape('turtle')
turtle.speed(4)
turtle.penup()

for k in index:
    printdigit(int(k))

turtle.exitonclick()