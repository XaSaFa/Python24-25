# Dibuixar finestra

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/b06ec08c-dda5-40f8-9b87-eb1b7b23aade)

Una finestra de joc té certs components que s'han de definir abans de poder dibuixar-se.

- Icon: És una icona que es mostra a l'esquerra de la finestra, normalment representa d'alguna manera el programa, és com un logo.
- Caption: És un text, el títol que tindrà la finestra.
- Amplada: S'ha de definir l'amplada que tindrà la finestra.
- Alçada: Alçada que tindrà la finestra.
- Color de fons: Podem omplir una finestra amb un color.
- Imatge de fons: Podem dibuixar una imatge que serà el fons de la finestra.

```
# import the pygame module, so you can use it
import pygame, sys

WIDTH = 640
HIGH = 480
CAPTION_TEXT = "My Space Game"
# create a surface on screen that has the size of 640 x 480
screen = pygame.display.set_mode((WIDTH, HIGH))

# define a main function
def main():
    # initialize the pygame module
    pygame.init()
    pygame.display.set_caption(CAPTION_TEXT)    
    # define a variable to control the main loop
    running = True
    # main loop
    while running:
        # background set to BLACK
        screen.fill((0, 0, 0))
        # draw the screen
        pygame.display.flip()
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            running = False
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
```

## Tamany de la finestra

Tot i que definirem un tamany de finestra amb la seva **amplada** i **alçada** també podem fer que la finestra ocupi tota la pantalla amb el mode **FULLSCREEN**, cosa que farà que tots els elements dibuixats de la finestra s'escalin per ocupar tota la superfície de la pantalla de l'ordinador.

### FULLSCREEN

Per dibuixar la finestra a pantalla complerta hem de cridar la funció set_mode així:

```
screen = pygame.display.set_mode((640, 480), pygame.FULLSCREEN)
```

## Assets del projecte

El nostre projecte serà un videojoc, per aquest motiu comptarà amb fitxers d'imatge i so. 

Aquests fitxers els guardarem dins una carpeta anomenada assets al nostre projecte.

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/23d4ac69-982a-434c-9b06-277c7dca85e4)

🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎

**Activitats:**

1. Crea una finestra de títol "Zoo X" on X és el teu cognom, tamany 320x200 i color de fons groc.
2. Crea una finestra de títol "Ocean X" on X és el teu cognom, tamany 640x480 i color de fons blau.
3. Crea una finestra de títol "Space X" on X és el teu cognom, tamany 1280x720 i color de fons gris.
4. Crea una finestra de títol "War X" on X és el teu cognom, tamany 800x600 i color de fons verd.

🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎


# Fullscreen

Si volem que el joc s'executi en pantalla complerta utilitzarem un paràmetre especial quan generem la pantalla de joc.

En comptes de screen = pygame.display.set_mode((WIDTH, HIGH)) escriurem:

```
screen = pygame.display.set_mode((WIDTH, HIGH), pygame.FULLSCREEN)
```

D'aquesta manera la pantalla escala al tamany real del monitor.


# Mostrar imatge a Pygame

Quan volem mostrar una imatge, com per exemple el fons de pantalla del nostre joc, utilitzem la funció pygame.image.load

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/c3e1f82e-5c6a-476b-bf60-b8975b7f1774)

En aquest exemple mostrem una imatge de fons a una pantalla de 640x480:

```
BACKGROUND_IMAGE = 'assets/wallpaper.jpg'
AMPLADA = 640
ALTURA = 480
import pygame
pygame.init()
#screen = pygame.display.set_mode((640, 480), pygame.FULLSCREEN)
screen = pygame.display.set_mode((AMPLADA, ALTURA))
pygame.display.set_caption("Hello, World!")
background = pygame.image.load(BACKGROUND_IMAGE).convert()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        screen.blit(background, (0,0))
        pygame.display.update()
```

Els dos valors a la funció BLIT indiquen a quina posició es començarà a dibuixar la imatge, per exemple si fiquem com a valors 320 i 240 obtenim:

```
screen.blit(background, (320,240))
```

![image](https://github.com/XaSaFa/IntroduccioProgramacio/assets/110727546/0389a634-c524-43e6-99c5-108df258745b)

🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎

**Activitats:**

Torna a recuperar les finestres que has fet anteriorment però **carrega una imatge de fons adequada**.

1. Crea una finestra amb una icona d'un animal, de títol "Zoo X" on X és el teu cognom, tamany 320x200 i color de fons groc.
2. Crea una finestra amb una icona d'un peix, de títol "Ocean X" on X és el teu cognom, tamany 640x480 i color de fons blau.
3. Crea una finestra amb una icona d'un planeta, de títol "Space X" on X és el teu cognom, tamany 1280x720 i color de fons gris.
4. Crea una finestra amb una icona d'un tanc, de títol "War X" on X és el teu cognom, tamany 800x600 i color de fons verd.
5. Crea un programa que pregunta a l'usuari:
    - Títol de finestra.
    - Amplada de finestra.
    - Alçada de finestra.
    - Quantitat de vermell al color de fons.
    - Quantitat de verd al color de fons.
    - Quantitat de blau al color de fons.
    - Si el programa és a pantalla sencera o en mode finestra.
    - Després el programa crea la finestra demanada per l'usuari.
EXTRA: Que el programa et deixi escollir entre unes quantes imatges i mostri la imatge que escolli l'usuari.

🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎

