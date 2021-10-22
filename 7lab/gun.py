import math
from math import sin, cos
import random
from random import choice, randint

import pygame

FPS = 200

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

accseleration = 700

gunLength = 100
defaultPower = 300
maxPower = 1500
defaultGunX0 = -50
defaultGunY0 = 450


class Ball:
    def __init__(self, screen: pygame.Surface, _x=defaultGunX0, _y=defaultGunY0):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        vx - начальная скорость мяча по горизонтали
        vy - начальная скорость мяча по вертикали
        """
        self.screen = screen
        self.x = _x
        self.y = _y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self, _deltatime):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.vy -= accseleration * _deltatime
        if self.x >= 800 - self.r:
            self.vx *= (-1)
        if self.y >= 600 - self.r:
            self.vy = round((-0.7) * self.vy)
            self.vx *= 0.7
        self.x += self.vx * _deltatime
        self.y -= self.vy * _deltatime

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if isinstance(obj, Target):
            dist = math.sqrt((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2)
            if dist <= self.r + obj.r:
                return True
        return False


class Gun:
    def __init__(self, screen):
        self.x0 = defaultGunX0
        self.y0 = defaultGunY0
        self.a = gunLength
        self.b = 20
        self.x = self.x0 + self.a
        self.y = self.y0 + self.b
        self.screen = screen
        self.f2_power = 20
        self.f2_on = False
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = True

    def fire2_end(self, _event, _balls, _bullet):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        _bullet += 1
        new_ball = Ball(self.screen)
        if (_event.pos[0] - new_ball.x) != 0:
            self.an = math.atan2((_event.pos[1] - new_ball.y), (_event.pos[0] - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        _balls.append(new_ball)
        self.f2_on = False
        self.f2_power = defaultPower
        self.a = gunLength
        return _bullet, _balls

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if (event.pos[0] - 20) != 0:
                self.an = math.atan((event.pos[1] - 450) / (event.pos[0] - 20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        x = self.x0
        y = self.y0
        a = self.a
        b = self.b
        angle = self.an
        pygame.draw.polygon(self.screen, self.color, [[x, y], [x + a * cos(angle), y + a * sin(angle)],
                                                      [x + a * cos(angle) + b * sin(angle),
                                                       y + a * sin(angle) - b * cos(angle)],
                                                      [x + b * sin(angle), y - b * cos(angle)]])

    def power_up(self):
        if self.f2_on:
            if self.f2_power < maxPower:
                self.f2_power += (maxPower - defaultPower) / 100
                self.a += 1
            self.color = RED
        else:
            self.color = GREY


class Target:

    def __init__(self):
        self.color = RED
        self.r = randint(2, 50)
        self.y = randint(300, 550)
        self.x = randint(600, 780)
        self.screen = screen
        self.points = 0
        self.live = 1

    def new_target(self):
        """ Инициализация новой цели. """
        self.r = randint(2, 50)
        self.y = randint(300, 550)
        self.x = randint(600, 780)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points
        self.live -= 1
        if self.live == 0:
            self.live = 1
            self.new_target()

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
target = Target()
finished = False
deltatime = 1 / FPS

while not finished:
    screen.fill(WHITE)
    gun.draw()
    target.draw()
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            bullet, balls = gun.fire2_end(event, balls, bullet)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        b.move(deltatime)
        if b.hittest(target) and target.live:
            target.live = 0
            target.hit()
            target.new_target()
    gun.power_up()

pygame.quit()
