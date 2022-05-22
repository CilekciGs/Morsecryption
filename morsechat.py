import socket
from threading import Thread


# server's IP address
# if the server is not on this machine,
# put the private (network) IP address (e.g 192.168.1.2)
SERVER_HOST = input("ip: ")
SERVER_PORT = int(input("port:"))  # server's port

global encryptedMessage
encryptedMessage = "0101 000 01 01 1 0101 0 1 011 "

# initialize TCP socket
s = socket.socket()
print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
# connect to the server
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected.")
s.send("0101 000 01 01 1 0101 0 1 011 ".encode())


def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        if message == encryptedMessage:
            pass
        else:

            decoding = message.replace("100001 ", "'")
            decoding = decoding.replace("100101 ", "@")
            decoding = decoding.replace("010010 ", ")")
            decoding = decoding.replace("000111 ", ":")
            decoding = decoding.replace("001100 ", ",")
            decoding = decoding.replace("10100 ", "!")
            decoding = decoding.replace("101010 ", ".")
            decoding = decoding.replace("011110 ", "-")
            decoding = decoding.replace("101101 ", '"')
            decoding = decoding.replace("110011 ", "?")
            decoding = decoding.replace("10111 ", "&")
            decoding = decoding.replace("01001 ", "(")
            decoding = decoding.replace("10101 ", "+")
            decoding = decoding.replace("11000 ", "2")
            decoding = decoding.replace("11100 ", "3")
            decoding = decoding.replace("11110 ", "4")
            decoding = decoding.replace("11111 ", "5")
            decoding = decoding.replace("01111 ", "6")
            decoding = decoding.replace("00111 ", "7")
            decoding = decoding.replace("00011 ", "8")
            decoding = decoding.replace("01101 ", "9")
            decoding = decoding.replace("01110 ", "=")
            decoding = decoding.replace("01011 ", " ")
            decoding = decoding.replace("1011 ", "l")
            decoding = decoding.replace("1110 ", "v")
            decoding = decoding.replace("0110 ", "x")
            decoding = decoding.replace("0100 ", "y")
            decoding = decoding.replace("0011 ", "z")
            decoding = decoding.replace("0111 ", "b")
            decoding = decoding.replace("0101 ", "c")
            decoding = decoding.replace("1101 ", "f")
            decoding = decoding.replace("1111 ", "h")
            decoding = decoding.replace("1001 ", "p")
            decoding = decoding.replace("0010 ", "q")
            decoding = decoding.replace("1000 ", "j")
            decoding = decoding.replace("011 ", "d")
            decoding = decoding.replace("001 ", "g")
            decoding = decoding.replace("010 ", "k")
            decoding = decoding.replace("100 ", "w")
            decoding = decoding.replace("000 ", "o")
            decoding = decoding.replace("101 ", "r")
            decoding = decoding.replace("111 ", "s")
            decoding = decoding.replace("110 ", "u")
            decoding = decoding.replace("10 ", "a")
            decoding = decoding.replace("11 ", "i")
            decoding = decoding.replace("00 ", "m")
            decoding = decoding.replace("01 ", "n")
            decoding = decoding.replace("1 ", "e")
            decoding = decoding.replace("0 ", "t")


            decryptedmessage = decoding
            print("Received: " + decryptedmessage)


# make a thread that listens for messages to this client & print them
t = Thread(target=listen_for_messages)
# make the thread daemon, so it ends whenever the main thread ends
t.daemon = True
# start the thread
t.start()

while True:
    # input message we want to send to the server
    to_send = input().lower()
    # a way to exit the program
    if to_send == 'q':
        s.send("011 11 111 0101 000 01 01 1 0101 0 1 011 ".encode())
        break
    else:

        encoding = to_send.replace(" ", "01011 ")

        encoding = encoding.replace("2", "11000 ")
        encoding = encoding.replace("3", "11100 ")
        encoding = encoding.replace("4", "11110 ")
        encoding = encoding.replace("5", "11111 ")
        encoding = encoding.replace("6", "01111 ")
        encoding = encoding.replace("7", "00111 ")
        encoding = encoding.replace("8", "00011 ")
        encoding = encoding.replace("9", "01101 ")

        encoding = encoding.replace("a", "10 ")
        encoding = encoding.replace("b", "0111 ")
        encoding = encoding.replace("c", "0101 ")
        encoding = encoding.replace("d", "011 ")
        encoding = encoding.replace("e", "1 ")
        encoding = encoding.replace("f", "1101 ")
        encoding = encoding.replace("g", "001 ")
        encoding = encoding.replace("h", "1111 ")
        encoding = encoding.replace("i", "11 ")
        encoding = encoding.replace("j", "1000 ")
        encoding = encoding.replace("k", "010 ")
        encoding = encoding.replace("l", "1011 ")
        encoding = encoding.replace("m", "00 ")
        encoding = encoding.replace("n", "01 ")
        encoding = encoding.replace("o", "000 ")
        encoding = encoding.replace("p", "1001 ")
        encoding = encoding.replace("q", "0010 ")
        encoding = encoding.replace("r", "101 ")
        encoding = encoding.replace("s", "111 ")
        encoding = encoding.replace("t", "0 ")
        encoding = encoding.replace("u", "110 ")
        encoding = encoding.replace("v", "1110 ")
        encoding = encoding.replace("w", "100 ")
        encoding = encoding.replace("x", "0110 ")
        encoding = encoding.replace("y", "0100 ")
        encoding = encoding.replace("z", "0011 ")

        encoding = encoding.replace("&", "10111 ")
        encoding = encoding.replace("'", "100001 ")
        encoding = encoding.replace("@", "100101 ")
        encoding = encoding.replace(")", "010010 ")
        encoding = encoding.replace("(", "01001 ")
        encoding = encoding.replace(":", "000111 ")
        encoding = encoding.replace(",", "001100 ")
        encoding = encoding.replace("=", "01110 ")
        encoding = encoding.replace("!", "10100 ")
        encoding = encoding.replace(".", "101010 ")
        encoding = encoding.replace("-", "011110 ")
        encoding = encoding.replace("+", "10101 ")
        encoding = encoding.replace('"', "101101 ")
        encoding = encoding.replace("?", "110011 ")

        encryptedMessage = encoding
        s.send(encryptedMessage.encode())

# close the socket
s.close()
