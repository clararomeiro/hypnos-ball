import os, sys
dirpath = os.getcwd()
sys.path.append(dirpath)
if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)
###

import pygame
from time import sleep

# Iniciando Janela
pygame.init()
window = pygame.display.set_mode((pygame.RESIZABLE, pygame.RESIZABLE), pygame.FULLSCREEN)
pygame.display.set_caption("Hypnos Ball")


window_open = True
pos_x = 85
pos_y = 85
vel = 0.4
clock = pygame.time.Clock()

if __name__ == "__main__":
    while window_open:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                window_open = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                if pos_y == 85:
                    pos_y = (window.get_height()-85)/2
                elif pos_y == (window.get_height()-85)/2:
                    pos_y = window.get_height()-85
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                if pos_y == window.get_height()-85:
                    pos_y = (window.get_height()-85)/2
                elif pos_y == (window.get_height()-85)/2:
                    pos_y = 85
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    vel = 0.4
                elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    vel = 0.5
                elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    vel = 0.7

        if pos_x == window.get_width()-85:
            sleep(vel)
            pos_x = 85
        elif pos_x == 85:
            sleep(vel)
            pos_x = window.get_width()-85

        # Desenhando
        window.fill([255, 255, 255])
        pygame.draw.circle(window, (201, 26, 26), (pos_x, pos_y), 75)
        pygame.display.update()
