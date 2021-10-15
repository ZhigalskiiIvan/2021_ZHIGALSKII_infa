import random
import pygame
from pygame.draw import circle, rect
from random import randint
from math import sqrt, floor
from pygame.font import Font

pygame.init()
pygame.font.init()

display_width = 1200
display_height = 800
FPS = 160
screen = pygame.display.set_mode((display_width, display_height))
deltatime = 1 / FPS
max_speed = 150
min_pulsing_speed = 30
max_pulsing_speed = 100
min_radius = 35
max_radius = 65
point_to_common_ball = 1
point_to_pulsing_ball = 2
countDiffObj = 2
fontSize = 45

unitTextSurfWidth = 40
unitTextSurfHeight = 50

fontName = 'back-to-1982/BACKTO1982.ttf'

myfont: Font = pygame.font.Font(fontName, fontSize)

ballsLifeTime = 3
beginCreateCoolDown = 0.5

RED = (200, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
backgroundColor = (255, 239, 205)
winTextColor = (0, 200, 0)
failedTextColor = (255, 0, 0)
resColor = (255 - backgroundColor[0], 255 - backgroundColor[1], 255 - backgroundColor[2])

leftedge = 0
upedge = 0
downedge = display_height - 0
rightedge = display_width - 0


class Ball:
    """
    класс хранит значения параметров, координат и проекций скорости шара, носит в себе функции его временного стирания
    и рисования в новом месте, а также полного его стирания
    """

    def __init__(self, color, r: int, x: int, y: int, xspeed: int, yspeed: int, pulsing: bool = False,
                 pulsingspeed: int = 0, lifetime: int = 0):
        """
        функция устанавливает параметры шара при его создании как объекта данного класса
        :param color: цвет шара
        :param r: радиус шара
        :param x: координатa x центра шара
        :param y: координатa y центра шара
        :param xspeed: скорость шара по x
        :param yspeed: скорость шара по y
        :param pulsing: отвечает за то, должен ли шар пульсировать
        :param pulsingspeed: отвечает за то, с какой скоростью шар должен пульсировать
        :param lifetime: время существования шара от момента создания
        """
        self.color = color
        self.r = r
        self.x = x
        self.y = y
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.lifetime = lifetime
        self.pulsing = pulsing
        if pulsing:
            self.point_to_tap = point_to_pulsing_ball
        else:
            self.point_to_tap = point_to_common_ball
        self.pulsingspeed = pulsingspeed
        circle(screen, color, (x, y), r)

    def clear_surf(self):
        """
        очищает пространство старого местоположения шара
        """
        circle(screen, backgroundColor, (self.x, self.y), self.r)

    def update(self):
        """
        считает новые коордтинаты шара и радиус шара и рисует его в новом месте
        """
        self.x += deltatime * self.xspeed
        self.y += deltatime * self.yspeed
        if self.pulsing:
            if self.r <= min_radius:
                self.pulsingspeed = abs(self.pulsingspeed)
            if self.r >= max_radius:
                self.pulsingspeed = (-1) * abs(self.pulsingspeed)
        self.r += self.pulsingspeed * deltatime
        self.lifetime += deltatime
        circle(screen, self.color, (self.x, self.y), self.r)

    def die(self):
        """
        стирает шар и присваивает его координатам и радиусам значения 0
        """
        self.color = backgroundColor
        circle(screen, self.color, (self.x, self.y), self.r)
        self.x = 0
        self.y = 0
        self.r = 0


def new_ball():
    """
    создает новый объект класса Ball
    :return: новый объект класса Ball
    """
    r = randint(min_radius, max_radius)
    x = randint(r, display_width - r)
    y = randint(r, display_height - r)
    xspeed = randint(-max_speed, max_speed)
    yspeed = randint(-max_speed, max_speed)
    color = COLORS[randint(0, len(COLORS) - 1)]
    rand_number = 0
    if diff_level >= 2:
        rand_number = random.randint(0, countDiffObj - 1)
    if rand_number == 0:
        return Ball(color, r, x, y, xspeed, yspeed)
    if rand_number == 1:
        pulsespeed = (-1) ** (randint(0, 1)) * randint(min_pulsing_speed, max_pulsing_speed)
        return Ball(color, r, x, y, xspeed, yspeed, True, pulsespeed)


def event_process():
    """
    обрабатывает события, происходящие во время выполнения программы
    :return: присваивает переменной finish значение False, если произошедшее событие - выход из программы;
     True - в ином случае и возвращает это значение
    :return: новое значение очков игрока
    """
    finish_status = finished
    newwinpoints = winpoints
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish_status = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            newwinpoints = mouse_button_click(event)
    return finish_status, newwinpoints


def ball_click_exam(xpush, ypush):
    """
    проверяет произошедший клик на предмет того, был ли он совершен по шару, и если да, то удаляет шар и возвращает
    количество очков, отведенное на данный шар, просумированное с уже начисленными очками
    :param xpush: горизонтальная координата клика мыши
    :param ypush: вертикальная координата клика мыши
    :return: возвращает количество очков, отведенное на нажатый шар, просумированное с уже начисленными очками
    """
    global balls
    winpoint = winpoints
    for ball in balls:
        x = ball.x
        y = ball.y
        r = ball.r
        dist_to_center = sqrt((x - xpush) ** 2 + (y - ypush) ** 2)
        if dist_to_center <= r:
            ball.die()
            balls.remove(ball)
            winpoint = str(int(winpoint) + ball.point_to_tap)
    return winpoint


def mouse_button_click(event):
    """
    вызывает функцию, которая отличает клики мыши по шарам от остальных, подавая в нее координаты клика
    :param event: событие(клик мышью)
    :return: новое количество очков
    """
    xpush, ypush = event.pos
    newwinpoints = ball_click_exam(xpush, ypush)
    return newwinpoints


def time_exam(cooldown):
    """
    проверяет, нужно ли создавать новый объект в данный момент времени
    :param cooldown: время "перезарядки" создания нового объекта
    :return: возвращает True, если в данный момент нужно создать новый данный объект, False - в обратном случае
    """
    if time_to_spawn >= cooldown:
        return True
    else:
        return False


def create_ball():
    """
    вызывает функцию создвния нового шара и записывает его в список всех шаров
    """
    global balls
    balls += [new_ball()]


def moving_ball():
    """
    перемещает шар в новое положение
    """
    global balls
    for ball in balls:
        ball.clear_surf()
        ball.update()


def balls_natural_death():
    """
    вызывает функцию исчезновения шара, который живет дольше, чем ballsLifeTime и удаляет его из списка всех шаров,
    а также начисляет при удалении и возвращает новое количество проигрышных очков
    """
    global balls
    failpoint = failedpoints
    for ball in balls:
        if ball.lifetime >= ballsLifeTime:
            ball.die()
            balls.remove(ball)
            failpoint = str(int(failpoint) + 1)

    return failpoint


def left_wall_hit(obj):
    """
    изменяет скорость объекта, ударившегося стену (левую)
    :param obj: объект, скорость которого нужно изменить при о ударе стену
    """
    obj.xspeed = abs(obj.xspeed)
    obj.yspeed = randint(-max_speed, max_speed)


def right_wall_hit(obj):
    """
    изменяет скорость объекта, ударившегося стену (правую)
    :param obj: объект, скорость которого нужно изменить при ударе о стену
    """
    obj.xspeed = (-1) * abs(obj.xspeed)
    obj.yspeed = randint(-max_speed, max_speed)


def floor_wall_hit(obj):
    """
    изменяет скорость объекта, ударившегося о правую стену
    :param obj: объект, скорость которого нужно изменить при ударе о ghfde. стену
    """
    obj.yspeed = (-1) * abs(obj.yspeed)
    obj.xspeed = randint(-max_speed, max_speed)


def roof_wall_hit(obj):
    """
    изменяет скорость объекта, ударившегося о правую стену
    :param obj: объект, скорость которого нужно изменить при ударе о ghfde. стену
    """
    obj.yspeed = abs(obj.yspeed)
    obj.xspeed = randint(-max_speed, max_speed)


def wall_hit_balls():
    """
    вызывает обработку сталкиваний шаров со стенами
    """
    global balls
    for ball in balls:
        x = ball.x
        y = ball.y
        r = ball.r
        if x <= leftedge + r:
            left_wall_hit(ball)
        if x >= rightedge - r:
            right_wall_hit(ball)
        if y <= upedge + r:
            roof_wall_hit(ball)
        if y >= downedge - r:
            floor_wall_hit(ball)


def ballsmain():
    """
    совершает основные действия с шарами
    :return: возвращает новое количество проигрышных очков, а также время со времени последнего спавна шара
    """
    time = time_to_spawn
    if time_exam(ballsCreatingCoolDown):
        create_ball()
        time = 0
    wall_hit_balls()
    moving_ball()
    newfailedpoint = balls_natural_death()
    return newfailedpoint, time


def fail_points_update():
    """
    обновляет количество проигрышных очков игрока на экране
    """
    failed_font_size = fontSize
    failed_font = pygame.font.Font(fontName, failed_font_size)
    failedpoint_textsurface = failed_font.render(failedpoints, False, failedTextColor)
    rect(screen, backgroundColor,
         [6, 6, unitTextSurfWidth * len(failedpoints), unitTextSurfHeight * (failed_font_size / fontSize)])
    screen.blit(failedpoint_textsurface, (6, 6))


def win_points_update():
    """
    обновляет количество выигрышных очков игрока на экране, увеличивает шрифт написания выигрышных
    очков в случае повышения уровня сложности (каждые 15 выигрышных очков)
    """
    win_font_size = round(fontSize * sqrt(diff_level))
    win_font = pygame.font.Font(fontName, win_font_size)
    winpoint_textsurface = win_font.render(winpoints, False, winTextColor)
    rect(screen, backgroundColor, [display_width - (win_font_size / fontSize) * unitTextSurfWidth * len(winpoints), 6,
                                   (win_font_size / fontSize) * unitTextSurfWidth * len(winpoints),
                                   unitTextSurfHeight * (win_font_size / fontSize)])
    screen.blit(winpoint_textsurface,
                (display_width - (win_font_size / fontSize) * unitTextSurfWidth * len(winpoints), 6))


def points_surfaces_update():
    """
    вызывыает функции обновления надписей очков
    """
    fail_points_update()
    win_points_update()


def difficult_update():
    """
    повышает уровень сложности каждые 15 выигрышных очков, меняет в связи с этим время спавна нового шара
    :return: новое время спавна, а также уровень сложности
    """
    lvl = 1 + floor(int(winpoints) / 15)
    if lvl == 1:
        return beginCreateCoolDown, 1
    else:
        return beginCreateCoolDown / sqrt(lvl), lvl


def end_text_render(font, y):
    """
    рендерит на экран конечный текст
    :param font: такст, который нужно отрендерить
    :param y: высота, на которой нужно расположить текст
    """
    x = (display_width - font.get_width()) / 2
    screen.blit(font, (x, y))


def print_new_high_score(font):
    """
    выводит на экран надпись в случайе, если рекорд побит
    :param font: шрифт
    """
    game_over_font = font.render("New score: " + winpoints, False, resColor)
    end_text_render(game_over_font, display_height / 2 - game_over_font.get_height() / 2)


def print_score(font, high_score):
    """
    выводит на экран надпись в том случае, если рекорд не побит
    :param font: шрифт
    :param high_score: рекорд
    """
    game_over_font = font.render("Your score: " + winpoints, False, resColor)
    end_text_render(game_over_font, display_height / 2 - game_over_font.get_height())
    game_over_font = font.render("High score: " + high_score, False, resColor)
    end_text_render(game_over_font, display_height / 2 + game_over_font.get_height())


def score_treatment():
    """
    считывает из файла лучший рекорд, сравнивает с результатом игрока и пишет соответстстующую запись на экране
    :return: список результатов с новым значением
    """
    end_screen_font = pygame.font.Font(fontName, int(fontSize * 1.5))
    with open("high_scores.txt", "r") as F:
        results = F.readlines()
        high_score = ""
        if len(results) != 0:
            high_score = results[0].split("\n")[0]
        if high_score == "":
            results = [winpoints + "\n"]
            print_new_high_score(end_screen_font)
        elif int(high_score) < int(winpoints):
            results += [winpoints + "\n"]
            print_new_high_score(end_screen_font)
        else:
            results += [winpoints + "\n"]
            print_score(end_screen_font, high_score)
        return results


def exclude_repeatitive(withreps):
    """
    собирает массив из различных элементов массива withreps и возвращает обновленный массив
    :param withreps: массив, в котором есть повторяющиеся элементы
    :return: массив из различных(неповторяющихся) элементов массива withreps
    """
    withoutreps = []
    for element in withreps:
        if not (element in withoutreps):
            withoutreps.append(element)
    return withoutreps


def game_over():
    """
    вызывает функцию, которая возвращает обновленный список всех результатов,
    новый список сортируеты и записывает в файл
    """
    results = score_treatment()
    results = exclude_repeatitive(results)
    results.sort(reverse=True, key=int)
    new_text = ""
    for i in range(len(results)):
        new_text += results[i]
    with open("high_scores.txt", "w") as F:
        F.write(new_text)


def game_over_exam():
    finish = False
    if int(failedpoints) >= 100:
        finish = True
    return finish


screen.fill(backgroundColor)
pygame.display.update()
clock = pygame.time.Clock()
finished = False
time_to_spawn = 0
balls = []
created_balls_number = 0

failedpoints = "0"
winpoints = "0"
ballsCreatingCoolDown = beginCreateCoolDown
diff_level = 1
failed_level = 1

while not finished:
    clock.tick(FPS)
    time_to_spawn += deltatime
    eventparameters = event_process()
    finished = (game_over_exam() or eventparameters[0])
    winpoints = eventparameters[1]
    ballsCreatingCoolDown, diff_level = difficult_update()
    points_surfaces_update()
    failedpoints, time_to_spawn = ballsmain()
    pygame.display.update()

game_over()
exitbool = False
while not exitbool:
    for exevent in pygame.event.get():
        if exevent.type == pygame.QUIT:
            exitbool = True
    pygame.display.update()

pygame.quit()
