import pygame
from pygame.locals import *
pygame.init()
pantalla = pygame.display.set_mode((640,480))
 imagen = pygame.image.load("mario.png")
while True:
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            exit()