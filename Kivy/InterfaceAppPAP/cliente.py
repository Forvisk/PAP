import socket

HOST, PORT = "localhost", 9999
destino = (HOST, PORT)

print('test lista voo')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect( destino)
client.send(bytes('lv', "utf8"))
while True:
	msg = client.recv(1024).decode("utf8")
	if not msg: break
	print( msg)
client.close()

print('test paradas 1')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect( destino)
client.send( bytes( 'lp', 'utf8'))
client.recv(1024).decode('utf8')
client.send( bytes( '1', 'utf8'))
while True:
	msg = client.recv(1024).decode("utf8")
	if not msg: break
	print( msg)

print('test paradas 2')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect( destino)
client.send( bytes( 'lp', 'utf8'))
client.recv(1024).decode('utf8')
client.send( bytes( '4', 'utf8'))
while True:
	msg = client.recv(1024).decode("utf8")
	if not msg: break
	print( msg)

client.close()