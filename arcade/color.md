# Color a Pygame

A Pygame s'utilitza el sistema RGB (Red, Green, Blue) per a pintar colors per pantalla, tot i que es poden utilitzar altres sistemes també.

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/5601599c-b860-4267-a5f8-fbf412ac4102)

Aquí teniu dos generadors de colors online:

- [GENERADOR 1](https://www.rapidtables.com/web/color/RGB_Color.html)
- [GENERADOR 2](https://www.w3schools.com/colors/colors_rgb.asp)

## Color de fons:

Per ficar color de fons de la pantalla fem servir la funció fill.

El següent programa fica el color CYAN de fons:

```
import pygame, sys
from pygame.locals import *

AMPLE = 600
ALT = 600
TAMANY = (AMPLE,ALT)
CYAN = (0,255,255)

pygame.init()
pantalla = pygame.display.set_mode(TAMANY)
pygame.display.set_caption('Color de fons')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill(CYAN)
    pygame.display.update()
```

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/a49376aa-4138-49e5-9e4d-c0cd990bef31)

🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎

**Activitats:**

Canvia el programa anterior per fer que l'usuari escolli un color de la taula següent i el programa dibuixi una finestra del color seleccionat de fons.

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/7547355b-8224-4551-9e5a-cb04c58b835a)


🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎
