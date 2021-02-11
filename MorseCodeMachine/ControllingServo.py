# servo control 15.12.2016
 
# 1) user set servo position in python
# 2) position is sent to arduino
# 3) arduino moves servo to position
# 4) arduino send confirmation message back to python
# 5) message is printed in python console

import serial, time                                     # import serial library
arduino = serial.Serial('COM3', 9600)                   # create serial object named arduino

Dict = {
        #LOWER
        "a":(".-"),
        "b":("-..."),
        "c":("-.-."),
        "d":("-.."),
        "e":("."),
        "f":("..-."),
        "g":("--."),
        "h":("...."),
        "i":(".."),
        "j":(".---"),
        "k":("-.-"),
        "l":(".-.."),
        "m":("--"),
        "n":("-."),
        "ñ":("--.--"),
        "o":("---"),
        "p":(".--."),
        "q":("--.-"),
        "r":(".-."),
        "s":("..."),
        "t":("-"),
        "u":("..-"),
        "v":("...-"),
        "w":(".--"),
        "x":("-..-"),
        "y":("-.--"),
        "z":("--.."),

        #UPPER
        "A":(".-"),
        "B":("-..."),
        "C":("-.-."),
        "D":("-.."),
        "E":("."),
        "F":("..-."),
        "G":("--."),
        "H":("...."),
        "I":(".."),
        "J":(".---"),
        "K":("-.-"),
        "L":(".-.."),
        "M":("--"),
        "N":("-."),
        "Ñ":("--.--"),
        "O":("---"),
        "P":(".--."),
        "Q":("--.-"),
        "R":(".-."),
        "S":("..."),
        "T":("-"),
        "U":("..-"),
        "V":("...-"),
        "W":(".--"),
        "X":("-..-"),
        "Y":("-.--"),
        "Z":("--.."),

        #NUMBERS
        "0":("-----"),
        "1":(".----"),
        "2":("..---"),
        "3":("...--"),
        "4":("....-"),
        "5":("....."),
        "6":("-...."),
        "7":("--..."),
        "8":("---.."),
        "9":("----."),

        #PUNCTUATION
        
        ".":(".-.-.-"),
        ",":("--..--"),
        "?":("..--.."),
        ";":("-.-.-."),
        ":":("---..."),
        "/":("-..-."),
        "-":("-....-"),
        "'":(".----."),
        '"':(".-..-."),
        "_":("..--.-"),
        "(":("-.--."),
        ")":("-.--.-"),
        "=":("-...-"),
        "+":(".-.-."),
        "*":("-..-"),
        "@":(".--.-."),





        " ":("     ")
        }

def split(word): 
    return [Dict[char] for char in word]                     #for every characher in "word", search the translation in the Dict and return it 

text = split(input("Hello! What do you want to translate?" ).lower())   #we store the list (dots and dashes) in the variable "text"

print(text)                                                         #print text for debugging purposes

command = "0"                                                       #we declare command so the program knows the variable                    

maxNumEl = len(text)
numEl = 0


print("Entering LOOP")
while numEl != maxNumEl:                                            # create loop
    element = text[numEl]
    print(element + ' :')  
    for char in element:

        if "." in char:
            arduino.write(b'90')                                    # write position to serial port
            time.sleep(1)
            arduino.write(b'0')
            time.sleep(1)                                                                               
            print(".")
        
        elif "-" in char:
            arduino.write(b'90')                                               
            time.sleep(2)
            arduino.write(b'0')                                            
            time.sleep(1)
            print("-")
            
        else:
            pass

    numEl += 1
    print(",")