import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock

import random

from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.scatter import Scatter

# selecionando um voo, pegar a lista de todas as paradas do voo
# aqui se conecta com o servidor e pega os dados
def getListaParadas( voo, n):
	"""Busca do servidor a lista de paradas de um voo, retornando uma lista com os dados das paradas"""
	listaParadas = []
	peso = 50
	for i in range(1,n):
		rlat = round( random.randint( -90, 90) + random.random(), 4)
		rlong = round( random.randint( -180, 180) + random.random(), 4)
		rMovCarga = random.randint( -50, 50)
		if peso + rMovCarga < 0:
			rMovCarga = 15
		peso += rMovCarga
		listaParadas.append( [rlat, rlong, rMovCarga, peso])

	return listaParadas

def listaParadastoStr( parada):
	
	if( parada[0] < 0):
		sLat = str( parada[0] * -1) + '° S'
	else:
		sLat = str( parada[0]) + '° N'
	if( parada[1] < 0):
		sLong = str( parada[1] * -1) + '° W'
	else:
		sLong = str( parada[1]) + '° E'
	sCord = sLat + ' -- ' + sLong
	if( parada[2] < 0):
		sCargaMov = 'Descarrega ' + str( parada[2] * -1) + 'kg'
	elif( parada[2] == 0):
		sCargaMov = 'Sem movimento'
	else:
		sCargaMov = 'Carrega ' + str( parada[2]) + 'kg'
	sCargaFinal = str( parada[3]) + 'kg'

	return [ sCord, sCargaMov, sCargaFinal]
	
# aqui se conecta com o servidor e pega os dados
def getListaVoo( n):
	listaVoo = []
	for i in range( n):
		listaVoo.append( ['Voo '+str( i * ( 3**3) + 10), (i+10)**2])
	return listaVoo

class TelaParadasVoo( Screen):
	scrollP = ObjectProperty( None)
	nomeVoo = StringProperty( '')

	def __init__( self, voo, **kwargs):
		super( TelaParadasVoo, self).__init__( **kwargs)
		self.voo = voo
		self.nomeVoo = voo[0]
		Clock.schedule_once(self.criarscrollview)

	def criarscrollview( self, dt):
		listaParadas = getListaParadas( self.voo[1], random.randint( 30, 1000))
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
		listaVoo = getListaVoo( random.randint( 10, 100))
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
		self.text = voo[0]
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

	def irTelaMapa( self):
		self.current = nomeTelaCarregando
		self.listaTela.append( TelaMapa( name = nomeTelaMapa))
		self.add_widget( self.listaTela[3])
		self.current = nomeTelaMapa

	def sairTelaMapa( self):
		self.current = nomeTelaParadaVoo
		self.remove_widget( self.listaTela[3])
		del self.listaTela[3]

class InterfaceV2App( App):
	"""InterfaceV2App"""
	def build( self):
		pass

"""Definindo os nomes das telas"""
nomeTelaMapa = 'telamap'
nomeTelaSelecVoo = 'telaselecvoo'
nomeTelaParadaVoo = 'telaparada'
nomeTelaInicial = 'telainic'
nomeTelaCarregando = 'telaloading'

if __name__ == '__main__':
	InterfaceV2App().run()
