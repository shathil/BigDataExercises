from thread import *

import sys
import random
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, True)
server_address = ('localhost', int(sys.argv[1]))
sock.bind(server_address)
sock.listen(10000)

def clientthread(conn):
    #Sending message to connected client     
    #infinite loop so that function do not terminate and thread do not end.
    try:
        while True:          
            conn.sendall((','.join(([str(random.randint(0,1000000)) for _ in range(100)]))+"\n").encode('utf-8'))
    finally:
        #came out of loop
        conn.close()
 
#now keep talking with the client
while 1:
    conn, addr = sock.accept()     
    start_new_thread(clientthread ,(conn,)) 
sock.close()
