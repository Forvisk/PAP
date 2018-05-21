import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock

import random
import socket

from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

# selecionando um voo, pegar a lista de todas as paradas do voo
# aqui se conecta com o servidor e pega os dados
def getListaParadas( voo):
	"""Busca do servidor a lista de paradas de um voo, retornando uma lista com os dados das paradas"""
	HOST, PORT = "localhost", 9999
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	destino = (HOST, PORT)
	client.connect( destino)
	client.send( bytes( 'lp', 'utf8'))
	client.recv(1024).decode('utf8')
	client.send( bytes( voo, 'utf8'))
	print( voo)
	listaParadas = []
	while True:
		msg = client.recv(1024).decode("utf8")
		if not msg: break
		listaParadas.append( msg.split())
		#print( msg)
	client.close()
	print( listaParadas)
	return listaParadas

def listaParadastoStr( parada):
	iLat = int( parada[0])
	iLong = int( parada[1])
	iCargaMov = int( parada[2])
	if( iLat < 0):
		sLat = str( iLat * -1) + '° S'
	else:
		sLat = str( iLat) + '° N'
	if( iLong < 0):
		sLong = str( iLong * -1) + '° W'
	else:
		sLong = str( iLong) + '° E'
	sCord = sLat + ' -- ' + sLong
	if( iCargaMov < 0):
		sCargaMov = 'Descarrega ' + str( iCargaMov * -1) + 'kg'
	elif( iCargaMov == 0):
		sCargaMov = 'Sem movimento'
	else:
		sCargaMov = 'Carrega ' + str( iCargaMov) + 'kg'
	sCargaFinal = parada[3] + 'kg'

	return [ sCord, sCargaMov, sCargaFinal]
	
# aqui se conecta com o servidor e pega os dados
def getListaVoo():
	listaVoo = []	
	HOST, PORT = "localhost", 9999
	destino = (HOST, PORT)
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect( destino)
	client.send( bytes( 'lv', 'utf8'))
	while True:
		msg = client.recv(1024).decode("utf8")
		if not msg: break
		listaVoo.append( msg.split('--'))
	client.close()
	return listaVoo

class TelaParadasVoo( Screen):
	scrollP = ObjectProperty( None)
	nomeVoo = StringProperty( '')
	modeloAviao = StringProperty( '')

	def __init__( self, voo, **kwargs):
		super( TelaParadasVoo, self).__init__( **kwargs)
		self.voo = voo
		self.nomeVoo = voo[1]
		self.modeloAviao =voo[3]
		Clock.schedule_once(self.criarscrollview)

	def criarscrollview( self, dt):
		listaParadas = getListaParadas( self.voo[0])

		lista = GridLayout( cols=1, padding=10, spacing=5, size_hint_y = None, width=400)
		lista.bind( minimum_height=lista.setter('height'))
		for i in range( len(listaParadas)):
			sParadas = listaParadastoStr( listaParadas[i])
			stringParada = sParadas[0] + '\t' + sParadas[1] + '\t' + sParadas[2]
			lbStr = LabelListaParadas( text = stringParada)
			lista.add_widget( lbStr)

		scrollP = ScrollView( size_hint=(1, None),size=(Window.width * 0.9, Window.height * 0.8), pos_hint={'center_x': .5, 'center_y': .4}, do_scroll_x=False)
		scrollP.add_widget( lista)
		self.add_widget( scrollP)

class LabelListaParadas( Button):
	def __init__( self, **kwargs):
		super( LabelListaParadas, self).__init__( **kwargs)
		self.font_size = 15
		self.size=( Window.width* 0.9, 40)
		self.size_hint=(1, None)
		self.text = self.text.replace('\t', '    ')

class TelaSelectVoo( Screen):
	scrollV = ObjectProperty( None)
	def __init__( self, **kwargs):
		super( TelaSelectVoo, self).__init__( **kwargs)
		Clock.schedule_once(self.criarscrollview)

	def criarscrollview( self, dt):
		listaVoo = getListaVoo()
		lista = GridLayout(cols=1, padding=10, spacing=10, size_hint_y = None, width=400)
		lista.bind(minimum_height=lista.setter('height'))
		for i in range( len(listaVoo)):
			btn = BotaoListaVoo( )
			btn.criaBotaoLVoo( listaVoo[i])
			lista.add_widget(btn)
		scrollV = ScrollView( size_hint=(1, None), size=(Window.width * 0.9, Window.height * 0.8), pos_hint={'center_x': .5, 'center_y': .4}, do_scroll_x=False)
		scrollV.add_widget( lista)
		self.add_widget(scrollV)

class BotaoListaVoo( Button):
	def __init__( self, **kwargs):
		super( BotaoListaVoo, self).__init__( **kwargs)
		self.size=(480, 40)
		self.size_hint=(1, None)
		self.background_color = [ 0.5, 0.5 , 0.5, 3]

	def criaBotaoLVoo( self, voo):
		self.text = voo[1]
		self.voo = voo

class TelaInicial( Screen):
	pass

class TelaCarregando(Screen):
	pass

class TelaMapa( Screen):
	pass

class Manager( ScreenManager):
	def __init__(self, **kwargs):
		super(Manager, self).__init__(**kwargs)
		self.listaTela = [ TelaInicial(), TelaCarregando()]
		self.add_widget( self.listaTela[0])
		self.add_widget( self.listaTela[1])

	def irTelaSelecVoo( self):
		self.current = nomeTelaCarregando
		self.listaTela.append( TelaSelectVoo( name = nomeTelaSelecVoo))
		self.add_widget( self.listaTela[ 2])
		self.current = nomeTelaSelecVoo

	def voltarTelaInic( self):
		self.current = nomeTelaInicial
		self.remove_widget( self.listaTela[2])
		del self.listaTela[2]

	def  recarregaTelaSelecVoo( self):
		self.current = nomeTelaCarregando
		self.remove_widget( self.listaTela[2])
		del self.listaTela[2]
		self.irTelaSelecVoo()

	def irTelaParadaVoo( self, voo):
		self.current = nomeTelaCarregando
		self.remove_widget( self.listaTela[2])
		del self.listaTela[2]
		self.listaTela.append( TelaParadasVoo( voo, name = nomeTelaParadaVoo))
		self.add_widget( self.listaTela[2])
		self.current = nomeTelaParadaVoo
	
	def sairTelaParadaVoo( self):
		self.current = nomeTelaCarregando
		self.remove_widget( self.listaTela[2])
		del self.listaTela[2]
		self.irTelaSelecVoo()

class InterfaceV3App( App):
	"""InterfaceV2App"""
	def build( self):
		pass

"""Definindo os nomes das telas"""
nomeTelaSelecVoo = 'telaselecvoo'
nomeTelaParadaVoo = 'telaparada'
nomeTelaInicial = 'telainic'
nomeTelaCarregando = 'telaloading'

if __name__ == '__main__':
	InterfaceV3App().run()
