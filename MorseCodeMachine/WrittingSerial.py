import serial, time
arduino = serial.Serial("COM3", 9600)   #The port where you plug your Arduino
time.sleep(2)
arduino.write(b'9')
arduino.close()
