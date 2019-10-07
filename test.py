import serial
import pygame
arduino = serial.Serial(port='/dev/cu.usbmodem141401', baudrate=9600)
listaInteprete = [0,0,0,0,0,0,0,0]
pygame.init()
#definir tamaño ventana:
pantalla = pygame.display.set_mode((640,480))
verde1 = pygame.image.load("mario.png")
verde2 = pygame.image.load("mario.png")
azul1 = pygame.image.load("mario.png")
azul2 = pygame.image.load("mario.png")
naranja1 = pygame.image.load("mario.png")
naranja2 = pygame.image.load("mario.png")
amarillo1 = pygame.image.load("mario.png")
amarillo2 = pygame.image.load("mario.png")
rojo1 = pygame.image.load("mario.png")
rojo2 = pygame.image.load("mario.png")
active = pygame.image.load("mario.png")

while True:
    line = arduino.readline().decode('utf-8')
    partes = line.split(',')
    for i in range(8):
        listaInteprete[i]=partes[i]
    for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                exit()
    #verde rojo  amarillo azul naranja
    pantalla.blit(verde1,(0,0))
    pantalla.blit(rojo1,(32,0))
    pantalla.blit(amarillo1,(64,0))
    pantalla.blit(azul1,(96,0))
    pantalla.blit(naranja1,(118,0))
    #cambios de estados:
    if(listaInteprete[0]== 1):
        pantalla.blit(verde2,(0,0))
        if(listaInteprete[7]== 1):
            pantalla.blit(active,(0,0))
    if(listaInteprete[1]== 1):
        pantalla.blit(rojo2,(0,0))
        if(listaInteprete[7]== 1):
            pantalla.blit(active,(0,0))
    if(listaInteprete[2]== 1):
        pantalla.blit(amarillo2,(0,0))
        if(listaInteprete[7]== 1):
            pantalla.blit(active,(0,0))
    if(listaInteprete[3]== 1):
        pantalla.blit(azul2,(0,0))
        if(listaInteprete[7]== 1):
            pantalla.blit(active,(0,0))
    if(listaInteprete[4]== 1):
        pantalla.blit(naranja2,(0,0))
        if(listaInteprete[7]== 1):
            pantalla.blit(active,(0,0))
    pygame.display.update()
    
    