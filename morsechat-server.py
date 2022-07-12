import sys
import socket
from threading import Thread

# initialize list/set of all connected client's sockets
client_sockets = set()
# create a TCP socket
s = socket.socket()
# make the port as reusable port
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    SERVER_HOST, separator, SERVER_PORT = sys.argv[1].rpartition(':')
    s.bind((SERVER_HOST, int(SERVER_PORT)))
except:
    SERVER_HOST = input("ip: ")
    SERVER_PORT = int(input("port:"))
    s.bind((SERVER_HOST, SERVER_PORT))

# listen for upcoming connections
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")


def listen_for_client(cs):

    while True:
        try:
            # keep listening for a message from `cs` socket
            msg = cs.recv(1024)
        except Exception as e:
            # client no longer connected
            # remove it from the set
            print(f"[!] Error: {e}")
            client_sockets.remove(cs)

        for client_socket in client_sockets:
            # and send the message
            client_socket.send(msg)

while True:
    # we keep listening for new connections all the time
    client_socket, client_address = s.accept()
    print(f"[+] {client_address} connected.")
    # add the new connected client to connected sockets
    client_sockets.add(client_socket)
    # start a new thread that listens for each client's messages
    t = Thread(target=listen_for_client, args=(client_socket,))
    # make the thread daemon so it ends whenever the main thread ends
    t.daemon = True
    # start the thread
    t.start()

# close client sockets
for cs in client_sockets:
    cs.close()
# close server socket
s.close()
