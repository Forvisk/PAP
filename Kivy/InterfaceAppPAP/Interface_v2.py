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

# selecionando um voo, pegar a lista de todas as paradas do voo
# aqui se conecta com o servidor e pega os dados
def getListaParadas( voo, n):
	listaParadas = []
	peso = 50
	for i in range(1,n):
		rlat = round( random.randint( -90, 90) + random.random(), 4)
		rlong = round( random.randint( -180, 180) + random.random(), 4)
		rMovCarga = random.randint( -50, 50)
		if peso + rMovCarga < 0:
			rMovCarga = 15
		peso += rMovCarga
		# parada = [ latitude, longitude, peso movido, peso final]
		listaParadas.append( [rlat, rlong, rMovCarga, peso])

	return listaParadas


def listaParadastoStr( parada):
	#print( parada)
	
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
		#[ nomeVoo, codigo]
		listaVoo.append( ['Voo '+str( i * ( 3**3) + 10), (i+10)**2])
	return listaVoo


# ver esse link	https://stackoverflow.com/questions/46749491/kivy-python-scroll-view-in-a-layout
class TelaParadasVoo( Screen):
	scrollP = ObjectProperty( None)
	nomeVoo = StringProperty( '')

	def __init__( self, voo, **kwargs):
		super( TelaParadasVoo, self).__init__( **kwargs)
		self.voo = voo
		#print( voo)
		self.nomeVoo = voo[0]
		Clock.schedule_once(self.criarscrollview)

	def criarscrollview( self, dt):
		listaParadas = getListaParadas( self.voo[1], 60)
		#print ( self.voo)
		#print ( listaParadas)
		lista = GridLayout( cols=1, padding=10, spacing=5, size_hint_y = None, width=400)
		
		lista.bind( minimum_height=lista.setter('height'))
		
		for i in range( len(listaParadas)):
			sParadas = listaParadastoStr( listaParadas[i])
			#como \t não funciona no kivy, colocamos 4 espaços para simbolizar o tab
			stringParada = sParadas[0] + '    ' + sParadas[1] + '    ' + sParadas[2]
			lbStr = Label( text = stringParada, font_size = 15, size=( Window.width* 0.9, 40), size_hint=(1, None))
			lista.add_widget( lbStr)

		scrollP = ScrollView( size_hint=(1, None),size=(Window.width * 0.9, Window.height * 0.8), pos_hint={'center_x': .5, 'center_y': .4}, do_scroll_x=False)
		scrollP.add_widget( lista)
		
		self.add_widget( scrollP)


class TelaSelectVoo( Screen):
	scrollV = ObjectProperty( None)

	def __init__( self, **kwargs):
		super( TelaSelectVoo, self).__init__( **kwargs)
		Clock.schedule_once(self.criarscrollview)

	def criarscrollview( self, dt):
		listaVoo = getListaVoo( 15)
		#print (listaVoo)

		lista = GridLayout(cols=1, padding=10, spacing=10, size_hint_y = None, width=400)

		lista.bind(minimum_height=lista.setter('height'))

		for i in range( len(listaVoo)):
			#btn = Button( text=listaVoo[i][0], size=(480, 40), size_hint=(1, None))
			#btn.bind( on_press = self.parent.irTelaParadaVoo( listaVoo[i][1]))
			btn = BotaoListaVoo( text=listaVoo[i][0], size=(480, 40), size_hint=(1, None))
			btn.criaBotaoLVoo( listaVoo[i])
			lista.add_widget(btn)

		scrollV = ScrollView( size_hint=(1, None), size=(Window.width * 0.9, Window.height * 0.8), pos_hint={'center_x': .5, 'center_y': .4}, do_scroll_x=False)
		scrollV.add_widget( lista)

		self.add_widget(scrollV)

class BotaoListaVoo( Button):
	def __init__( self, **kwargs):
		super( BotaoListaVoo, self).__init__( **kwargs)
		#self.criaBotaoLVoo( voo):

	def criaBotaoLVoo( self, voo):
		#print( voo)
		self.voo = voo


class TelaInicial( Screen):
	pass

class Manager( ScreenManager):
	def __init__(self, **kwargs):
		super(Manager, self).__init__(**kwargs)
		self.listaTela = [ TelaInicial()]
		self.add_widget( self.listaTela[0])

	def irTelaSelecVoo( self):
		nomeTelaSelecVoo = 'telaselecvoo'
		self.listaTela.append( TelaSelectVoo( name = nomeTelaSelecVoo))
		self.add_widget( self.listaTela[1])
		self.current = nomeTelaSelecVoo

	def voltarTelaInic( self):
		self.current = 'telainic'
		self.remove_widget( self.listaTela[1])
		del self.listaTela[1]

	def  recarregaTelaSelecVoo( self):
		self.current = 'telainic'
		self.remove_widget( self.listaTela[1])
		del self.listaTela[1]
		self.irTelaSelecVoo()

	def irTelaParadaVoo( self, voo):
		nomeTelaParadaVoo = 'telaparada'
		self.current = 'telainic'
		self.remove_widget( self.listaTela[1])
		del self.listaTela[1]
		print( voo)
		self.listaTela.append( TelaParadasVoo( voo, name = nomeTelaParadaVoo))
		self.add_widget( self.listaTela[1])
		self.current = nomeTelaParadaVoo
	
	def sairTelaParadaVoo( self):
		nomeTelaSelecVoo = 'telaselecvoo'
		self.remove_widget( self.listaTela[1])
		del self.listaTela[1]
		self.irTelaSelecVoo()
		


#interface = Builder.load_file( "main.kv")

class interfaceV2App( App):
	def build( self):
		pass


if __name__ == '__main__':
	interfaceV2App().run()
