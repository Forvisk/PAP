import socket

HOST, PORT = "localhost", 9999

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((HOST,PORT))
serv.listen(1)
print('Iniciando servidor')
listaVoo = []

while True:
	conect, cli = serv.accept()
	print('Conectado por:', cli)
	pedido = conect.recv(1024).decode("utf8")

	if pedido == 'lv':
		arq = open('arquivos/listaVoo.txt', 'r')
		k = 0
		for i in arq.readlines():
			k += 1
			if k >= len( listaVoo):
				print( i)
				listaVoo.append( i.split('--'))
			conect.sendto( bytes( i, "utf8"), cli)
			arq.close()
		#print(listaVoo)
	elif pedido == 'lp':
		conect.sendto( bytes( 'k', "utf8"), cli)
		sIndice = conect.recv(1024).decode("utf8")
		indice = int( sIndice) -1
		if( len( listaVoo) > indice):
			arq = open('arquivos/' + listaVoo[indice][1] + '.txt', 'r')
			k = 0
			for i in arq.readlines():
				#print( i)
				conect.sendto( bytes( i, "utf8"), cli)
				arq.close()
	conect.close()

serv.close()
