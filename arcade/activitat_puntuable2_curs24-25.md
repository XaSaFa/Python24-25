# Imatges

- Nau jugador 1
- Nau jugador 2
- Fons 800x600
- Vida jugador 1
- Vida jugador 2
- Pantalla Game Over 800x600
- Bala jugador 1
- Bala jugador 2

# Sons

- Música principal
- Música Game Over
- Efecte de so de jugador 1 disparant
- Efecte de so de jugador 2 disparant
- Efecte de so jugador 1 perd una vida
- Efecte de so jugador 2 perd una vida

# Codi
- Jugador 1 dispara (ajustar jugabilitat, velocitat i cadència)
- Jugador 2 dispara (ajustar jugabilitat)
- Dibuixar vides dels jugadors

# Codi que queda per fer:
- Quan una nau perd totes les vides, surt una pantalla de game over, sona la música de game over i surt un text indicant quin jugador ha guanyat.
- Menú inici.
  - Títol del joc.
  - 1.- Jugar
  - 2.- Crèdits
  - 3.- Sortir
- Crédits.
  - Programació.
  - Gràfics.
  - Música i So.

## Codi provisional:

```
import time
from pygame.locals import *
import pygame

guanyador = 0
AMPLADA = 800
ALTURA = 600
BACKGROUND_IMAGE = 'assets/fons.png'
MUSICA_FONS = 'assets/music.mp3'
WHITE = (255,255,255)
MAGENTA = (207,52,118)


# pantalles:
# pantalla 1 = Menú
# pantalla 2 = Crèdits
# pantalla 3 = Joc
# pantalla 4 = Game Over!
pantalla_actual = 3

# Vides jugador 1:
vides_image1 = pygame.image.load('assets/vida_jugador1.png')


# Jugador 1:
player_image = pygame.image.load('assets/nau.png')
player_rect = player_image.get_rect(midbottom=(AMPLADA // 2, ALTURA - 10))
velocitat_nau = 6
vides_jugador1 = 3

# Jugador 2:
player_image2 = pygame.image.load('assets/nau.png')
player_rect2 = player_image2.get_rect(midbottom=(AMPLADA // 2, ALTURA - 500))
velocitat_nau2 = 6
vides_jugador2 = 3

# Bala rectangular blanca:
bala_imatge = pygame.Surface((8,15)) #definim una superficie rectangle de 4 pixels d'ample i 10 d'alçada
bala_imatge.fill(WHITE) #pintem la superficie de color blanc
bales_jugador1 = [] #llista on guardem les bales del jugador 1
bales_jugador2 = [] #llista on guardem les bales del jugador 2
velocitat_bales = 12
temps_entre_bales = 300 #1 segon
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
        if pantalla_actual == 3:
            if event.type == KEYDOWN:
                #jugador 1
                if event.key == K_w and current_time - temps_ultima_bala_jugador1 >= temps_entre_bales:
                    bales_jugador1.append(pygame.Rect(player_rect.centerx - 2, player_rect.top, 4, 10))
                    temps_ultima_bala_jugador1 = current_time
                # jugador 2
                if event.key == K_UP and current_time - temps_ultima_bala_jugador2 >= temps_entre_bales:
                    bales_jugador2.append(pygame.Rect(player_rect2.centerx - 2, player_rect2.bottom -10, 4, 10))
                    temps_ultima_bala_jugador2 = current_time

    # Mostrar Pantalla de Menú:
    if pantalla_actual == 1:
        pass
    # Mostrar Pantalla de Crèdits:
    elif pantalla_actual == 2:
        pass
    
    # Mostrar Pantalla de Game Over:
    elif pantalla_actual == 4:
        imprimir_pantalla_fons('assets/game_over1.png')
        font = pygame.font.SysFont(None, 100)
        text = "Player " + str(guanyador) + " Wins!"
        img = font.render(text, True, MAGENTA)
        pantalla.blit(img,(130,30))
    # Mostrar Pantalla de Joc:
    elif pantalla_actual == 3:
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
                vides_jugador2 = vides_jugador2 - 1
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
                vides_jugador1 =  vides_jugador1 - 1
                # mostrem una explosió
                # eliminem el jugador 1 (un temps)
                # anotem punts al jugador 1

        #dibuixar els jugadors:
        pantalla.blit(player_image, player_rect)
        pantalla.blit(player_image2, player_rect2)

        #dibuixar vides jugador 1:
        if vides_jugador1 >= 3:
            pantalla.blit(vides_image1,(700,560)) #3
        if vides_jugador1 >= 2:
            pantalla.blit(vides_image1, (720, 560)) #2
        if vides_jugador1 >= 1:
            pantalla.blit(vides_image1, (740, 560)) #1

        # dibuixar vides jugador 2:
        if vides_jugador2 >= 3:
            pantalla.blit(vides_image1, (60, 40))  # 3
        if vides_jugador2 >= 2:
            pantalla.blit(vides_image1, (80, 40))  # 2
        if vides_jugador2 >= 1:
            pantalla.blit(vides_image1, (100, 40))  # 1

        if vides_jugador1 <= 0 or vides_jugador2 <= 0:
            pantalla_actual = 4
            guanyador = 1
            if vides_jugador1 <= 0:
                guanyador = 2

    pygame.display.update()
    clock.tick(fps)
```
