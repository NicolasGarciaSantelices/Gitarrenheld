import pygame
from pygame.locals import *
pygame.init()
pantalla = pygame.display.set_mode((1000,800))
imagen = pygame.image.load("mario.png")
imagen = pygame.transform.scale(imagen,(100,100))#Escalamos la imagen en Pygame

while True:
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            exit()
    pantalla.blit(imagen,(100,100))
    pygame.display.update()
