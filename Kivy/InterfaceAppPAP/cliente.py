import socket

HOST, PORT = "localhost", 9999
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destino = (HOST, PORT)
client.connect( destino)

while True:
	msg = client.recv(1024).decode("utf8")
	if not msg: break
	print( msg)

client.close()