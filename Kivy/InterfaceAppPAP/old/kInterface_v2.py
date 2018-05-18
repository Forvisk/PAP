from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


# ver isso
# https://kivy.org/docs/api-kivy.uix.scrollview.html

class Voo():

	def __init__( self, num, listaParadas):
		self.name = 'voo' + str(num)
		self.paradas = listaParadas


class TopBar( BoxLayout):
	def build( self):
		self.orientation = 'horizontal'
		butAnterior = Button( text='<')
		nomeVoo = Label( text = 'Voo x')
		butSeguinte = Button( text='>')
		#selecaoVoo = BoxLayout( orientation='horizontal')
		self.add_widget(butAnterior)
		self.add_widget(nomeVoo)
		self.add_widget(butSeguinte)

		return self


class InterfaceV2App( App):
	def build( self):
		top = TopBar()
		interface = BoxLayout( orientation='vertical')
		interface.add_widget( top)

		return interface

if __name__ == '__main__':
	InterfaceV2App().run()