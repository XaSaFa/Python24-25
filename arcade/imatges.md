# Assets del projecte

De vegades un projecte que fem en Pygame necessita imatges o sons, quan això passa normalment crearem una carpeta dins el projecte per guardar aquest tipus de fitxers.

Aquesta carpeta es dirà assets que és el terme utilitzat en el sector per denominar els recursos que utilitza el nostre programa.

En aquest exemple veiem una carpeta assets amb 4 imatges.

![image](https://github.com/user-attachments/assets/3f1f96cf-cb16-43de-ada9-42a90b6e79d0)

# Mostrar imatge a Pygame

Quan volem mostrar una imatge, com per exemple el fons de pantalla del nostre joc, utilitzem la funció pygame.image.load

A l'exemple següent tenim una imatge d'un orc que mostrem a la posició 0,0 de la pantalla:

```
# En aquest exemple mostrem una imatge d'un orc a una pantalla de 640x480:
import pygame
orc_image = 'assets/orco.png'
pygame.init()
pantalla = pygame.display.set_mode((640, 480))
orc = pygame.image.load(orc_image)
while True:
    pantalla.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        pantalla.blit(orc, (0, 0))
        pygame.display.update()
```

Si volem que la imatge estigui a una altra posició hem de canviar les coordenades a la línia ```pantalla.blit(orc, (0, 0))```

🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎
- Activitat 1: Quines seran les coordenades del programa si volem que l'orc es mostri al mig de la pantalla?
- Activitat 2: Busca una imatge d'un paisatge i dibuixa una imatge d'un personatge davant.
- Activitat 3: Fes que la imatge del personatge es mogui d'un costat a l'altre de la pantalla.
- Activitat 4: Apliqueu un efecte pluja a l'escenari utilitzant el codi d'exemple pluja que hi ha als apunts. 
🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎

