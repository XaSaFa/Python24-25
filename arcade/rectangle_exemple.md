```
# import the pygame module, so you can use it
import pygame, sys

WIDTH = 320
HIGH = 240
CAPTION_TEXT = "LOLA INDITEX"
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
INDIGO = (75, 0, 130)
ORANGE = (255, 165, 0)
YELLOW = (255,255,0)
VIOLET = (148,0,211)
GREY = (128,128,128)
MARRON = (128,0,0)
BLACK = (0,0,0)
OLIVE = (134,139,73)
CYAN = (0,255,255)
PINK = (255,153,204)
MAGENTA = (255,0,255)
TAN = (210,180,140)
TEAL = (0,128,128)
WHITE = (255,255,255)
color = TEAL
import pygame, sys
from pygame.locals import *

pygame.init()
pantalla = pygame.display.set_mode((800,600))
pygame.display.set_caption('Rectangle')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill(WHITE)
    rectangle1 =  pygame.Rect(200, 200, 400, 200)
    pygame.draw.rect(pantalla, RED, rectangle1)
    pygame.display.update()
```
