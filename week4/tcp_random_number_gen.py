import sys
import random
import time
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, True)
server_address = ('localhost', int(sys.argv[1]))
sock.bind(server_address)
sock.listen(10000)

while True:
    connection, client_address = sock.accept()
    try:
        connection.sendall((','.join(([str(random.randint(0,1000000)) for _ in range(100)]))+"\n").encode('utf-8'))
    finally:
        connection.close()
