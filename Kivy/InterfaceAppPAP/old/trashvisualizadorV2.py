from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty, StringProperty, ListProperty

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button

import random

# pegar a lista de todos os voos do servidor
def getListaVoo( n):
	listaVoo = []
	for i in range( n):
		voo = StringProperty('Voo '+str( i * ( 3**3) + 10))
		listaVoo.append( voo)
	return  listaVoo


# selecionando um voo, pegar a lista de todas as paradas do voo
def getListaParadas( voo):
	listaParadas = []
	peso = NumericProperty( 50)
	for i in range(1,15):
		rlat = NumericProperty( random.randint( -90, 90) + random.random())
		rlong = NumericProperty( random.randint( -180, 180) + random.random())
		rMovCarga = NumericProperty( rambom.randint( -50, 50))
		if peso + rMovCarga < 0:
			rMovCarga = NumericProperty( 15)
		peso += rMovCarga
		listaParadas.append( [rlat, rlong, rMovCarga, peso])

	return listaParadas


class BlListaVoo( Widget):
	listaVoo = getListaVoo(15)
	def __init__( self):
		lista = BoxLayout( orientation = 'vertical', spacing = 10, width = 500)
		lista.bind(minimum_height=lista.setter('height'))

		for i in range( len( self.listaVoo)):
			newBt = Button( text = str( self.listaVoo[i]))
			lista.add_widget( newBt)

		scroll = ScrollView( size=(500, 320), pos_hint={'center_x': .5, 'center_y': .5}, do_scroll_x=False)
		scroll.add_widget( lista)

class TelaListaVoos( Screen):
	def __init__(self):
		self.add_widget( BlListaVoo())
		self.name = name
		return self
		
		

class Manager( ScreenManager):
	pass

class VisualizadorV2App( App):
	def build (self):

		scrManag = Manager()
		scrManag.add_widget( TelaListaVoos())
		return scrManag



if __name__ == '__main__':
	VisualizadorV2App().run()