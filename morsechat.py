import zmq
import time
import base64
import sys
from threading import Thread

global encryptedMessage
global stop
stop = 0
encryptedMessage = ""
context = zmq.Context()


try:
    SERVER_HOST, separator, SERVER_PORT = sys.argv[1].rpartition(':')
## add connect code
except:
    SERVER_HOST = input("ip: ")
    SERVER_PORT = int(input("port:"))
## add connectcode

print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")

print("[+] Connected.")

def coding(input, todo):
    
    if todo == "decode":
            input = input.replace("100001 ", "'")
            input = input.replace("100101 ", "@")
            input = input.replace("010010 ", ")")
            input = input.replace("000111 ", ":")
            input = input.replace("001100 ", ",")
            input = input.replace("10100 ", "!")
            input = input.replace("101010 ", ".")
            input = input.replace("011110 ", "-")
            input = input.replace("101101 ", '"')
            input = input.replace("110011 ", "?")
            input = input.replace("10111 ", "&")
            input = input.replace("01001 ", "(")
            input = input.replace("10101 ", "+")
            input = input.replace("11000 ", "2")
            input = input.replace("11100 ", "3")
            input = input.replace("11110 ", "4")
            input = input.replace("11111 ", "5")
            input = input.replace("01111 ", "6")
            input = input.replace("00111 ", "7")
            input = input.replace("00011 ", "8")
            input = input.replace("01101 ", "9")
            input = input.replace("01110 ", "=")
            input = input.replace("11001 ", "e") ## NOT MORSE ACCURATE
            input = input.replace("00101 ", "t") ## NOT MORSE ACCURATE
            input = input.replace("01011 ", " ")
            input = input.replace("1011 ", "l")
            input = input.replace("1110 ", "v")
            input = input.replace("0110 ", "x")
            input = input.replace("0100 ", "y")
            input = input.replace("0011 ", "z")
            input = input.replace("0111 ", "b")
            input = input.replace("0101 ", "c")
            input = input.replace("1101 ", "f")
            input = input.replace("1111 ", "h")
            input = input.replace("1001 ", "p")
            input = input.replace("0010 ", "q")
            input = input.replace("1000 ", "j")
            input = input.replace("011 ", "d")
            input = input.replace("001 ", "g")
            input = input.replace("010 ", "k")
            input = input.replace("100 ", "w")
            input = input.replace("000 ", "o")
            input = input.replace("101 ", "r")
            input = input.replace("111 ", "s")
            input = input.replace("110 ", "u")
            input = input.replace("10 ", "a")
            input = input.replace("11 ", "i")
            input = input.replace("00 ", "m")
            input = input.replace("01 ", "n")
            return(input)
            input = "" ## over-engineered
    else:
        input = input.replace(" ", "01011 ")
        input = input.replace("2", "11000 ")
        input = input.replace("3", "11100 ")
        input = input.replace("4", "11110 ")
        input = input.replace("5", "11111 ")
        input = input.replace("6", "01111 ")
        input = input.replace("7", "00111 ")
        input = input.replace("8", "00011 ")
        input = input.replace("9", "01101 ")

        input = input.replace("a", "10 ")
        input = input.replace("b", "0111 ")
        input = input.replace("c", "0101 ")
        input = input.replace("d", "011 ")
        input = input.replace("e", "11001 ") ## NOT MORSE ACCURATE
        input = input.replace("f", "1101 ")
        input = input.replace("g", "001 ")
        input = input.replace("h", "1111 ")
        input = input.replace("i", "11 ")
        input = input.replace("j", "1000 ")
        input = input.replace("k", "010 ")
        input = input.replace("l", "1011 ")
        input = input.replace("m", "00 ")
        input = input.replace("n", "01 ")
        input = input.replace("o", "000 ")
        input = input.replace("p", "1001 ")
        input = input.replace("q", "0010 ")
        input = input.replace("r", "101 ")
        input = input.replace("s", "111 ")
        input = input.replace("t", "00101 ") ## NOT MORSE ACCURATE
        input = input.replace("u", "110 ")
        input = input.replace("v", "1110 ")
        input = input.replace("w", "100 ")
        input = input.replace("x", "0110 ")
        input = input.replace("y", "0100 ")
        input = input.replace("z", "0011 ")

        input = input.replace("&", "10111 ")
        input = input.replace("'", "100001 ")
        input = input.replace("@", "100101 ")
        input = input.replace(")", "010010 ")
        input = input.replace("(", "01001 ")
        input = input.replace(":", "000111 ")
        input = input.replace(",", "001100 ")
        input = input.replace("=", "01110 ")
        input = input.replace("!", "10100 ")
        input = input.replace(".", "101010 ")
        input = input.replace("-", "011110 ")
        input = input.replace("+", "10101 ")
        input = input.replace('"', "101101 ")
        input = input.replace("?", "110011 ")
        return(input)
        input = "" ## over-engineered

def listen_for_messages():
    while stop == 0:
        message = "" ##add recieve code
        if message == encryptedMessage:
            pass
        else:
            print("Recieved: "+ coding(base64.b32decode(message).decode('utf-8'), "decode"))

t = Thread(target=listen_for_messages)
t.daemon = True
t.start()

while True:
    to_send = input().lower()
    if to_send == 'q':
        stop = 1
        break
    else:
        encryptedMessage = coding(to_send, "encode")
##add send code        s.send(base64.b32encode(bytearray(encryptedMessage, 'ascii')))

# add close code

sys.exit(0)
