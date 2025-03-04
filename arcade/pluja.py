import random
import time

import pygame, sys
from pygame.gfxdraw import rectangle
from pygame.locals import *




AMPLE = 800
ALT = 600
TAMANY = (AMPLE,ALT)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
INDIGO = (75,0,130)
ORANGE = (255,102,0)
YELLOW = (255,255,0)
VIOLET = (127,0,255)
GREY = (128,128,128)
MAROON = (128,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
OLIVE = (128,128,0)
CYAN = (0,255,255)
PINK = (255,192,203)
MAGENTA = (255,0,255)
TAN = (210,180,140)
TEAL = (0,128,128)
pygame.init()
pantalla = pygame.display.set_mode(TAMANY)
pygame.display.set_caption('Color de fons')
i = 0
llista_gotes = []
total_gotes = 610

def genera_gota():
    genera = random.randint(1,10)
    if genera == 10:
        ample_gota = random.randint(4,6)
        llarg_gota = random.randint(9, 16)
        posicio_x = random.randint(0,AMPLE)
        rect1 = pygame.Rect(posicio_x,0,ample_gota,llarg_gota)
        llista_gotes.append(rect1)

while True: # main game loop
    time.sleep(0.003)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill(INDIGO)
    if len(llista_gotes) < total_gotes:
        genera_gota()
    for gota in llista_gotes:
        pygame.draw.rect(pantalla, WHITE, gota)
        gota.y += 1

        if gota.y > ALT:
            llista_gotes.remove(gota)
    pygame.display.update()

