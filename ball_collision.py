from random import randint, choice

import pygame
import sys

pygame.init()

width, height = 500, 500

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Balls')
clock = pygame.time.Clock()

set_color = 0
move_ball = 0
balls = 0
rad = 20
ind = -1
B = []

colors = [(38, 70, 83), (42, 157, 143), (233, 196, 106), (244, 162, 97),
          (231, 111, 81), (230, 57, 70), (241, 250, 238), (168, 218, 220),
          (69, 123, 157), (29, 53, 87)]


def reflect_ball(speed_x, speed_y):
    """ Bouncing off screen frames
    """
    if x >= width - rad and speed_x > 0:
        speed_x *= -1
    elif y >= height - rad and speed_y > 0:
        speed_y *= -1
    elif x <= rad and speed_x < 0:
        speed_x *= -1
    elif y <= rad and speed_y < 0:
        speed_y *= -1
    return speed_x, speed_y


def add_ball(x_pos, y_pos):
    """ Adding a ball with random parameters
     at the position of the mouse cursor
     """
    speed_x, speed_y = 0, 0
    col = choice(colors)
    while speed_x == 0 and speed_y == 0:
        speed_x = randint(-9, 9)
        speed_y = randint(-9, 9)
    B.append([col, x_pos, y_pos, speed_x, speed_y])


def collision_balls(ball):
    """ Elastic collision of balls
    """
    if ball > 1:
        for i in range(len(B) - 1):
            for j in range(i + 1, len(B)):
                cat_x = B[i][1] - B[j][1]
                cat_y = B[i][2] - B[j][2]
                d = (cat_x * cat_x + cat_y * cat_y) ** 0.5
                if d == 0: d = 0.01
                sin = cat_x / d
                cos = cat_y / d
                spd_x1, spd_y1, spd_x2, spd_y2 = B[i][3], B[i][4], B[j][3], B[j][4]
                if d <= 2 * rad:
                    # поврот системы координат, расчет направления векторов
                    Vet_x1 = spd_x2 * sin + spd_y2 * cos
                    Vet_x2 = spd_x1 * sin + spd_y1 * cos

                    # разлет шаров при "склеивании"
                    dt = (2 * rad - d) / (Vet_x1 - Vet_x2)
                    if dt > 0.6: dt = 0.6
                    if dt < -0.6: dt = -0.6
                    B[i][1] -= spd_x1 * dt
                    B[i][2] -= spd_y1 * dt
                    B[j][1] -= spd_x2 * dt
                    B[j][2] -= spd_y2 * dt

                    Vet_y1 = -spd_x2 * cos + spd_y2 * sin
                    Vet_y2 = -spd_x1 * cos + spd_y1 * sin

                    Vet_x1, Vet_x2 = Vet_x2, Vet_x1
                    # поврот системы координат обратно
                    spd_x1 = Vet_x2 * sin - Vet_y2 * cos
                    spd_y1 = Vet_x2 * cos + Vet_y2 * sin
                    spd_x2 = Vet_x1 * sin - Vet_y1 * cos
                    spd_y2 = Vet_x1 * cos + Vet_y1 * sin

                    B[i][3], B[i][4], B[j][3], B[j][4] = spd_x1, spd_y1, spd_x2, spd_y2


def change_color(col):
    """Измениние цвета шарика при клике на него
    """
    if set_color:
        tmp = col
        if ((pos_x - x) ** 2 + (pos_y - y) ** 2) <= rad ** 2:
            while col == tmp:
                col = choice(colors)
    return col


def stop_ball(idx):
    """Останавливает выбранный шарик и получает его индекс
    """
    if move_ball == 1:
        for i in range(len(B)):
            if ((pos_x - B[i][1]) ** 2 + (pos_y - B[i][2]) ** 2) <= rad ** 2:
                B[i][3], B[i][4] = 0, 0
                idx = i
    return idx


while True:
    clock.tick(30)
    screen.fill((43, 45, 66))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:  # event.type == pygame.KEYDOWN
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_x, pos_y = pygame.mouse.get_pos()
            if event.button == 3:
                add_ball(pos_x, pos_y)  # добавить шарик в позицию мыши
                balls += 1
            elif event.button == 2:
                move_ball = 1
                ind = stop_ball(ind)  # остановить шарик в позиции мыши
            elif event.button == 1:
                set_color = 1

        #  управление остановленным шариком
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                B[ind][4] += -2
            if event.key == pygame.K_a:
                B[ind][3] += -2
            if event.key == pygame.K_d:
                B[ind][3] += 2
            if event.key == pygame.K_s:
                B[ind][4] += 2

    if balls > 0:
        for color, x, y, spd_x, spd_y in B:
            pygame.draw.circle(screen, color, (int(x), int(y)), rad)

        collision_balls(balls)  # соударение шаров

        for top in range(balls):
            [color, x, y, spd_x, spd_y] = B[top]
            spd_x, spd_y = reflect_ball(spd_x, spd_y)  # отскок от стенок
            color = change_color(color)  # изменение цвета по клику
            x += spd_x
            y += spd_y
            B[top] = [color, x, y, spd_x, spd_y]
        set_color = 0
    move_ball = 0
    pygame.display.flip()
