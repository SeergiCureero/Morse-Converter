import pyfirmata
import time

board = pyfirmata.Arduino('COM3')
d1 = board.get_pin('d:2:o')      
d2 = board.get_pin('d:3:o')     
d3 = board.get_pin('d:4:o')     
d4 = board.get_pin('d:5:o')      
d5 = board.get_pin('d:6:o')    
d6 = board.get_pin('d:7:o')      
d7 = board.get_pin('d:8:o')     
d8 = board.get_pin('d:9:o')      
d9 = board.get_pin('d:10:o')
d10 = board.get_pin('d:11:o')
d11 = board.get_pin('d:12:o')
d12 = board.get_pin('d:13:o')


it = pyfirmata.util.Iterator(board)
it.start()

class Num:
    def __init__(self):
        d1.write(0)
        d2.write(0)
        d3.write(0)
        d4.write(1)
        d5.write(0)
        d6.write(0)
        d7.write(0)
        d8.write(0)
        d9.write(0)
        d10.write(0)
        d11.write(0)
        d12.write(0)

    
    def intermitentNum(self):
        d1.write(1)
        time.sleep(1)
        d1.write(0)
        time.sleep(1)
        print("1")

        d2.write(1)
        time.sleep(1)
        d2.write(0)
        time.sleep(1)
        print("2")

        d3.write(1)
        time.sleep(1)
        d3.write(0)
        time.sleep(1)
        print("3")
        
        d4.write(1)
        time.sleep(1)
        d4.write(0)
        time.sleep(1)
        print("4")
        
        d5.write(1)
        time.sleep(1)
        d5.write(0)
        time.sleep(1)
        print("5")
        
        d6.write(1)
        time.sleep(1)
        d6.write(0)
        time.sleep(1)
        print("6")
        
        d7.write(1)
        time.sleep(1)
        d7.write(0)
        time.sleep(1)
        print("7")
        
        d8.write(1)
        time.sleep(1)
        d8.write(0)
        time.sleep(1)
        print("8")
        
        d9.write(1)
        time.sleep(1)
        d9.write(0)
        time.sleep(1)
        print("9")

        d10.write(1)
        time.sleep(1)
        d10.write(0)
        time.sleep(1)
        print("10")

        d11.write(1)
        time.sleep(1)
        d11.write(0)
        time.sleep(1)
        print("11")

        d12.write(1)
        time.sleep(1)
        d12.write(0)
        time.sleep(1)
        print("12")



while True:
    Num().intermitentNum()
