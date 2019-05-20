import socket
host = "localhost"
port = 5000
#create a socket at client side using TCP/IP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect with server and port number
s.connect((host, port))
#  receive msg string from server, at a time 1024 Byte
msg = s.recv(1024)

# repeat as long as message strings are not empty
while msg:
	print("received: " + msg.decode())
	msg = s.recv(1024)
# disconnect the client
s.close()
