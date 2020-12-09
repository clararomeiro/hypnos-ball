import pygame
from time import sleep

# Iniciando Janela
pygame.init()
window = pygame.display.set_mode((pygame.RESIZABLE, pygame.RESIZABLE), pygame.FULLSCREEN)
pygame.display.set_caption("Hypnos Ball")


window_open = True
pos_x = 85
pos_y = 85
vel = 10
clock = pygame.time.Clock()

while window_open:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            window_open = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            if pos_y == 85:
                pos_y = 500
            elif pos_y == 500:
                pos_y = 990
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            if pos_y == 990:
                pos_y = 500
            elif pos_y == 500:
                pos_y = 85

    if pos_x == 1800:
        sleep(0.5)
        pos_x = 85
    elif pos_x == 85:
        sleep(0.5)
        pos_x = 1800

    # Desenhando
    window.fill([255, 255, 255])
    pygame.draw.circle(window, (0, 100, 158), (pos_x, pos_y), 75)
    pygame.display.update()
