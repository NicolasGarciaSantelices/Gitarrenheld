import serial
arduino = serial.Serial(port='/dev/cu.usbmodem141401', baudrate=9600)
while True:
    line = arduino.readline().decode('utf-8')
    print(line)
    print("hola")