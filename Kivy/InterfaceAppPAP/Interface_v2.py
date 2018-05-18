import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock

from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty

from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

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
		pass

	def criarscrollview( self, dt):
		pass



class TelaSelectVoo( Screen):
	scrollV = ObjectProperty( None)

	def __init__( self, **kwargs):
		super( TelaSelectVoo, self).__init__( **kwargs)
		Clock.schedule_once(self.criarscrollview)
		pass

	def criarscrollview( self, dt):
		listaVoo = getListaVoo( 15)
		print (listaVoo)

		lista = GridLayout(cols=1, padding=10, spacing=10, size_hint_y = None, width=500)

		lista.bind(minimum_height=lista.setter('height'))

		for i in range( len(listaVoo)):
			btn = Button(text=listaVoo[i][0], size=(480, 40), size_hint=(1, None))
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

	def voltarTelaInic( self):
		self.current = 'telainic'
		self.remove_widget( self.listaTela[1])
		del self.listaTela[1]


	def irTelaSelecVoo( self):
		nomeTelaSelecVoo = 'telaselecvoo'
		self.listaTela.append( TelaSelectVoo( name = nomeTelaSelecVoo))
		self.add_widget( self.listaTela[1])
		self.current = nomeTelaSelecVoo

	def  recarregascrollview( self):
		self.current = 'telainic'
		self.remove_widget( self.listaTela[1])
		del self.listaTela[1]
		self.irTelaSelecVoo()

	def irTelaParadaVoo( self, voo):
		nomeTelaParadaVoo = 'telaparada'
		self.listaTela.append( TelaParadasVoo( voo,name = nomeTelaParadaVoo))
		self.add_widget( listaTela[2])
		self.current = nomeTelaParadaVoo


#interface = Builder.load_file( "main.kv")

class interfaceV2App( App):
	def build( self):
		pass


if __name__ == '__main__':
	interfaceV2App().run()