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
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window_open = False

    draw()
    pygame.display.update()