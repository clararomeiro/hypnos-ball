import pygame

# Iniciando Janela
pygame.init()
window = pygame.display.set_mode((pygame.RESIZABLE, pygame.RESIZABLE), pygame.FULLSCREEN)
pygame.display.set_caption("Hypnos Ball")

# Definindo função draw


def draw():
    window.fill([255, 255, 255])


window_open = True

while window_open:
    draw()
    pygame.display.update()