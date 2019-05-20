import socket
host = "localhost"
port = 5000
# create a client side socket that uses udp protocol
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# connect it to server
s.bind((host, port))
# receive msg string from server , at a time 1024 B
msg,addr=s.recvfrom(1024)

try:
# Let the socket block after 5 secs if the server disconnects
	s.settimeout(5)
	while msg:
		print("received:" +  msg.decode())
		msg , addr = s.recvfrom(1024)

except socket.timeout:
	print("time is over and hence terminating...")
#disconnect
s.close()

	


