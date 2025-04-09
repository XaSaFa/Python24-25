import time
from pygame.locals import *
import pygame


# Tamany finestra
VIEW_WIDTH = 800
VIEW_HEIGHT = 800

# iniciem pygame
pygame.init()
pantalla = pygame.display.set_mode((VIEW_WIDTH, VIEW_HEIGHT))
pygame.display.set_caption("Arcade")

# Control de FPS
clock = pygame.time.Clock()
fps = 30

animation_protagonist_speed = 500
last_change_frame_time = 0


pebrot_state = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    current_time = pygame.time.get_ticks()
    pantalla.fill((0,0,0))

    # pebrot:
    pebrot_image = pygame.image.load('assets/pebrot_vermell.png')
    if pebrot_state == 0:
        pantalla.blit(pebrot_image,(100,100))
    elif pebrot_state == 1:
        pebrot_image = pygame.transform.scale(pebrot_image,(100,100))
        pantalla.blit(pebrot_image, (100, 100))

    if current_time - last_change_frame_time >= animation_protagonist_speed:
        last_change_frame_time = current_time
        if pebrot_state == 0:
            pebrot_state = 1
        else:
            pebrot_state = 0

    pygame.display.update()
    clock.tick(fps)
