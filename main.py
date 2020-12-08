import pygame

# Iniciando Janela
pygame.init()
window = pygame.display.set_mode((pygame.RESIZABLE, pygame.RESIZABLE), pygame.FULLSCREEN)
pygame.display.set_caption("Hypnos Ball")


window_open = True
pos_x = 60
pos_y = 60
vel = 1

while window_open:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window_open = False
            elif event.key == pygame.K_DOWN and pos_y == 60:
                pos_y = 500
            elif event.key == pygame.K_DOWN and pos_y == 500:
                pos_y = 1010
            elif event.key == pygame.K_UP and pos_y == 1010:
                pos_y = 500
            elif event.key == pygame.K_UP and pos_y == 500:
                pos_y = 60

    # Desenhando
    window.fill([255, 255, 255])
    pos_x = pos_x + vel
    pygame.draw.circle(window, (0, 100, 158), (pos_x, pos_y), 50)
    pygame.display.update()
