import pygame, random

screen_width = 920
screen_height = 600

white_color = (200, 200, 200)
back_color = pygame.Color('grey12')

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))


def user_1_controller():
    global user_1_speed
    if user_1.top + 50 < screen_height:
        user_1.top += user_1_speed


def user_2_controller():
    global user_2_speed
    if user_2.top + 50 < screen_height:
        user_2.top += user_2_speed


def start_bola():
    global speed_bola_x, speed_bola_y

    if bola.left + 50 > screen_width or bola.left < 0:
        bola.top = screen_height // 2
        bola.left = screen_width // 2

        speed_bola_x = 3 * random.choice((1, -1))
        speed_bola_y = 3 * random.choice((1, -1))


def mover_bola():
    global speed_bola_x, speed_bola_y

    if bola.top + 50 > screen_height or bola.top < 0:
        speed_bola_x = -speed_bola_x

    if bola.left < 10 and user_1.top < bola.top < user_1.top + 140:
        speed_bola_y = -speed_bola_y

    if bola.right < 10 and user_2.top < bola.top < user_2.top + 140:
        speed_bola_y = -speed_bola_y

    start_bola()

    bola.top += speed_bola_x
    bola.left += speed_bola_y


user_1 = pygame.Rect(10, 10, 10, 140)
user_2 = pygame.Rect(900, 10, 10, 140)
bola = pygame.Rect(10, 10, 50, 50)
user_1_speed = 0
user_2_speed = 0
speed_bola_x = 3
speed_bola_y = 3

while True:
    screen.fill(back_color)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                user_1_speed = -3
            if event.key == pygame.K_DOWN:
                user_1_speed = 3
            if event.key == pygame.K_w:
                user_2_speed = -3
            if event.key == pygame.K_s:
                user_2_speed = 3
        elif event.type == pygame.KEYUP:
            user_1_speed = 0
            user_2_speed = 0

    user_1_controller()
    user_2_controller()
    mover_bola()

    pygame.draw.rect(screen, white_color, user_1)
    pygame.draw.rect(screen, white_color, user_2)
    pygame.draw.ellipse(screen, white_color, bola)

    pygame.display.flip()
    clock.tick(60)
