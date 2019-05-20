import socket
host = "localhost"
port = 5000
#create a socket at server side using TCP/IP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind the socket with server and port number
s.bind((host, port))
#allow max 5 connections to socket
s.listen(5)
# wait till client accepts connection
c, addr = s.accept()
print("connection from: ", str(addr))
#sends msg to the client after encoding into binary
c.send(b"hello client, how are you")
msg = "Bye!"
c.send(msg.encode())
c.close()
#disconnect the server
