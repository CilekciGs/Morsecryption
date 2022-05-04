#!/usr/bin/env python

# import required libraries
import socket
from multiprocessing import Process

TCP_IP = '127.0.0.1' #input("ip: ")
TCP_PORT = int(input("port: "))	
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

def send():
	cl = str(input("Type:")).lower()
	# - = 0 . = 1 1010 = " "
	encoding = cl.replace(" ", "1010 ")
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
	encryptedMessage = encoding
	cl = str(encryptedMessage)
	s.send(cl.encode(encoding='utf_8', errors='strict'))

def recieve():
	sv = s.recv(BUFFER_SIZE).decode(encoding='utf_8', errors='strict')
	decoding = sv.replace("1010 ", " ")
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

	decryptedMessage = decoding
	print("Recieved: ", decryptedMessage)

while True:
	if __name__ == '__main__':
		p1 = Process(target=send)
		p2 = Process(target=recieve)
		p1.start()
		p2.start()
		p1.join()
		p2.join()