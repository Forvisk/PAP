from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.slider import Slider

# ver isso
# https://kivy.org/docs/api-kivy.uix.scrollview.html

class Voo():
	def __init__( self, num, listaParadas):
		self.name = 'voo' + str(num)
		self.paradas = listaParadas

class ListaParadas( Widget):
	pass

class BarraTopo( Widget):
	pass

class Interface( Widget):
	top = BarraTopo()
	lista = ListaParadas()

class InterfaceV1App( App):
	def build( self):
		interface = ListaParadas()

		return interface
		pass

if __name__ == '__main__':
	InterfaceV1App().run()