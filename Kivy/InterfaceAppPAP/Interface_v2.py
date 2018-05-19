import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock

from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

# selecionando um voo, pegar a lista de todas as paradas do voo
def getListaParadas( voo):
	listaParadas = []
	peso = 50
	for i in range(1,15):
		rlat = random.randint( -90, 90) + random.random()
		rlong = random.randint( -180, 180) + random.random()
		rMovCarga = random.randint( -50, 50)
		if peso + rMovCarga < 0:
			rMovCarga = 15
		peso += rMovCarga
		# parada = [ latitude, longitude, peso movido, peso final]
		listaParadas.append( [rlat, rlong, rMovCarga, peso])
return listaParadas

def listaParadastoStr( parada):
	if( listaParadas[i][0] < 0):
		sLat = str( listaParadas[i][0] * -1) + '° S'
	else:
		sLat = str( listaParadas[i][0]) + '° N'
	if( listaParadas[i][1] < 0):
		sLong = str( listaParadas[i][1] * -1) + '° W'
	else:
		sLong = str( listaParadas[i][1]) + '° E'
	sCord = sLat + '\n' + sLong
	if( listaParadas[i][2] < 0):
		sCargaMov = 'Descarrega ' str( listaParadas[i][2] * -1) + 'kg'
	elif( listaParadas[i][2] == 0):
		sCargaMov = 'Sem movimento'
	else:
		sCargaMov = 'Carrega ' str( listaParadas[i][2]) + 'kg'
	sCargaFinal = str( peso) + 'kg'
	return [ sCord, sCargaMov, sCargaFinal]
	

def getListaVoo( n):
	listaVoo = []
	for i in range( n):
		#[ nomeVoo, codigo]
		listaVoo.append( ['Voo '+str( i * ( 3**3) + 10), (i+10)**2])
	return listaVoo


# ver esse link	https://stackoverflow.com/questions/46749491/kivy-python-scroll-view-in-a-layout

class TelaParadasVoo( Screen):
	scrollP = ObjectProperty( None)

	def __init__( self, voo, **kwargs):
		super( TelaSelectVoo, self).__init__( **kwargs)
		self.voo = voo
		Clock.schedule_once(self.criarscrollview)

	def criarscrollview( self, dt):
		listaParadas = getListaParadas( self.voo)
		print ( listaParadas)
		lista = GridLayout( cols=3, padding=10, spacing=10, size_hint_y = Nonr, width=500)
		
		lista.bind( minimum_height=lista.setter('height'))
		
		for i in range( len(listaParadas)):
			sParadas = listaParadastoStr( listaParadas[i])
			lbCord = Label( text=sParadas[0], font_size=15, halign='right', valign='middle')
			lbPesMv = Label( text=sParadas[1], font_size=15, halign='left', valign='middle')
			lbPesFn = Label( text=sParadas[2], font_size=15, halign='left', valign='middle')
			lista.add_widget( lbCord)
			lista.add_widget( lbPesMv)
			lista.add_widget( lbPesFn)
			
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
		print (listaVoo)

		lista = GridLayout(cols=1, padding=10, spacing=10, size_hint_y = None, width=500)

		lista.bind(minimum_height=lista.setter('height'))

		for i in range( len(listaVoo)):
			btn = Button(text=listaVoo[i][0], size=(480, 40), size_hint=(1, None))
			btn.bind( on_press = mang.irTelaParadaVoo( listaVoo[i][1]))
			lista.add_widget(btn)

		scrollV = ScrollView( size_hint=(1, None),size=(Window.width * 0.9, Window.height * 0.8), pos_hint={'center_x': .5, 'center_y': .4}, do_scroll_x=False)
		scrollV.add_widget( lista)

		self.add_widget(scrollV)


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
		self.listaTela.append( TelaParadasVoo( voo,name = nomeTelaParadaVoo))
		self.add_widget( self.listaTela[2])
		self.current = nomeTelaParadaVoo
	
	def sairTelaParadaVoo( self):
		nomeTelaSelecVoo = 'telaselecvoo'
		self.remove_widget( self.listaTela[2])
		del self.listaTela[2]
		self.current = nomeTelaSelecVoo
		


#interface = Builder.load_file( "main.kv")

class interfaceV2App( App):
	def build( self):
		pass


if __name__ == '__main__':
	interfaceV2App().run()
