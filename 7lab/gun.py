import math
from math import sin, cos
from random import choice, randint
from pygame.font import Font
import pygame

pygame.init()
pygame.font.init()

FPS = 200

fontSize = 45
fontName = 'back-to-1982/BACKTO1982.ttf'
myfont: Font = pygame.font.Font(fontName, fontSize)

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
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
groundY = 570
NextLvlTextTime = 1


class Ball:

    def __init__(self, _screen: pygame.Surface, _x=defaultGunX0, _y=defaultGunY0):
        """
        Конструктор класса Ball
        """
        self.screen = _screen
        self.x = _x
        self.y = _y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.timelive = 3

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.y < groundY - self.r - 5:
            self.vy -= accseleration * deltatime
        if self.x >= 800 - self.r:
            self.vx *= (-1)
        if self.y >= groundY - self.r:
            self.vy = round(0.7 * abs(self.vy))
            self.vx *= 0.7
        self.x += self.vx * deltatime
        self.y -= self.vy * deltatime
        self.timelive -= deltatime

    def update_pic(self):
        """
        обновляет картинку мячика
        """
        if self.timelive <= 0:
            pass
        else:
            pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)

    def hittest(self, obj):
        """
        Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

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

    def __init__(self):
        """
        конструктор класса Gun
        """
        self.x0 = defaultGunX0
        self.y0 = defaultGunY0
        self.a = gunLength
        self.b = 20
        self.screen = screen
        self.f2_power = 20
        self.f2_on = False
        self.an = 1
        self.color = GREY

    def fire2_start(self):
        """
        при нажатии на клавишу мыши включает соответствующий параметр
        """
        self.f2_on = True

    def fire2_end(self, _event, _balls):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        new_ball = Ball(self.screen)
        if (_event.pos[0] - new_ball.x) != 0:
            self.an = math.atan2((_event.pos[1] - new_ball.y), (_event.pos[0] - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        _balls.append(new_ball)
        self.f2_on = False
        self.f2_power = defaultPower
        self.a = gunLength
        return _balls

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if (event.pos[0] - 20) != 0:
                self.an = math.atan((event.pos[1] - self.y0) / (event.pos[0] - self.x0))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def update_pic(self):
        """
        обновляет картинку пушки
        """
        x = self.x0
        y = self.y0
        lenght = self.a
        height = self.b
        angle = self.an
        pygame.draw.polygon(self.screen, self.color, [[x, y], [x + lenght * cos(angle), y + lenght * sin(angle)],
                                                      [x + lenght * cos(angle) + height * sin(angle),
                                                       y + lenght * sin(angle) - height * cos(angle)],
                                                      [x + height * sin(angle), y - height * cos(angle)]])

    def power_up(self):
        """
        увеличивает со временем силу выстрела
        """
        if self.f2_on:
            if self.f2_power < maxPower:
                self.f2_power += (maxPower - defaultPower) / 200
                self.a += 1
            self.color = RED
        else:
            self.color = GREY


class Target:

    def __init__(self):
        """
        конструктор класса Target
        """
        self.color = RED
        self.r = randint(20, 50)
        self.y = randint(300, 450)
        self.x = randint(550, 700)
        self.vx = randint(-200, -100)
        self.vy = (-1) ** randint(0, 1) * randint(100, 200)
        self.ax = randint(-300, -100)
        self.ay = ((-1) ** randint(0, 1)) * randint(100, 300)
        self.startX = self.x
        self.startY = self.y
        self.screen = screen
        self.live = 1

    def die_target(self):
        """
        удаляет объект из списка мишеней
        """
        _targets = targets
        _targets.remove(self)
        self.live = 0
        return _targets

    def update_pic(self):
        """
        обновляет картинку мишени
        """
        if self.live > 0:
            pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)
            pygame.draw.circle(self.screen, BLACK, (self.x, self.y), self.r, width=1)

    def move(self):
        """
        изменяет по обеим осям скорости, координаты и ускорения мишени
        """
        if self.x < self.startX:
            self.ax = abs(self.ax)
        else:
            self.ax = (-1) * abs(self.ax)
        if self.y < self.startY:
            self.ay = abs(self.ay)
        else:
            self.ay = -1 * abs(self.ay)
        self.vx += self.ax * deltatime
        self.vy += self.ay * deltatime
        self.x += self.vx * deltatime
        self.y += self.vy * deltatime


def update_pics():
    """
    вызывает функции обновления картинок объектов
    """
    gun.update_pic()
    for target in targets:
        target.update_pic()
    for ball in balls:
        ball.update_pic()
    pygame.display.update()


def balls8targets_move():
    """
    вызывает функции перемещения шаров и мишеней
    """
    for ball in balls:
        ball.move()
    for target in targets:
        target.move()


def balls8targets_process():
    """
    обрабатывает процессы взаимодействия шаров и мишеней между собой, возвращает массив мишеней после обработки
    """
    balls8targets_move()
    _targets = targets
    for ball in balls:
        for target in targets:
            if ball.hittest(target) and target.live:
                _targets = target.die_target()
    return _targets


def new_targets_create():
    """
    создает новые цели в согласовании с количеством очков
    """
    _targets = []
    count = lvl // 10 + 1
    for i in range(count):
        _targets.append(Target())
    return _targets


def update_text(time):
    """
    получая на вход время, в течение которого должна гореть надпись с информацией об обновлении уровня, уменьшает
    это время и вызывает функцию отрисовки надписи
    :return:
    """
    next_lvl_text()
    pygame.display.update()
    time -= 1 / FPS
    return time


def next_lvl_text():
    """
    рассчитывает положение и текст надписи об обновлении уровня и высвечивает ее на экран
    """
    next_lvl_font = myfont.render("LVL: " + str(lvl), False, BLACK)
    x = (WIDTH - next_lvl_font.get_width()) / 2
    y = HEIGHT / 2 - next_lvl_font.get_height() / 2
    screen.blit(next_lvl_font, (x, y))


def lvl_check(_targets):
    """
    проверяет наличие мишеней на экране и в случае отсутствия таковых запускает счеткчик горения надписи нового уровня,
    повышает уровень и создает новые мишени в соответствии с уровнем, возвращает массив с ними
    """
    _lvl = lvl
    _text_time = text_time
    if len(_targets) == 0 and _text_time <= 0:
        _text_time = NextLvlTextTime
        _lvl += 1
        _targets = new_targets_create()
    return _targets, _text_time, _lvl


def del_elems(_balls):
    """
    возвращает список без элементов
    """
    _balls = []
    return _balls


def main():
    """
    выполняет основные действия игры
    """
    clock.tick(FPS)
    screen.fill(WHITE)
    update_lvl_text()
    _text_time = text_time
    _targets = targets
    _finished, _balls = events_process(balls)
    if _text_time <= 0:
        _targets = balls8targets_process()
    gun.power_up()
    _targets, _text_time, _lvl = lvl_check(_targets)
    if _text_time > 0:
        _balls = del_elems(_balls)
        _text_time = update_text(_text_time)
    else:
        update_pics()
    return _balls, _targets, _finished, _text_time, _lvl


def events_process(_balls):
    """
    выполняет обработку собывий нажатия клавиш и кнопок
    """
    _finished = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            _finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start()
        elif event.type == pygame.MOUSEBUTTONUP:
            _balls = gun.fire2_end(event, _balls)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
    return _finished, _balls


def update_lvl_text():
    """
    обновляет счетчик очков в левом верхнем углу экрана
    """
    font = myfont.render(str(lvl), False, BLACK)
    x = 50
    y = 50
    screen.blit(font, (x, y))


screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
targets = []
lvl = 0
text_time = 0

clock = pygame.time.Clock()
gun = Gun()
targets.append(Target())
finished = False
deltatime = 1 / FPS

while not finished:
    balls, targets, finished, text_time, lvl = main()

pygame.quit()
