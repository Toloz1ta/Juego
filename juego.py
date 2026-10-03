import pygame
import sys
import random
import os

pygame.init()

ancho, alto = 1920, 1080
pantalla = pygame.display.set_mode ((ancho, alto))
pygame.display.set_caption ("DinoRun 🦖")
fps = pygame.time.Clock()
fuente = pygame.font.SysFont("arial", 24)

cielo = (130,200,229)
dino = pygame.image.load("sprites/Dinosaurio.png")
agachado = pygame.image.load ("sprites/agachado.png")
obstaculos = [
    pygame.image.load("sprites/cactus.png"),
    pygame.image.load("sprites/cactus.png"),
    pygame.image.load("sprites/roca.png")]

velocidad_obstaculos = 6

suelo = pygame.image.load("sprites/suelo.png")
color = (53,56,57)
puntos = 0

dino_rect = pygame.Rect(100, 300, 100, 100)
dino = pygame.transform.scale(dino, (100, 100))
suelo_y = 300
velocidad_y = 0
gravedad = 0.8
fuerza_salto = -15
en_el_suelo = True



jugando = True

while jugando: 
    fps.tick (60) 
    pantalla.fill (cielo)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    teclas = pygame.key.get_pressed()

    if teclas [pygame.K_LEFT]:
        dino_rect.x -= 5
    if teclas [pygame.K_RIGHT]:
        dino_rect.x += 5
    if teclas [pygame.K_DOWN]:
        pantalla.blit ("sprites/agachado.png")

    
    pygame.draw.rect (pantalla, cielo, dino_rect)
    
    pygame.display.flip()

pygame.quit()
sys.exit()
