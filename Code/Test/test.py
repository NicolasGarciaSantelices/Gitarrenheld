
import serial
import pygame

arduino = serial.Serial(port='/dev/cu.usbmodem142301', baudrate=9600)
listaInteprete = [0,0,0,0,0,0,0,0]
pygame.init()
def starPowerdef():
    pantalla.blit(starPower,(0,0))
    pantalla.blit(starPower,(100,0))
    pantalla.blit(starPower,(200,0))
    pantalla.blit(starPower,(300,0))
    pantalla.blit(starPower,(400,0))
   
    if(listaInteprete[0]== 1):
        pantalla.blit(starPower2,(0,0))
        if(listaInteprete[7]== 1):
            pantalla.blit(starPower3,(0,0))
    if(listaInteprete[1]== 1):
        pantalla.blit(starPower2,(100,0))
        if(listaInteprete[7]== 1):
            pantalla.blit(starPower3,(100,0))
    if(listaInteprete[2]== 1):
        pantalla.blit(starPower2,(200,0))
        if(listaInteprete[7]== 1):
            pantalla.blit(starPower3,(200,0))
    if(listaInteprete[3]== 1):
        pantalla.blit(starPower2,(300,0))
        if(listaInteprete[7]== 1):
            pantalla.blit(starPower3,(300,0))
    if(listaInteprete[4]== 1):
        pantalla.blit(starPower2,(400,0))
        if(listaInteprete[7]== 1):
            pantalla.blit(starPower3,(400,0))    

#definir tamaño ventana:
pantalla = pygame.display.set_mode((500,100))
pygame.display.set_caption('Gitarren Held')
verde1 = pygame.image.load("Img/Sprites/Botonera/verde1.png")
verde2 = pygame.image.load("Img/Sprites/Botonera/Verde2.png")
azul1 = pygame.image.load("Img/Sprites/Botonera/Azul1.png")
azul2 = pygame.image.load("Img/Sprites/Botonera/Azul2.png")
naranja1 = pygame.image.load("Img/Sprites/Botonera/Naranjo1.png")
naranja2 = pygame.image.load("Img/Sprites/Botonera/Naranja2.png")
amarillo1 = pygame.image.load("Img/Sprites/Botonera/Amarillo1.png")
amarillo2 = pygame.image.load("Img/Sprites/Botonera/Amarillo2.png")
rojo1 = pygame.image.load("Img/Sprites/Botonera/Rojo.png")
rojo2 = pygame.image.load("Img/Sprites/Botonera/Rojo2.png")
active = pygame.image.load("Img/Sprites/Botonera/ON.png")
starPower = pygame.image.load("Img/Sprites/Botonera/starpower.png")
starPower2 = pygame.image.load("Img/Sprites/Botonera/starpower2.png")
starPower3 = pygame.image.load("Img/Sprites/Botonera/starpower3.png")
#Escalamos la imagen en Pygame
verde1 = pygame.transform.scale(verde1,(100,100))
verde2 = pygame.transform.scale(verde2,(100,100))
azul1 = pygame.transform.scale(azul1,(100,100))
azul2 = pygame.transform.scale(azul2,(100,100))
naranja1 = pygame.transform.scale(naranja1,(100,100))
naranja2 = pygame.transform.scale(naranja2,(100,100))
amarillo1 = pygame.transform.scale(amarillo1,(100,100))
amarillo2 = pygame.transform.scale(amarillo2,(100,100))
rojo1 = pygame.transform.scale(rojo1,(100,100))
rojo2 = pygame.transform.scale(rojo2,(100,100))
active = pygame.transform.scale(active,(100,100))
starPower = pygame.transform.scale(starPower,(100,100))
starPower2 = pygame.transform.scale(starPower2,(100,100))
starPower3 = pygame.transform.scale(starPower3,(100,100))
white = [0, 0, 0]
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
    pantalla.blit(rojo1,(100,0))
    pantalla.blit(amarillo1,(200,0))
    pantalla.blit(azul1,(300,0))
    pantalla.blit(naranja1,(400,0))
    #cambios de estados:
    if(listaInteprete[5]==0):
        if(listaInteprete[0]== 1):
            pantalla.blit(verde2,(0,0))
            if(listaInteprete[7]== 1):
                pantalla.blit(active,(0,0))
        if(listaInteprete[1]== 1):
            pantalla.blit(rojo2,(100,0))
            if(listaInteprete[7]== 1):
                pantalla.blit(active,(100,0))
        if(listaInteprete[2]== 1):
            pantalla.blit(amarillo2,(200,0))
            if(listaInteprete[7]== 1):
                pantalla.blit(active,(200,0))
        if(listaInteprete[3]== 1):
            pantalla.blit(azul2,(300,0))
            if(listaInteprete[7]== 1):
                pantalla.blit(active,(300,0))
        if(listaInteprete[4]== 1):
            pantalla.blit(naranja2,(400,0))
            if(listaInteprete[7]== 1):
                pantalla.blit(active,(400,0))
    else:
        starPowerdef()
    pygame.display.update()