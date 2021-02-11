import smtplib, ssl

port = 465  # For SSL
receiver_email = input("The Receiver Adress: ")

# Create a secure SSL context
context = ssl.create_default_context()

#MORSE MACHINE CODE STARTS HERE
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
        "!":("-.-.--"),

        " ":("     ")
        }

password = YOUR_PASSWORD
yourEmail = YOUR_EMAIL_ADRESS

def translate(word): 
    return [Dict[char] for char in word] 

text = input("Hello! What do you want to convert and send? " ).lower()
message = str(translate(text))
#END OF THE MORSE MACHINE CODE

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    print("About to login")
    server.login(yourEmail, password)
    print("Logged in")
    server.sendmail(yourEmail, receiver_email , message)
    print(f"Sending {message}")

print("Done!") 
