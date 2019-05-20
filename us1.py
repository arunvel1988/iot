#A udp server that sends msg to client
import socket
import time
#take server name and port no
host = "localhost"
port = 5000
# create a socket at server side to use UDP protocol
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Lets the server wait for 5 sec

time.sleep(5)
#sends msg to the client after encoding into binary string
s.sendto(b"hello client, how are you", (host,port))
msg = "Bye"
s.sendto(msg.encode(), (host,port))
#disconnet the server
s.close()

