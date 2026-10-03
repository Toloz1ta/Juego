import pygame
import sys

pygame.init()

ANCHO, ALTO = 800, 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("El Cuadrado Saltarín")
reloj = pygame.time.Clock()
FUENTE = pygame.font.SysFont("arial", 24)

# Colores
CIELO = (135, 206, 235)
AZUL = (40, 90, 200)
ROJO = (200, 50, 50)
BLANCO = (255, 255, 255)

# Jugador
jugador = pygame.Rect(80, 300, 40, 40)
suelo_y = 300
velocidad_y = 0
gravedad = 0.8
fuerza_salto = -15
en_el_suelo = True

# Obstáculo
obstaculo = pygame.Rect(800, 320, 30, 30)
velocidad_obstaculo = 6

# Puntaje
puntos = 0

jugando = True
while jugando:
    reloj.tick(60)

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    keys = pygame.key.get_pressed()

    # Movimiento izquierda/derecha
    if keys[pygame.K_LEFT]:
        jugador.x -= 5
    if keys[pygame.K_RIGHT]:
        jugador.x += 5

    # Salto
    if keys[pygame.K_SPACE] and en_el_suelo:
        velocidad_y = fuerza_salto
        en_el_suelo = False

    # Gravedad
    velocidad_y += gravedad
    jugador.y += velocidad_y

    if jugador.y >= suelo_y:
        jugador.y = suelo_y
        velocidad_y = 0
        en_el_suelo = True

    # Mover obstáculo
    obstaculo.x -= velocidad_obstaculo
    if obstaculo.right < 0:
        obstaculo.x = 800
        puntos += 1

    # Colisión
    if jugador.colliderect(obstaculo):
        jugando = False

    # Dibujar
    pantalla.fill(CIELO)
    pygame.draw.rect(pantalla, AZUL, jugador)
    pygame.draw.rect(pantalla, ROJO, obstaculo)

    texto = FUENTE.render(f"Puntos: {puntos}", True, BLANCO)
    pantalla.blit(texto, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()