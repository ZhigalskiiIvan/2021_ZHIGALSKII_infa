import pygame
from math import radians, cos, sin
from pygame.draw import rect, line, circle

pygame.init()

groundColor = "#EEEEEE"
plantColor = "#00FF00"
faceColor = "YELLOW"
eyesColor = "RED"
faceEdgeColor = "BLACK"
eyesEdgeColor = "BLACK"
mouthColor = "BLACK"
browColor = "BLACK"

screenwidth = 1400
screenheight = 750

faceX = 700
faceY = 300
faceRadius = 200

browXLeft = faceX - 30
browYLeft = faceY - 100
browXRight = faceX + 130
browYRight = faceY - 160
browALeft = 140
browARight = 100
browWidthLeft = 30
browWidthRight = 25
browAngleLeft = 30
browAngleRight = -40

mouthA = 200
mouthB = 40
mouthX = faceX - mouthA // 2
mouthY = faceY + 90

eyeRadiusLeft = 30
eyeXLeft = faceX - 80
eyeYLeft = faceY - 80

eyeRadiusRight = 20
eyeXRight = faceX + 80
eyeYRight = faceY - 80

FPS = 60
screen = pygame.display.set_mode((screenwidth, screenheight))
screen.fill(groundColor)


def drawbrows(browColor, x1, y1, a1, browWidthLeft, alpha1, x2, y2, a2, browWidthRight, alpha2):
    drawline(browColor, x1, y1, x1 - a1 * cos(radians(alpha1)), y1 - a1 * sin(radians(alpha1)), browWidthLeft)
    drawline(browColor, x2, y2, x2 - a2 * cos(radians(alpha2)), y2 - a2 * sin(radians(alpha2)), browWidthRight)


def drawline(browColor, x0, y0, x, y, _width):
    line(screen, browColor, (x0, y0), (x, y), width=_width)


def draweyes(eyesColor, eyeXLeft, eyeYLeft, eyeRadiusLeft, eyeXRight, eyeYRight, eyeRadiusRight, edgeColor):
    drawcircle(eyesColor, eyeRadiusLeft, eyeXLeft, eyeYLeft, edgeColor)
    drawcircle("BLACK", eyeRadiusLeft / 2, eyeXLeft, eyeYLeft, edgeColor)  # left eye width pupil and edge

    drawcircle(eyesColor, eyeRadiusRight, eyeXRight, eyeYRight, edgeColor)
    drawcircle("BLACK", eyeRadiusRight / 2, eyeXRight, eyeYRight, edgeColor)


def drawcircle(color, r, x0, y0, edgeColor):
    circle(screen, color, (x0, y0), r)  # draw circle with edge
    circle(screen, edgeColor, (x0, y0), r, width=1)


def drawrect(x0, y0, a, b, color):
    rect(screen, color, (x0, y0, a, b))


def drawface(faceColor, faceEdgeClor, faceX, faceY, faceRadius):
    drawcircle(faceColor, faceRadius, faceX, faceY, faceEdgeClor)


def drawmouth(mouthX, mouthY, mouthA, mouthB, mouthColor):
    drawrect(mouthX, mouthY, mouthA, mouthB, mouthColor)


drawface(faceColor, faceEdgeColor, faceX, faceY, faceRadius)
draweyes(eyesColor, eyeXLeft, eyeYLeft, eyeRadiusLeft, eyeXRight, eyeYRight, eyeRadiusRight, eyesEdgeColor)
drawmouth(mouthX, mouthY, mouthA, mouthB, mouthColor)
drawbrows(browColor, browXLeft, browYLeft, browALeft, browWidthLeft, browAngleLeft,
          browXRight, browYRight, browARight, browWidthRight, browAngleRight)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
