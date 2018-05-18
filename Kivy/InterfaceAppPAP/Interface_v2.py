import kivy
from kivy.app import App
from kivy.lang import Builder

from kivy.uix.screenmanager import ScreenManager, Screen
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

class ScrollListaVoo( ScrollView):
	lista = getListaVoo( 15)

	layout = GridLayout(cols=1, padding=10, spacing=10, size_hint=(None, None), width=500)

	layout.bind(minimum_height=layout.setter('height'))

	for i in range( len(lista)):
		btn = Button(text=lista[i][0], size=(480, 40), size_hint=(None, None))
		layout.add_widget(btn)

class Tela1( Screen):
	#scrollL = ObjectProperty( None)
	def __init__( self, **kwargs):
		listaVoo = getListaVoo( 15)
		print (listaVoo)
		boxlay = BoxLayout( orientation='vertical')

		butExit = Button( text='Sair', font_size=14)
		boxlay.add_widget( butExit)

		lista = GridLayout(cols=1, padding=10, spacing=10, size_hint=(None, None), width=500)

		lista.bind(minimum_height=lista.setter('height'))

		for i in range( len(listaVoo)):
			btn = Button(text=listaVoo[i][0], size=(480, 40), size_hint=(None, None))
			lista.add_widget(btn)

		scroll = ScrollView(size_hint=(None, None), size=(500, 320), pos_hint={'center_x': .5, 'center_y': .5}, do_scroll_x=False)
		scroll.add_widget( lista)

		boxlay.add_widget(scroll)
		self.add_widget( boxlay)

class TelaInicial( Screen):
	pass

class Manager( ScreenManager):
	pass

interface = Builder.load_file( "main.kv")

class interfaceV2App( App):
	def build( self):
		"""
		screenChefe = Manager()
		tl1 = Tela1( name = 'tela1')
		screenChefe.add_widget( tl1)
		return screenChefe
		"""
		return interface

if __name__ == '__main__':
	interfaceV2App().run()