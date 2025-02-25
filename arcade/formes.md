# Dibuixar formes a Pygame

A Pygame podem dibuixar formes bàsiques directament amb funcions pròpies de Pygame.

[Aquí tens un vídeo d'exemple per si necessites repassar](https://www.youtube.com/watch?v=_nNVOMkSWaY).

## Rectangles:

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/81cb0f1b-9909-4982-a835-0ccdb8107cb0)

Un rectangle es dibuixa coneixent:

- El punt X d'origen (la posició horitzontal on comença el rectangle)
- El punt Y d'origen (la posició vertical on comença el rectangle)
- L'amplada del rectangle.
- L'alçada del rectangle.

El següent programa dibuixa un rectangle que comença a les coordenades X=100, Y=100 i té 400 pixels d'amplada i 200 d'alçada. 

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/14c1950e-556f-4163-aabb-691621de407d)

```
import pygame, sys
from pygame.locals import *

AMPLE = 600
ALT = 600
TAMANY = (AMPLE,ALT)
NEGRE = (0,0,0)
VERMELL = (255,0,0,0)
BLANC = (255,255,255)

pygame.init()
pantalla = pygame.display.set_mode(TAMANY)
pygame.display.set_caption('Rectangle')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill(BLANC)
    rectangle1 =  pygame.Rect(100, 100, 400, 200)
    pygame.draw.rect(pantalla, VERMELL, rectangle1)
    pygame.display.update()
```

La part important del programa són aquestes dues línies:

```
# Fiquem les coordenades i mesures del rectangle
rectangle1 =  pygame.Rect(100, 100, 400, 200)
# Dibuixem el rectangle
pygame.draw.rect(pantalla, VERMELL, rectangle1)
```

🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎

**Activitats:**

1. Utilitzant rectangles dibuixa una lletra:

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/806c2892-6f48-47f5-b1ec-3118436ed441)

2. Utilitzant rectangles de diferentes amplades fes una escala amb els colors de l'arc de Sant Martí.

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/d81d4c4c-a849-4714-8444-9c49475609d5)

🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎

## Rectangles sense farcir

Podem dibuixar rectangles que no tinguin farciment de color, només una línia exterior.

Per exemple, si volem dibuixar un rectangle sense farcir amb una vora de color negre de 10 pixels d'ample escrivim la línia de dibuix del rectangle així:

```
NEGRE = (0,0,0)
rectangle1 =  pygame.Rect(100, 100, 400, 200)
pygame.draw.rect(pantalla, NEGRE, rectangle1,10)
```

On el número 10 és l'amplada de la vora del rectangle.

## Cercles:

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/548d62fa-2568-4961-ab49-844456b8037e)

Per dibuixar un cercle utilitzem la funció draw circle a la que li passem el punt central del cercle i el radi del mateix:

Exemple:

```
import pygame, sys
from pygame.locals import *

AMPLE = 600
ALT = 600
TAMANY = (AMPLE,ALT)
NEGRE = (0,0,0)
VERMELL = (255,0,0,0)
BLANC = (255,255,255)

pygame.init()
pantalla = pygame.display.set_mode(TAMANY)
pygame.display.set_caption('Cercle')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill(BLANC)
    pygame.draw.circle(pantalla, VERMELL, (300,300),100)

    pygame.display.update()
```

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/5d9ebb7e-9fb7-437b-8d2c-06333cfe688c)


La línia que dibuixa el cercle és:

```
pygame.draw.circle(pantalla, VERMELL, (300,300),100)
```

## Cercle sense farcir

Podem dibuixar només la vora, per exemple el mateix cercle sense farcir, amb una vora de 5 pixels seria:

```
pygame.draw.circle(pantalla, VERMELL, (300,300),100,5)
```

🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎

1.- Fes un dibuix amb cercles sense farcir de les anelles olímpiques

![image](https://github.com/user-attachments/assets/f2cbdb9b-9717-4fac-b84e-e152c6f04aca)

2.- Fes un dibuix d'aquesta figura

![image](https://github.com/user-attachments/assets/ea693b70-b5cb-457b-b97f-767c98f39c26)

🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎�

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/ce9977ab-a4cd-4056-8bb9-678587ccf00b)

## Línia:

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/192bd0e7-6744-461d-8e92-006baced5f86)

## El·lipse:

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/8aed95a4-d5ea-4f8b-8906-0dd65e2d7c5d)

## Poligon:

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/d16dbdbc-a666-42c3-80a4-767e8b8f38b4)

