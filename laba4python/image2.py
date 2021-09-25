import pygame
from math import pi
from pygame.draw import rect, line, ellipse, arc, circle

pygame.init()

pandaColorLight = "WHITE"
pandaColorDark = "BlACK"

screenColor = "#FFAF79"
plantColor = "#00FF00"

pandaX = 600
pandaY = 300

podgonX1 = 140
podgonY1 = 330
podgonX2 = 0
podgonY2 = 300
podgonX3 = -10
podgonY3 = 335
podgonXface = -140
podgonYface = 60

unitLength = 10
kAbody = 40
kBbody = 20

deltaXpaw1 = unitLength * 5
deltaXpaw2 = unitLength * 0
deltaXpaw3 = unitLength * (-5)
deltaYpaw1 = unitLength * 5
deltaYpaw2 = unitLength * 10
deltaYpaw3 = unitLength * 0

deltaX1 = 40
deltaY1 = 60

kPaw1 = 2
kPaw2 = 1.2
kPaw3 = 2
kFace = 1.9

anglePaw2 = 20
anglePaw3 = 0

"""""
def rotatearea(angle):
    rotateZone = pygame.transform.rotate(screen, angle)
    return rotateZone
"""""



FPS = 60
screen = pygame.display.set_mode((1400, 750))
screen.fill(screenColor)

def drawface(x, y):
    imageFace = pygame.image.load('face.png')
    sizeFace = imageFace.get_size()
    sizeFace = list(sizeFace)
    sizeFace = round((sizeFace[0]) / kFace), round((sizeFace[1]) / kFace)
    imageFace = pygame.transform.scale(imageFace, sizeFace)
    rectFace = imageFace.get_rect(bottomleft=(x + podgonXface, y + podgonYface))
    screen.blit(imageFace, rectFace)

def drawnose(x, y):
    pass

def draweyes(x, y):
    pass

def drawmouth(x, y):
    pass

def drawears(x, y):
    pass

def drawhead(pandaX, pandaY):
    x, y = pandaX + 100, pandaY + 100
    drawface(x, y)
    drawnose(x, y)
    draweyes(x, y)
    drawmouth(x, y)
    drawears(x, y)



def drawpandabody(x, y):
    global kAbody, kBbody, unitLength
    a = kAbody * unitLength
    b = kBbody * unitLength
    color = pandaColorLight
    ellipse(screen, color, (x, y, a, b))


def drawpandapaw1(x, y):
    imagePaw1 = pygame.image.load('paw1.png')
    sizePaw1 = imagePaw1.get_size()
    sizePaw1 = list(sizePaw1)
    sizePaw1 = round((sizePaw1[0]) / kPaw1), round((sizePaw1[1]) / kPaw1)
    imagePaw1 = pygame.transform.scale(imagePaw1, sizePaw1)
    rectPaw1 = imagePaw1.get_rect(bottomleft=(x + podgonX1, y + podgonY1))
    screen.blit(imagePaw1, rectPaw1)


def drawpandapaw2(x, y):
    imagePaw2 = pygame.image.load('paw2.png')
    sizePaw2 = imagePaw2.get_size()
    sizePaw2 = list(sizePaw2)
    sizePaw2 = round((sizePaw2[0]) / kPaw2), round((sizePaw2[1]) / kPaw2)
    imagePaw2 = pygame.transform.scale(imagePaw2, sizePaw2)
    rectPaw2 = imagePaw2.get_rect(bottomleft=(x + podgonX2, y + podgonY2))
    screen.blit(imagePaw2, rectPaw2)


def drawpandapaw3(x, y):
    imagePaw3 = pygame.image.load('paw3.png')
    sizePaw3 = imagePaw3.get_size()
    sizePaw3 = list(sizePaw3)
    sizePaw3 = round((sizePaw3[0]) / kPaw2), round((sizePaw3[1]) / kPaw2)
    imagePaw3 = pygame.transform.scale(imagePaw3, sizePaw3)
    rectPaw3 = imagePaw3.get_rect(bottomleft=(x + podgonX3, y + podgonY3))
    screen.blit(imagePaw3, rectPaw3)


def drawpandapaws(pandaX, pandaY):
    global deltaXpaw1, deltaXpaw2, deltaXpaw3, deltaYpaw1, deltaYpaw2, deltaYpaw3
    drawpandapaw1(pandaX + deltaXpaw1, pandaY + deltaYpaw1)
    drawpandapaw2(pandaX + deltaXpaw2, pandaY + deltaYpaw2)
    drawpandapaw3(pandaX + deltaXpaw3, pandaY + deltaYpaw3)


def drawpanda(pandaColorLight, pandaColorDark, pandaX, pandaY):
    global unitLength
    drawpandabody(pandaX, pandaY)
    drawpandapaws(pandaX, pandaY)
    drawhead(pandaX, pandaY)


drawpanda(pandaColorLight, pandaColorDark, pandaX, pandaY)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
