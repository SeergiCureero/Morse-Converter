import serial, time
arduino = serial.Serial('COM3', 9600)   #'COM3' is the port where I plugged my arduino. Make sure you change it to the port where you are plugging your arduino
time.sleep(2)
rawString = arduino.readline()
print(rawString)
arduino.close()
