import sys

import pygame

pygame.init()

# set window
width = 300
height = 150
R_scr, G_scr, B_scr = 240, 228, 209

# set digits
R, G, B = 162, 0, 0
size_digits = 4
shift = 0

# set button
R_but, G_but, B_but = 209, 160, 82
R_press, G_press, B_press = 240, 228, 209
coord_x, coord_y = -1, -1
# color icon button
R_emb, G_emb, B_emb = 162, 0, 0

start = False
left = 0
right = 0
tmp = -1

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('My Timer')
clock = pygame.time.Clock()


def dict_number(index, s):
    A = {0: [(130 + s, 30), (160 + s, 30), (160 + s, 80), (130 + s, 80), (130 + s, 30)],
         1: [(160 + s, 30), (160 + s, 80)],
         2: [(130 + s, 30), (160 + s, 30), (160 + s, 55), (130 + s, 55), (130 + s, 80), (160 + s, 80)],
         3: [(130 + s, 30), (160 + s, 30), (160 + s, 55), (130 + s, 55), (160 + s, 55), (160 + s, 80), (130 + s, 80)],
         4: [(130 + s, 30), (130 + s, 55), (160 + s, 55), (160 + s, 30), (160 + s, 80)],
         5: [(160 + s, 30), (130 + s, 30), (130 + s, 55), (160 + s, 55), (160 + s, 80), (130 + s, 80)],
         6: [(160 + s, 30), (130 + s, 30), (130 + s, 80), (160 + s, 80), (160 + s, 55), (130 + s, 55)],
         7: [(130 + s, 30), (160 + s, 30), (160 + s, 80)],
         8: [(130 + s, 30), (160 + s, 30), (160 + s, 80), (130 + s, 80), (130 + s, 30), (130 + s, 55), (160 + s, 55)],
         9: [(130 + s, 80), (160 + s, 80), (160 + s, 30), (130 + s, 30), (130 + s, 55), (160 + s, 55)]
         }
    return A[index]


def number_display(index):
    index_seconds = index % 10
    pygame.draw.lines(screen, (R, G, B), False, dict_number(index_seconds, 90), size_digits)

    index_ten_seconds = (index // 10) % 6
    pygame.draw.lines(screen, (R, G, B), False, dict_number(index_ten_seconds, 40), size_digits)

    index_minutes = (index // 60) % 10
    pygame.draw.lines(screen, (R, G, B), False, dict_number(index_minutes, -30), size_digits)

    index_ten_minutes = (index // 600) % 6
    pygame.draw.lines(screen, (R, G, B), False, dict_number(index_ten_minutes, -80), size_digits)


while True:

    clock.tick(30)   # FPS
    screen.fill((R_scr, G_scr, B_scr))
    sec = pygame.time.get_ticks() // 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif pygame.mouse.get_pressed()[0]:
            coord_x, coord_y = pygame.mouse.get_pos()

            if 40 <= coord_x <= 130 and 100 <= coord_y <= 135:
                start = True
                tmp = sec
                left = 1
            elif 170 <= coord_x <= 260 and 100 <= coord_y <= 135:
                start = False
                right = 1

    if start is True:
        sec -= tmp
        number_display(sec)

    # Next need to change

    # start button
    pygame.draw.lines(screen, (R_but, G_but, B_but), True, [(41, 101), (130, 101), (130, 135), (41, 135)], 2)
    pygame.draw.rect(screen, (235, 215, 183), [40, 100, 90, 35])

    # pressing the start button
    if 40 <= coord_x <= 120 and 100 <= coord_y <= 135 and left == 1:
        left = 0
        pygame.draw.lines(screen, (R_press, G_press, B_press), True, [(40, 100), (130, 100), (130, 135), (40, 135)], 2)

    # icon start button
    pygame.draw.aalines(screen, (R_emb, G_emb, B_emb), True, [[78, 105], [100, 117], [78, 130]])

    # stop button
    pygame.draw.lines(screen, (R_but, G_but, B_but), True, [(171, 101), (260, 101), (260, 135), (171, 135)], 2)
    pygame.draw.rect(screen, (235, 215, 183), [170, 100, 90, 35])

    # pressing the stop button
    if 180 <= coord_x <= 260 and 100 <= coord_y <= 135 and right == 1:
        right = 0
        pygame.draw.lines(screen, (R_press, G_press, B_press), True, [(170, 100), (260, 100), (260, 135), (170, 135)],
                          2)
    # icon stop button
    pygame.draw.aalines(screen, (R_emb, G_emb, B_emb), True, [[205, 106], [228, 106], [228, 129], [205, 129]])

    # two points
    pygame.draw.line(screen, (R, G, B), (150, 70), (150, 76), 4)
    pygame.draw.line(screen, (R, G, B), (150, 45), (150, 51), 4)

    # frame
    pygame.draw.lines(screen, (54, 19, 5), True, [(0, 1), (299, 1), (299, 149), (0, 149)], 1)

    pygame.display.flip()
