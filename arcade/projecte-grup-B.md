# Projecte final - Grup B
## Joc estil RPG (Pokemon)

## Grups

1. Dídac i Christian.
2. Diego i David.
3. Hugo i Joel.
4. Sergi i Carla.
5. Claudi i Felipe.
6. Kevin i Eric.
7. Xavi i Zumar.
 

## Fites

- Pantalla de joc: És el mapa pel que es mou el personatge.
- Pantalla de lluita: És una pantalla on els protagonistes lluiten contra uns enemics per torns.


# Recursos

- [Coding with Russ](http://www.codingwithruss.com/)
- [Level Editor](https://www.youtube.com/watch?v=-vQPEfK_GJQ)
- Instal·lar Github Desktop a Linux:

```
wget https://github.com/shiftkey/desktop/releases/download/release-3.4.3-linux1/GitHubDesktop-linux-amd64-3.4.3-linux1.deb
sudo dpkg -i GitHubDesktop-linux-amd64-3.4.3-linux1.deb
```

- Si un so té lag al joc heu de substituir:

```
pygame.init()
```
per

```
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()
```
