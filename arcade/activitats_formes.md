# Activitats de formes

1. Fes un programa que dibuixi aquesta finestra:

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/fdb1f10d-dd7c-4fd3-abaa-b7f9be461de4)

```
import pygame, sys
from pygame.locals import *

AMPLE = 800
ALT = 600
TAMANY = (AMPLE,ALT)
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

pygame.init()
pantalla = pygame.display.set_mode(TAMANY)
pygame.display.set_caption('Rectangle')
i = 1
d = 1
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill(WHITE)

    pygame.draw.rect(pantalla, BLACK, (100, 100, 600, 400))
    pygame.draw.rect(pantalla, WHITE, (140, 140, 520, 320))
    pygame.draw.rect(pantalla, BLUE, (180, 180, 440, 240))
    pygame.draw.rect(pantalla, GREEN, (220, 220, 360, 160))
    pygame.draw.rect(pantalla, RED, (260, 260, 280, 80))
    pygame.display.update()

```
2. Fes un programa que dibuixi aquesta finestra:

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/41b722f0-21c5-46fb-8180-0bafc99265d2)

```
import pygame, sys
from pygame.locals import *

AMPLE = 800
ALT = 600
TAMANY = (AMPLE,ALT)
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

pygame.init()
pantalla = pygame.display.set_mode(TAMANY)
pygame.display.set_caption('Rectangle')
i = 1
d = 1
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill(WHITE)

    pygame.draw.rect(pantalla,BLUE,(100,100,400,400))
    pygame.draw.ellipse(pantalla, RED, (100, 100, 400, 400))
    pygame.draw.polygon(pantalla, YELLOW,((300,100),(130,400),(470,400)))
    pygame.display.update()
```

3. Fes un programa que dibuixi una cara:

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/3edf2186-821c-4016-8d52-fc290cd7ca6c)

4. Fes un programa que dibuixi un paisatge
