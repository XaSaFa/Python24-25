# Bales

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/0a39f0be-2749-4166-971b-664bd22d6993)

Per a utilitzar bales necessitem varies coses:

1. Forma de la bala (o imatge).
2. Velocitat de la bala i direcció.
3. Cadència de tret que representarem en mil·lisegons entre trets.

Per exemple el nostre codi d'una bala per cada jugador serà:

```
# Bala rectangular blanca:
bala_imatge = pygame.Surface((4,10)) #definim una superficie rectangle de 4 pixels d'ample i 10 d'alçada
bala_imatge.fill(WHITE) #pintem la superficie de color blanc
bales_jugador1 = [] #llista on guardem les bales del jugador 1
bales_jugador2 = [] #llista on guardem les bales del jugador 2
velocitat_bales = 3
temps_entre_bales = 1000 #1 segon
temps_ultima_bala_jugador1 = 0 #per contar el temps que ha passat des de que ha disparat el jugador 1
temps_ultima_bala_jugador2 = 0 #per contar el temps que ha passat des de que ha disparat el jugador 2
```

Així les bales de cada jugador es guardaran en una llista diferent.

El jugador no podrà disparar si no ha passat temps_entre_bales des de la última vegada que ha disparat.

Per controlar el temps ho farem cada vegada que el jugador dispari:

```
 #jugador 1
if event.key == K_w and current_time - temps_ultima_bala_jugador1 >= temps_entre_bales:
  bales_jugador1.append(pygame.Rect(player_rect.centerx - 2, player_rect.top, 4, 10))
  temps_ultima_bala_jugador1 = current_time
```

Les bales es comportaran de la següent manera a cada bucle del programa:

1. Es mouran en la seva direcció tants pixels com la velocitat de la bala.
2. Si surten de la pantalla desapareixen (s'eliminen de la llista).
3. Si toquen l'enemic (col·lisionen) faran alguna acció: Matar l'enemic, apuntar puntuació al jugador que ha encertat...

Això ho controlem dins el bucle de joc:

```
  #Actualitzar i dibuixar les bales del jugador 1:
    for bala in bales_jugador1: # bucle que recorre totes les bales
        bala.y -= velocitat_bales # mou la bala
        if bala.bottom < 0 or bala.top > ALTURA: # comprova que no ha sortit de la pantalla
            bales_jugador1.remove(bala) # si ha sortit elimina la bala
        else:
            pantalla.blit(bala_imatge, bala) # si no ha sortit la dibuixa
        # Detectar col·lisions jugador 2:
        if player_rect2.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
            print("BOOM 1!")
            bales_jugador1.remove(bala)  # eliminem la bala
            # mostrem una explosió
            # eliminem el jugador 1 (un temps)
            # anotem punts al jugador 1
```

## Exemple de codi amb ús de bales:

```
import time
from pygame.locals import *
import pygame

AMPLADA = 800
ALTURA = 600
BACKGROUND_IMAGE = 'assets/fons.png'
MUSICA_FONS = 'assets/music.mp3'
WHITE = (255,255,255)



# Jugador 1:
player_image = pygame.image.load('assets/nau.png')
player_rect = player_image.get_rect(midbottom=(AMPLADA // 2, ALTURA - 10))
velocitat_nau = 4

# Jugador 2:
player_image2 = pygame.image.load('assets/nau.png')
player_rect2 = player_image2.get_rect(midbottom=(AMPLADA // 2, ALTURA - 500))
velocitat_nau2 = 4

# Bala rectangular blanca:
bala_imatge = pygame.Surface((4,10)) #definim una superficie rectangle de 4 pixels d'ample i 10 d'alçada
bala_imatge.fill(WHITE) #pintem la superficie de color blanc
bales_jugador1 = [] #llista on guardem les bales del jugador 1
bales_jugador2 = [] #llista on guardem les bales del jugador 2
velocitat_bales = 3
temps_entre_bales = 1000 #1 segon
temps_ultima_bala_jugador1 = 0 #per contar el temps que ha passat des de que ha disparat el jugador 1
temps_ultima_bala_jugador2 = 0 #per contar el temps que ha passat des de que ha disparat el jugador 2


pygame.init()
pantalla = pygame.display.set_mode((AMPLADA, ALTURA))
pygame.display.set_caption("Arcade")

# Control de FPS
clock = pygame.time.Clock()
fps = 30

def imprimir_pantalla_fons(image):
    # Imprimeixo imatge de fons:
    background = pygame.image.load(image).convert()
    pantalla.blit(background, (0, 0))

while True:
    #contador
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        # controlar trets de les naus
        if event.type == KEYDOWN:
            #jugador 1
            if event.key == K_w and current_time - temps_ultima_bala_jugador1 >= temps_entre_bales:
                bales_jugador1.append(pygame.Rect(player_rect.centerx - 2, player_rect.top, 4, 10))
                temps_ultima_bala_jugador1 = current_time
            # jugador 2
            if event.key == K_UP and current_time - temps_ultima_bala_jugador2 >= temps_entre_bales:
                bales_jugador2.append(pygame.Rect(player_rect2.centerx - 2, player_rect2.bottom -10, 4, 10))
                temps_ultima_bala_jugador2 = current_time

    # Moviment del jugador 1
    keys = pygame.key.get_pressed()
    if keys[K_a]:
        player_rect.x -= velocitat_nau
    if keys[K_d]:
        player_rect.x += velocitat_nau
    # Moviment del jugador 2
    if keys[K_LEFT]:
        player_rect2.x -= velocitat_nau2
    if keys[K_RIGHT]:
        player_rect2.x += velocitat_nau2



    # Mantenir al jugador dins de la pantalla:
    player_rect.clamp_ip(pantalla.get_rect())
    player_rect2.clamp_ip(pantalla.get_rect())

    #dibuixar el fons:
    imprimir_pantalla_fons(BACKGROUND_IMAGE)

    #Actualitzar i dibuixar les bales del jugador 1:
    for bala in bales_jugador1: # bucle que recorre totes les bales
        bala.y -= velocitat_bales # mou la bala
        if bala.bottom < 0 or bala.top > ALTURA: # comprova que no ha sortit de la pantalla
            bales_jugador1.remove(bala) # si ha sortit elimina la bala
        else:
            pantalla.blit(bala_imatge, bala) # si no ha sortit la dibuixa
        # Detectar col·lisions jugador 2:
        if player_rect2.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
            print("BOOM 1!")
            bales_jugador1.remove(bala)  # eliminem la bala
            # mostrem una explosió
            # eliminem el jugador 1 (un temps)
            # anotem punts al jugador 1

    # Actualitzar i dibuixar les bales del jugador 2:
    for bala in bales_jugador2:
        bala.y += velocitat_bales
        if bala.bottom < 0 or bala.top > ALTURA:
            bales_jugador2.remove(bala)
        else:
            pantalla.blit(bala_imatge, bala)
        # Detectar col·lisions jugador 1:
        if player_rect.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
            print("BOOM 2!")
            bales_jugador2.remove(bala)  # eliminem la bala
            # mostrem una explosió
            # eliminem el jugador 1 (un temps)
            # anotem punts al jugador 1

    #dibuixar els jugadors:
    pantalla.blit(player_image, player_rect)
    pantalla.blit(player_image2, player_rect2)

    pygame.display.update()
    clock.tick(fps)
```


# Exemple amb vides de jugador 1:

```
import time
from pygame.locals import *
import pygame

AMPLADA = 800
ALTURA = 600
BACKGROUND_IMAGE = 'assets/fons2025.png'
MUSICA_FONS = 'assets/music.mp3'
WHITE = (255,255,255)



# Jugador 1:
player_image = pygame.image.load('assets/nau2025.png')
player_rect = player_image.get_rect(midbottom=(AMPLADA // 2, ALTURA - 10))
velocitat_nau = 5


# Jugador 2:
player_image2 = pygame.image.load('assets/nau2025.png')
player_rect2 = player_image2.get_rect(midbottom=(AMPLADA // 2, ALTURA - 500))
velocitat_nau2 = 5

# vides:
vides_jugador1 = 3
vides_jugador2 = 3
vides_jugador1_image = pygame.image.load('assets/vida1.png')


# Bala rectangular blanca:
bala_imatge = pygame.Surface((4,10)) #definim una superficie rectangle de 4 pixels d'ample i 10 d'alçada
bala_imatge.fill(WHITE) #pintem la superficie de color blanc
bales_jugador1 = [] #llista on guardem les bales del jugador 1
bales_jugador2 = [] #llista on guardem les bales del jugador 2
velocitat_bales = 5
temps_entre_bales = 500 #1 segon
temps_ultima_bala_jugador1 = 0 #per contar el temps que ha passat des de que ha disparat el jugador 1
temps_ultima_bala_jugador2 = 0 #per contar el temps que ha passat des de que ha disparat el jugador 2


pygame.init()
pantalla = pygame.display.set_mode((AMPLADA, ALTURA))
pygame.display.set_caption("Arcade")

# Control de FPS
clock = pygame.time.Clock()
fps = 30

def imprimir_pantalla_fons(image):
    # Imprimeixo imatge de fons:
    background = pygame.image.load(image).convert()
    pantalla.blit(background, (0, 0))

while True:
    #contador
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        # controlar trets de les naus
        if event.type == KEYDOWN:
            #jugador 1
            if event.key == K_w and current_time - temps_ultima_bala_jugador1 >= temps_entre_bales:
                bales_jugador1.append(pygame.Rect(player_rect.centerx - 2, player_rect.top, 4, 10))
                temps_ultima_bala_jugador1 = current_time
            # jugador 2
            if event.key == K_UP and current_time - temps_ultima_bala_jugador2 >= temps_entre_bales:
                bales_jugador2.append(pygame.Rect(player_rect2.centerx - 2, player_rect2.bottom -10, 4, 10))
                temps_ultima_bala_jugador2 = current_time

    # Moviment del jugador 1
    keys = pygame.key.get_pressed()
    if keys[K_a]:
        player_rect.x -= velocitat_nau
    if keys[K_d]:
        player_rect.x += velocitat_nau
    # Moviment del jugador 2
    if keys[K_LEFT]:
        player_rect2.x -= velocitat_nau2
    if keys[K_RIGHT]:
        player_rect2.x += velocitat_nau2



    # Mantenir al jugador dins de la pantalla:
    player_rect.clamp_ip(pantalla.get_rect())
    player_rect2.clamp_ip(pantalla.get_rect())

    #dibuixar el fons:
    imprimir_pantalla_fons(BACKGROUND_IMAGE)

    #Actualitzar i dibuixar les bales del jugador 1:
    for bala in bales_jugador1: # bucle que recorre totes les bales
        bala.y -= velocitat_bales # mou la bala
        if bala.bottom < 0 or bala.top > ALTURA: # comprova que no ha sortit de la pantalla
            bales_jugador1.remove(bala) # si ha sortit elimina la bala
        else:
            pantalla.blit(bala_imatge, bala) # si no ha sortit la dibuixa
        # Detectar col·lisions jugador 2:
        if player_rect2.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
            print("BOOM 1!")
            bales_jugador1.remove(bala)  # eliminem la bala
            vides_jugador2 = vides_jugador2 -1
            print("vides jugador 2:", vides_jugador2)
            # mostrem una explosió
            # eliminem el jugador 1 (un temps)
            # anotem punts al jugador 1

    # Actualitzar i dibuixar les bales del jugador 2:
    for bala in bales_jugador2:
        bala.y += velocitat_bales
        if bala.bottom < 0 or bala.top > ALTURA:
            bales_jugador2.remove(bala)
        else:
            pantalla.blit(bala_imatge, bala)
        # Detectar col·lisions jugador 1:
        if player_rect.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
            print("BOOM 2!")
            bales_jugador2.remove(bala)  # eliminem la bala
            vides_jugador1 = vides_jugador1 - 1
            print("vides jugador 1:",vides_jugador1)
            # mostrem una explosió
            # eliminem el jugador 1 (un temps)
            # anotem punts al jugador 1

    #dibuixar els jugadors:
    pantalla.blit(player_image, player_rect)
    pantalla.blit(player_image2, player_rect2)

    #dibuixar bales
    if vides_jugador1 >= 3:
        pantalla.blit(vides_jugador1_image,(700,550))
    if vides_jugador1 >= 2:
        pantalla.blit(vides_jugador1_image, (720, 550))
    if vides_jugador1 >= 1:
        pantalla.blit(vides_jugador1_image, (740, 550))

    pygame.display.update()
    clock.tick(fps)
```
