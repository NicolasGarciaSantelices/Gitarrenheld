
import serial
import pygame
arduino = serial.Serial(port='/dev/cu.usbmodem146301', baudrate=9600)
listaInteprete = [0,0,0,0,0,0,0,0]
pygame.init()

#definir tamaño ventana:
pantalla = pygame.display.set_mode((160,32))
pygame.display.set_caption('Gitarren Held')
verde1 = pygame.image.load("verde1.png")
verde2 = pygame.image.load("Verde2.png")
azul1 = pygame.image.load("Azul1.png")
azul2 = pygame.image.load("Azul2.png")
naranja1 = pygame.image.load("Naranjo1.png")
naranja2 = pygame.image.load("Naranja2.png")
amarillo1 = pygame.image.load("Amarillo1.png")
amarillo2 = pygame.image.load("Amarillo2.png")
rojo1 = pygame.image.load("Rojo.png")
rojo2 = pygame.image.load("Rojo2.png")
active = pygame.image.load("ON.png")
white = [255, 255, 255]
pantalla.fill(white)
while True:
    pantalla.fill(white)
    line = arduino.readline().decode('utf-8')
    print(line)
    partes = line.split(',')
    for i in range(8):
        listaInteprete[i]=int(partes[i])
    for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                exit()
    #verde rojo  amarillo azul naranja
    pantalla.blit(verde1,(0,0))
    pantalla.blit(rojo1,(32,0))
    pantalla.blit(amarillo1,(64,0))
    pantalla.blit(azul1,(96,0))
    pantalla.blit(naranja1,(128,0))
    #cambios de estados:
    if(listaInteprete[0]== 1):
        pantalla.blit(verde2,(0,0))
        if(listaInteprete[7]== 1):
            pantalla.blit(active,(0,0))
    if(listaInteprete[1]== 1):
        pantalla.blit(rojo2,(32,0))
        if(listaInteprete[7]== 1):
            pantalla.blit(active,(32,0))
    if(listaInteprete[2]== 1):
        pantalla.blit(amarillo2,(64,0))
        if(listaInteprete[7]== 1):
            pantalla.blit(active,(64,0))
    if(listaInteprete[3]== 1):
        pantalla.blit(azul2,(96,0))
        if(listaInteprete[7]== 1):
            pantalla.blit(active,(96,0))
    if(listaInteprete[4]== 1):
        pantalla.blit(naranja2,(128,0))
        if(listaInteprete[7]== 1):
            pantalla.blit(active,(128,0))
    pygame.display.update()