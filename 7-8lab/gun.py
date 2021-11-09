import math
from math import sin, cos, sqrt, pi
from random import choice, randint
from pygame.font import Font
import pygame

pygame.init()
pygame.font.init()

FPS = 200

fontSize = 45
fontName = "back-to-1982/BACKTO1982.ttf"
myFont: Font = pygame.font.Font(fontName, fontSize)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = 0xFFC91F
GREEN = (0, 255, 0)
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 1200
HEIGHT = 600

acceleration = 700

gunLength = 100
defaultPower = 300
maxPower = 1500
defaultGunX0 = -50
defaultGunY0 = 450
groundY = 570
NextLvlTextTime = 1
defaultPulsingSpeed = 30
gunSpeed = 500
defaultRadius = 10
defaultBombX0 = WIDTH // 2
defaultBombY0 = HEIGHT // 2
defaultBombSpeed = 200
bombAcceleration = acceleration // 4
defaultBombRadius = 50
speedPowerUp = 200
powerUpTime = 1
winPoints = 20
k = 3

screen = pygame.display.set_mode((WIDTH, HEIGHT))
bomb_surf = pygame.image.load("sprites/bomb.png")
bomb_surf = pygame.transform.scale(bomb_surf, (bomb_surf.get_width() // k, bomb_surf.get_height() // k))


class Projectile:

    def __init__(self, _screen: pygame.Surface, _x=defaultGunX0, _y=defaultGunY0):
        """
        Конструктор класса Projectile
        :param _screen: surface, к которому будет привязан объект
        :param _x: начальная координата x объекта
        :param _y: начальная координата y объекта
        """
        self.time_live = None
        self.screen = _screen
        self.r = None
        self.x = _x
        self.y = _y
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.id = -1

    def update_pic(self):
        """
        обновляет картинку мячика
        """
        if self.time_live > 0:
            pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)

    def move(self):
        """
        Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна WIDTHхHEIGHT) и вызывает функцию, обновляющую self.r, если объект относится
        к классу PulsingBall.
        """
        if self.y < groundY - self.r - 5:
            self.vy -= acceleration * deltatime
        if self.x >= WIDTH - self.r:
            self.vx = (-1) * abs(self.vx)
        if self.x <= self.r:
            self.vx = abs(self.vx)
        if self.y >= groundY - self.r:
            self.vy = round(0.7 * abs(self.vy))
            self.vx *= 0.7

        if isinstance(self, PulsingBall):
            self.pulsing()

        self.x += self.vx * deltatime
        self.y -= self.vy * deltatime
        self.time_live -= deltatime
        if self.time_live < 0:
            self.r = 0

    def hittest(self, obj):
        """
        Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Если в obj был описан объект класса Gun, то функция проверяет принадлежность снаряда к obj с помощью
        параметра id и возвращает обновленный массив объектов класса Gun
        :param obj: объект, для которого нужно проверить столкновение со снарядом
        :return: False, если столкновения не было и True, если было.
        """
        _guns = guns
        if isinstance(obj, Target):
            dist = math.sqrt((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2)
            if dist <= self.r + obj.r:
                for gun in _guns:
                    if self.id == gun.id:
                        gun.point += 1
                return True, _guns
        if isinstance(obj, Gun):
            x1, y1 = obj.x, obj.y
            r1 = 3 * gunLength / 4
            x, y = self.x, self.y
            r = self.r
            dist = sqrt((x - x1) ** 2 + (y - y1) ** 2)
            if dist <= r + r1:
                for gun in _guns:
                    if obj.id == gun.id and self.id != obj.id and cooldown <= 0:
                        gun.live -= 1
                return True, _guns
        return False, _guns


class Ball(Projectile):

    def __init__(self, _screen: pygame.Surface, _x, _y, _id=-1):
        """
        Конструктор объектов класса Ball (снарядов с постоянным размером)
        """
        super().__init__(_screen, _x, _y)
        self.r = defaultRadius
        self.time_live = 3
        self.id = _id


class PulsingBall(Projectile):

    def __init__(self, _screen: pygame.Surface, _x, _y, _id=-1):
        """
        Конструктор объектов класса PulsingBall (снарядов с увеличивающимся размером)
        """
        super().__init__(_screen, _x, _y)
        self.time_live = 2
        self.r = 1
        self.pulsingspeed = defaultPulsingSpeed
        self.id = _id

    def pulsing(self):
        """
        Функция, увеличивающая радиус объекта
        :return:
        """
        self.r += self.pulsingspeed * deltatime


class Gun:

    def __init__(self):
        """
        Конструктор класса Gun
        """
        self.a = gunLength
        self.b = 20
        self.screen = screen
        self.f2_power = 20
        self.f2_on = False
        self.an = 1
        self.color = GREY
        self.speed = gunSpeed
        self.live = 10
        self.active = False
        self.x = 0
        self.y = 0
        self.id = -1
        self.point = 0

    def fire2_start(self):
        """
        При нажатии на клавишу мыши включает соответствующий параметр
        """
        if self.active:
            self.f2_on = True

    def fire2_end(self, _event, _balls):
        """
        Выстрел мячом из активной пушки.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        Функция при выстреле переключает параметр active у обеих пушек
        """
        if self.active:
            _guns = guns
            _ = randint(0, 1)
            if _ == 0:
                new_projectile = Ball(self.screen, self.x, self.y, self.id)
            else:
                new_projectile = PulsingBall(self.screen, self.x, self.y, self.id)
            if (_event.pos[0] - new_projectile.x) != 0:
                self.an = math.atan2((_event.pos[1] - new_projectile.y), (_event.pos[0] - new_projectile.x))
            new_projectile.vx = self.f2_power * math.cos(self.an)
            new_projectile.vy = - self.f2_power * math.sin(self.an)
            _balls.append(new_projectile)
            self.f2_on = False
            self.f2_power = defaultPower
            self.a = gunLength
            for _gun in _guns:
                _gun.active = not _gun.active
            return _balls, _guns

    def update_pic(self):
        """
        Обновляет картинку пушки
        """
        x = self.x
        y = self.y
        lenght = self.a
        height = self.b
        angle = self.an
        pygame.draw.polygon(self.screen, self.color, [[x, y], [x + lenght * cos(angle), y + lenght * sin(angle)],
                                                      [x + lenght * cos(angle) + height * sin(angle),
                                                       y + lenght * sin(angle) - height * cos(angle)],
                                                      [x + height * sin(angle), y - height * cos(angle)]])
        pygame.draw.circle(self.screen, self.color, (x, y), 3 * gunLength / 4)

    def targetting(self, event):
        """
        Прицеливание. Зависит от положения мыши. Работает для активной пушки.
        """
        if self.active:
            if event:
                if (event.pos[0] - 20) != 0:
                    if self.id == 0:
                        self.an = math.atan((event.pos[1] - self.y) / (event.pos[0] - self.x))
                    else:
                        self.an = pi + math.atan((event.pos[1] - self.y) / (event.pos[0] - self.x))
            if self.f2_on:
                self.color = RED
            else:
                self.color = MAGENTA

    def power_up(self):
        """
        Увеличивает со временем силу выстрела.
        """
        if self.f2_on:
            if self.f2_power < maxPower:
                self.f2_power += (maxPower - defaultPower) / (powerUpTime / deltatime)
                self.a += speedPowerUp * deltatime
            self.color = RED
        else:
            if self.active:
                self.color = MAGENTA
            else:
                self.color = GREY

    def move(self, direction):
        """
        При на жатии на клавиши W и S перемещает в соответствующем направлении активную пушку
        :param direction:
        :return:
        """
        if self.active:
            if direction == "up":
                if self.y >= 0:
                    self.y += (-1) * self.speed * deltatime
            if direction == "down":
                if self.y <= groundY - defaultRadius - 5:
                    self.y += self.speed * deltatime


class LeftGun(Gun):

    def __init__(self, _active=True):
        """
        Конструктор левой пушки
        """
        super().__init__()
        self.x = defaultGunX0
        self.y = defaultGunY0
        self.id = 0
        self.active = _active


class RightGun(Gun):

    def __init__(self, _active=False):
        """
        Конструктор правой пушки
        """
        super().__init__()
        self.x = WIDTH - defaultGunX0
        self.y = defaultGunY0
        self.id = 1
        self.active = _active
        self.an = pi


class Target:

    def __init__(self, _x, _y):
        """
        конструктор класса Target
        """
        self.color = RED
        self.r = randint(20, 50)
        self.y = _y
        self.x = _x
        self.vx = randint(-200, -100)
        self.vy = (-1) ** randint(0, 1) * randint(100, 200)
        self.ax = randint(-300, -100)
        self.ay = ((-1) ** randint(0, 1)) * randint(100, 300)
        self.startX = self.x
        self.startY = self.y
        self.screen = screen
        self.live = 1

    def update_pic(self):
        """
        обновляет картинку мишени
        """
        if self.live > 0:
            pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)
            pygame.draw.circle(self.screen, BLACK, (self.x, self.y), self.r, width=1)


class CommonTarget(Target):

    def __init__(self, _x, _y):
        """
        Конструктор класса CommonTarget - мишени с движениями только в вертикальном направлении
        :params _x, _y: начальные координаты
        """
        super().__init__(_x, _y)
        self.ax = 0
        self.vx = 0

    def move(self):
        """
        Функция отвечает за изменение координат мешени класса CommonTarget
        """
        if self.y < self.startY:
            self.ay = abs(self.ay)
        else:
            self.ay = -1 * abs(self.ay)
        self.vy += self.ay * deltatime
        self.y += self.vy * deltatime


class HardTarget(Target):

    def __init(self, _x, _y):
        """
        Конструктор класса HardTarget - мишени со сложными движениями(как в вертикальном,
        так и в горизонтальном направлениях)
        """
        super().__init__(_x, _y)

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


class Bomb:

    def __init__(self, _screen: pygame.surface = screen):
        """
        Конструктор класса Bomb
        """
        self.x = defaultBombX0
        self.y = defaultBombY0
        self.x0 = self.x
        self.y0 = self.y
        self.vy = defaultBombSpeed
        self.vx = 0
        self.ax = 0
        self.ay = bombAcceleration
        self.screen = _screen
        self.r = defaultBombRadius

    def move(self):
        """
        Функция отвечает за изменение координат объекта класса Bomb
        """
        if self.y >= self.y0:
            self.ay = (-1) * abs(self.ay)
        else:
            self.ay = abs(self.ay)
        self.vy += self.ay * deltatime
        self.y += self.vy * deltatime

    def update_pic(self):
        """
        Отвечает за обновление картинки объекта класса Bomb
        :return:
        """
        bomb_rect = bomb_surf.get_rect(center=(self.x, self.y))
        screen.blit(bomb_surf, bomb_rect)


def update_pics():
    """
    вызывает функции обновления картинок объектов
    """
    for gun in guns:
        gun.update_pic()
    for target in targets:
        target.update_pic()
    for ball in balls:
        ball.update_pic()
    bomb.update_pic()
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
    обрабатывает процессы взаимодействия шаров и мишеней между собой, возвращает массив мишеней и пушек после обработки
    """
    _guns = guns
    balls8targets_move()
    _targets = targets
    for ball in balls:
        for target in targets:
            hit, _guns = ball.hittest(target)
            if hit and target.live:
                target.live = 0
                _targets.remove(target)
    return _targets, _guns


def guns8balls_process(_guns, _cooldown):
    """
    Обрабатывает взаимодействие пушек со снарядами и в связи с этим изменяет параметр _cooldown
    :param _guns: массив пушек, который нужно обработать
    :param _cooldown: время после уменьшения HP у пушек до того, как у пушек может снова уменьшится HP
    :return: обновленный после обработки массив пушек и параметр _cooldown
    """
    for gun in _guns:
        for ball in balls:
            hit, _guns = ball.hittest(gun)
            if hit and _cooldown <= 0:
                _cooldown = 0.3
    return _guns, _cooldown


def new_targets_create():
    """
    Создает новые цели в согласовании с количеством очков и положением бомбы, спавнящей цели
    """
    _targets = []
    count = lvl // 10 + 1
    for i in range(count):
        if count >= 2:
            new_target = HardTarget(bomb.x, bomb.y)
        else:
            new_target = CommonTarget(bomb.x, bomb.y)
        _targets.append(new_target)
    return _targets


def update_text(time):
    """
    Получая на вход время, в течение которого должна гореть надпись с информацией об обновлении уровня, уменьшает
    это время и вызывает функцию отрисовки надписи
    """
    next_lvl_text()
    pygame.display.update()
    time -= deltatime
    return time


def next_lvl_text():
    """
    Рассчитывает положение и текст надписи об обновлении уровня и высвечивает ее на экран
    """
    next_lvl_font = myFont.render("LVL: " + str(lvl), False, BLACK)
    x = (WIDTH - next_lvl_font.get_width()) / 2
    y = HEIGHT / 2 - next_lvl_font.get_height() / 2
    screen.blit(next_lvl_font, (x, y))


def lvl_check(_targets):
    """
    Проверяет наличие мишеней на экране и в случае отсутствия таковых запускает счеткчик горения надписи нового уровня,
    повышает уровень и создает новые мишени в соответствии с уровнем, возвращает массив с ними.
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
    Возвращает список без элементов
    """
    _balls = []
    return _balls


def main():
    """
    Выполняет основные действия игры
    """
    _output = output
    _cooldown = cooldown - deltatime
    clock.tick(FPS)
    screen.fill(WHITE)
    _text_time = text_time
    _targets = targets
    _finished, _balls, _keydown, _eventkey, _guns, _output = events_process(balls)
    if _text_time <= 0:
        bomb.move()
        _targets, _guns = balls8targets_process()
        _guns, _cooldown = guns8balls_process(_guns, _cooldown)
    for _gun in guns:
        _gun.power_up()
    _targets, _text_time, _lvl = lvl_check(_targets)
    if _text_time > 0:
        _balls = del_elems(_balls)
        _text_time = update_text(_text_time)
    else:
        hp_text_update()
        points_text_update()
        update_pics()
    return _balls, _targets, _finished, _text_time, _lvl, _keydown, _eventkey, _guns, _cooldown, _output


def move_obj(objects, _eventkey):
    """
    Вызывает перемещение объектов из массива objects в соответствии с тем, какая клавиша нажата
    """
    if _eventkey == 119:
        for obj in objects:
            obj.move("up")
    if _eventkey == 115:
        for obj in objects:
            obj.move("down")


def events_process(_balls):
    """
    Выполняет обработку событий нажатия клавиш и кнопок
    """
    _finished = False
    _keydown = keydown
    _eventkey = eventkey
    _guns = guns
    _output = output
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            _finished = True
            _output = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for _gun in guns:
                _gun.fire2_start()
        elif event.type == pygame.MOUSEBUTTONUP:
            for _gun in guns:
                if _gun.active:
                    _balls, _guns = _gun.fire2_end(event, _balls)
                    break
        elif event.type == pygame.MOUSEMOTION:
            for _gun in guns:
                _gun.targetting(event)
        elif event.type == pygame.KEYDOWN:
            _eventkey = event.key
            _keydown = True
        elif event.type == pygame.KEYUP:
            _eventkey = 0
            _keydown = False
        if _keydown:
            move_obj(guns, _eventkey)
    return _finished, _balls, _keydown, _eventkey, _guns, _output


def left_hp_text_update():
    """
    Функция обновления текста со значениями жизней левой пушки
    """
    font = myFont.render(str(l_gun.live), False, RED)
    x = 20
    y = 20
    screen.blit(font, (x, y))


def right_hp_text_update():
    """
    Функция обновления текста со значениями жизней правой пушки
    """
    font = myFont.render(str(r_gun.live), False, RED)
    x = WIDTH - 20 - font.get_width()
    y = 20
    screen.blit(font, (x, y))


def hp_text_update():
    """
    Вызывает функции обновления текста с жизнями пушек
    """
    left_hp_text_update()
    right_hp_text_update()


def right_points_text_update():
    """
    Функция обновляет текстовое поле с очками правой пушки
    """
    font = myFont.render(str(r_gun.point), False, GREEN)
    x = WIDTH - 20 - font.get_width()
    y = 100
    screen.blit(font, (x, y))


def left_points_text_update():
    """
    Функция обновляет текстовое поле с очками левой пушки
    """
    font = myFont.render(str(l_gun.point), False, GREEN)
    x = 20
    y = 100
    screen.blit(font, (x, y))


def points_text_update():
    """
    Функция вызывает функции обновления текстовых полей с очками пушек
    """
    left_points_text_update()
    right_points_text_update()


def finishexam():
    """
    Проверяет, не окончена ли игра в связи с нулевыми жизнями одной из пушек или достижением одной
    из них winPoints очков
    """
    for gun in guns:
        if gun.live == 0 or gun.point >= winPoints:
            return True


def winner_exam():
    """
    Проверяет причину окончания игры и победителя
    :return: Причину окончания и победителя
    """
    winner = ""
    reason = ""
    if l_gun.point >= winPoints:
        winner = "LEFT"
        reason = "POINTS"
    elif l_gun.live <= 0:
        winner = "RIGHT"
        reason = "HP"
    elif r_gun.point >= winPoints:
        winner = "RIGHT"
        reason = "POINTS"
    elif r_gun.live <= 0:
        winner = "LEFT"
        reason = "HP"
    return winner, reason


def end_text_update():
    """
    Обновляет текст конечного экрана в зависимости от причины окончания игры и победителя
    """
    winner, reason = winner_exam()
    first_str = myFont.render("WINNER: " + winner, False, BLACK)
    second_str = myFont.render("", False, BLACK)
    if reason == "POINTS":
        second_str = myFont.render("HE SCORED " + str(winPoints) + " POINTS", False, BLACK)
    elif reason == "HP":
        if winner == "LEFT":
            second_str = myFont.render("RIGHT HAS SPENT ALL HITPOINTS", False, BLACK)
        else:
            second_str = myFont.render("LEFT HAS SPENT ALL HITPOINTS", False, BLACK)
    first_str_x = WIDTH // 2 - first_str.get_width() // 2
    second_str_x = WIDTH // 2 - second_str.get_width() // 2
    first_str_y = HEIGHT // 2 - first_str.get_height()
    second_str_y = HEIGHT // 2 + second_str.get_height()
    screen.blit(first_str, (first_str_x, first_str_y))
    screen.blit(second_str, (second_str_x, second_str_y))
    pygame.display.update()


def end_main():
    """
    Выполняет основные действия после окончания игры
    """
    clock.tick(FPS)
    screen.fill(WHITE)
    end_text_update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False


balls = []
targets = []
lvl = 0
text_time = 0
keydown = False
eventkey = 0

clock = pygame.time.Clock()
bomb = Bomb()
l_gun = LeftGun()
r_gun = RightGun()
l_gun.update_pic()
r_gun.update_pic()
guns = (l_gun, r_gun)
targets.append(CommonTarget(bomb.x, bomb.y))
finished = False
deltatime = 1 / FPS
cooldown = 0
output = False

while not finished:
    balls, targets, finished, text_time, lvl, keydown, eventkey, guns, cooldown, output = main()
    if finishexam():
        finished = True

while not output:
    output = end_main()

pygame.quit()
