import pygame
from math import pi, cos, sin, radians
from pygame.draw import rect, ellipse, arc, polygon

pygame.init()

pandaColorLight = "WHITE"
pandaColorDark = "BlACK"
screenColor = "#FFAF79"
plantColor = "#00FF00"
plantColor = "DARKGREEN"

countEarCords = 1000

rEarLeft = 80
arcEarLeft = 200
leftEarAngle = 110

rEarRight = 80
arcEarRight = -220
rightEarAngle = 110

aNose = 65
bNose = 45
aLeftEye = 45
bLeftEye = 60
aRightEye = 60
bRightEye = 60

pandaX = 900
pandaY = 450
smallPandaX = 2000
smallPandaY = 2000
kPanda = 0.9
kSmallPanda = 0.3

palmaX1 = 150
palmaY1 = 400
palmaX2 = 400
palmaY2 = 420
palmaX3 = 600
palmaY3 = 420
palmaX4 = 1200
palmaY4 = 420
kPalma1 = 0.8
kPalma2 = 0.9
kPalma3 = 1.6
kPalma4 = 1.3


podgonX1 = 140
podgonY1 = 330
podgonX2 = 0
podgonY2 = 300
podgonX3 = -10
podgonY3 = 335
podgonXface = -140
podgonYface = 60
podgonXhead = 100
podgonYhead = 100
podgonXLeftEar = -115
podgonYLeftEar = -90
podgonXRightEar = 100
podgonYRightEar = -80
podgonXNose = -90
podgonYNose = 0
podgonXLeftEye = -110
podgonYLeftEye = -70
podgonXRightEye = -40
podgonYRightEye = -60

unitLength = 10
kAbody = 40
kBbody = 20

deltaXPaw1 = unitLength * 5
deltaXPaw2 = unitLength * 0
deltaXPaw3 = unitLength * (-5)
deltaYPaw1 = unitLength * 5
deltaYPaw2 = unitLength * 10
deltaYPaw3 = unitLength * 0

deltaX1 = 40
deltaY1 = 60

kPaw1 = 2
kPaw2 = 1.2
kPaw3 = 2
kFace = 1.9

FPS = 60
screen = pygame.display.set_mode((1400, 750))
screen.fill(screenColor)


def drawEarLeft(x, y, k):
    leftEarCords = [0] * countEarCords
    kEllipseMosiv = [(2 * sin((i / (countEarCords)))) / 2 for i in range(countEarCords)]
    angleEarLeftMosiv = [((arcEarLeft / countEarCords) * i + leftEarAngle) for i in range(countEarCords)]
    for i in range(countEarCords):
        leftEarCords[i] = [x + round(rEarLeft * k * cos(radians(angleEarLeftMosiv[i])) * kEllipseMosiv[i]),
                           y + round(rEarLeft * k * sin(radians(angleEarLeftMosiv[i])) * kEllipseMosiv[i])]
    polygon(screen, pandaColorDark, leftEarCords)


def drawEarRight(x, y, k):
    rightEarCords = [0] * countEarCords
    kEllipseMosiv = [(2 * sin((i / (countEarCords)))) / 2 for i in range(countEarCords)]
    angleEarRightMosiv = [((arcEarRight / countEarCords) * i + rightEarAngle) for i in range(countEarCords)]
    for i in range(countEarCords):
        rightEarCords[i] = [x + round(rEarRight * k * cos(radians(angleEarRightMosiv[i])) * kEllipseMosiv[i]),
                            y + round(rEarRight * k * sin(radians(angleEarRightMosiv[i])) * kEllipseMosiv[i])]
    polygon(screen, pandaColorDark, rightEarCords)


def drawface(x, y, k):
    imageFace = pygame.image.load('pngs/face.png')
    sizeFace = imageFace.get_size()
    sizeFace = list(sizeFace)
    sizeFace = round((sizeFace[0]) * k / kFace), round((sizeFace[1]) * k / kFace)
    imageFace = pygame.transform.scale(imageFace, sizeFace)
    rectFace = imageFace.get_rect(bottomleft=(x + podgonXface * k, y + podgonYface * k))
    screen.blit(imageFace, rectFace)


def drawnose(x, y, k):
    x, y = x + podgonXNose * k, y + podgonYNose * k
    ellipse(screen, pandaColorDark, (x, y, aNose * k, bNose * k))


def draweyes(x, y, k):
    drawlefteye(x, y, k)
    drawrighteye(x, y, k)


def drawlefteye(x, y, k):
    x, y = round(x + podgonXLeftEye * k), round(y + podgonYLeftEye * k)
    ellipse(screen, pandaColorDark, (x, y, aLeftEye * k, bLeftEye * k))


def drawrighteye(x, y, k):
    x, y = round(x + podgonXRightEye * k), round(y + podgonYRightEye * k)
    ellipse(screen, pandaColorDark, (x, y, aRightEye * k, bRightEye * k))


def drawears(x, y, k):
    xLeft = x + podgonXLeftEar * k
    yLeft = y + podgonYLeftEar * k
    xRight = x + podgonXRightEar * k
    yRight = y + podgonYRightEar * k
    drawEarLeft(xLeft, yLeft, k)
    drawEarRight(xRight, yRight, k)


def drawhead(pandaX, pandaY, k):
    x, y = round(pandaX + podgonXhead * k), round(pandaY + podgonYhead * k)
    drawface(x, y, k)
    drawnose(x, y, k)
    draweyes(x, y, k)
    drawears(x, y, k)


def drawpandabody(x, y, k):
    a = kAbody * unitLength * k
    b = kBbody * unitLength * k
    color = pandaColorLight
    ellipse(screen, color, (x, y, a, b))


def drawpandapaw1(x, y, k):
    imagePaw1 = pygame.image.load('pngs/paw1.png')
    sizePaw1 = imagePaw1.get_size()
    sizePaw1 = list(sizePaw1)
    sizePaw1 = round((sizePaw1[0]) * k / kPaw1), round((sizePaw1[1]) * k / kPaw1)
    imagePaw1 = pygame.transform.scale(imagePaw1, sizePaw1)
    rectPaw1 = imagePaw1.get_rect(bottomleft=(x + podgonX1 * k, y + podgonY1 * k))
    screen.blit(imagePaw1, rectPaw1)


def drawpandapaw2(x, y, k):
    imagePaw2 = pygame.image.load('pngs/paw2.png')
    sizePaw2 = imagePaw2.get_size()
    sizePaw2 = list(sizePaw2)
    sizePaw2 = round((sizePaw2[0]) * k / kPaw2), round((sizePaw2[1]) * k / kPaw2)
    imagePaw2 = pygame.transform.scale(imagePaw2, sizePaw2)
    rectPaw2 = imagePaw2.get_rect(bottomleft=(x + podgonX2 * k, y + podgonY2 * k))
    screen.blit(imagePaw2, rectPaw2)


def drawpandapaw3(x, y, k):
    imagePaw3 = pygame.image.load('pngs/paw3.png')
    sizePaw3 = imagePaw3.get_size()
    sizePaw3 = list(sizePaw3)
    sizePaw3 = round((sizePaw3[0]) * k / kPaw2), round((sizePaw3[1]) * k / kPaw2)
    imagePaw3 = pygame.transform.scale(imagePaw3, sizePaw3)
    rectPaw3 = imagePaw3.get_rect(bottomleft=(x + podgonX3 * k, y + podgonY3 * k))
    screen.blit(imagePaw3, rectPaw3)


def drawpandapaws(pandaX, pandaY, k):
    drawpandapaw1(pandaX + deltaXPaw1 * k, pandaY + deltaYPaw1 * k, k)
    drawpandapaw2(pandaX + deltaXPaw2 * k, pandaY + deltaYPaw2 * k, k)
    drawpandapaw3(pandaX + deltaXPaw3 * k, pandaY + deltaYPaw3 * k, k)


def drawpanda(pandaX, pandaY, k):
    drawpandabody(pandaX * k, pandaY * k, k)
    drawpandapaws(pandaX * k, pandaY * k, k)
    drawhead(pandaX * k, pandaY * k, k)


def drawtrunk(x, y, kPalma):
    uL = kPalma  # unitLength
    rect(screen, plantColor, (x, y, 20 * uL, 80 * uL))
    rect(screen, plantColor, (x + 3 * uL, y - 85 * uL, 15 * uL, 80 * uL))
    polygon(screen, plantColor, ([x + 6 * uL, y - 92 * uL],
                                 [x + 12 * uL, y - 90 * uL],
                                 [x + 30 * uL, y - 170 * uL],
                                 [x + 24 * uL, y - 172 * uL]))
    polygon(screen, plantColor, ([x + 26 * uL, y - 178 * uL],
                                 [x + 30 * uL, y - 176 * uL],
                                 [x + 66 * uL, y - 250 * uL],
                                 [x + 62 * uL, y - 252 * uL]))


def drawrotateleaf(color, x, y, kPalma, rotateAngle):
    leafCords = [0] * 400
    angleLeafMosiv = [((360 / 400) * i + 60) for i in range(400)]
    for i in range(400):
        leafCords[i] = [round(x + 20 * cos(radians(angleLeafMosiv[i])) * kPalma),
                        round(y + 30 * sin(radians(angleLeafMosiv[i] + rotateAngle)) * kPalma)]
    polygon(screen, color, leafCords)


def drawleaves(x, y, kPalma):
    uL = kPalma

    drawrotateleaf("DARKGREEN", x + 200 * uL, y - 215 * uL, uL, 110)
    drawrotateleaf("DARKGREEN", x + 180 * uL, y - 215 * uL, uL, 110)
    drawrotateleaf("DARKGREEN", x + 160 * uL, y - 213 * uL, uL, 110)
    drawrotateleaf("DARKGREEN", x + 140 * uL, y - 208 * uL, uL, 110)
    drawrotateleaf("DARKGREEN", x + 120 * uL, y - 200 * uL, uL, 110)

    drawrotateleaf("DARKGREEN", x - 150 * uL, y - 185 * uL, uL, -110)
    drawrotateleaf("DARKGREEN", x - 130 * uL, y - 185 * uL, uL, -110)
    drawrotateleaf("DARKGREEN", x - 110 * uL, y - 182 * uL, uL, -110)
    drawrotateleaf("DARKGREEN", x - 90 * uL, y - 179 * uL, uL, -110)
    drawrotateleaf("DARKGREEN", x - 70 * uL, y - 173 * uL, uL, -110)

    drawrotateleaf("DARKGREEN", x + 135 * uL, y - 100 * uL, uL * 0.8, 110)
    drawrotateleaf("DARKGREEN", x + 120 * uL, y - 100 * uL, uL * 0.8, 110)
    drawrotateleaf("DARKGREEN", x + 105 * uL, y - 98 * uL, uL * 0.8, 110)
    drawrotateleaf("DARKGREEN", x + 90 * uL, y - 93 * uL, uL * 0.8, 110)
    drawrotateleaf("DARKGREEN", x + 75 * uL, y - 85 * uL, uL * 0.8, 110)

    drawrotateleaf("DARKGREEN", x - 115 * uL, y - 70 * uL, uL * 0.8, -110)
    drawrotateleaf("DARKGREEN", x - 100 * uL, y - 70 * uL, uL * 0.8, -110)
    drawrotateleaf("DARKGREEN", x - 85 * uL, y - 67 * uL, uL * 0.8, -110)
    drawrotateleaf("DARKGREEN", x - 71 * uL, y - 61 * uL, uL * 0.8, -110)
    drawrotateleaf("DARKGREEN", x - 59 * uL, y - 53 * uL, uL * 0.8, -110)


def drawbranches(x, y, kPalma):
    uL = kPalma  # unitLength
    arc(screen, plantColor, (x + 15 * uL, y - 130 * uL, 200 * uL, 200 * uL), pi / 3, 7 * pi / 8, width=4)
    arc(screen, plantColor, (x + 30 * uL, y - 250 * uL, 300 * uL, 200 * uL), pi / 3, 7 * pi / 8, width=4)
    arc(screen, plantColor, (x - 195 * uL, y - 100 * uL, 200 * uL, 200 * uL), pi / 8, 2 * pi / 3, width=4)
    arc(screen, plantColor, (x - 270 * uL, y - 220 * uL, 300 * uL, 200 * uL), pi / 8, 2 * pi / 3, width=4)
    drawleaves(x, y, kPalma)


def drawpalma(x, y, kPalma):
    drawbranches(x, y, kPalma)
    drawtrunk(x, y, kPalma)


drawpanda(pandaX, pandaY, kPanda)
drawpanda(smallPandaX, smallPandaY, kSmallPanda)

drawpalma(palmaX1, palmaY1, kPalma1)
drawpalma(palmaX2, palmaY2, kPalma2)
drawpalma(palmaX3, palmaY3, kPalma3)
drawpalma(palmaX4, palmaY4, kPalma4)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
