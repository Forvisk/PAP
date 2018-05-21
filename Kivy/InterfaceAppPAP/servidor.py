import socket

HOST, PORT = "localhost", 9999

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((HOST,PORT))
serv.listen(1)
print('tst')
while True:
	conect, cli = serv.accept()
	print ('Conectado por:', cli)
	arq = open('voos.txt', 'r')

	for i in arq.readlines():
		conect.sendto( bytes( i, "utf8"), cli)
	arq.close()
	conect.close()

serv.close()
