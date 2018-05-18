from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import NumericProperty, StringProperty, ListProperty

import random


def getListaVoo( n):
	listaVoo = []
	for i in range( n):
		listaVoo.append( 'Voo '+str( i * ( 3**3) + 10))
	return listaVoo

def getListaParadas( voo):
	listaParadas = []
	peso = 50
	for i in range(1,15):
		rlat = random.randint( -90, 90) + random.random()
		rlong = random.randint( -180, 180) + random.random()
		rMovCarga = rambom.randint( -50, 50)
		if peso + rMovCarga < 0:
			rMovCarga = 15
		peso += rMovCarga
		listaParadas.append( [rlat, rlong, rMovCarga, peso])

	return listaParadas


class TelaListaVoo( Screen):
	listaVoo = getListaVoo( 15)
	print( listaVoo)
	listaMostra = ListProperty([])
	k = NumericProperty(0)
	for i in range( k, k+8):
		if i < len( listaVoo):
			listaMostra.append( listaVoo[ i])
		else:
			listaMostra.append( '')
	print (listaMostra)

	def retornaMostra( self, i):
		return self.listaMostra[ self.k + i]

	def nextMostra( self):
		if self.k + 8 < len( self.listaVoo):
			self.k += 8
			for i in range( self.k, self.k+8):
				if i < len( self.listaVoo):
					self.listaMostra[i - self.k] = self.listaVoo[i]
				else:
					self.listaMostra[i - self.k] =  ''
		print ( self.listaMostra)

	def lastMostra( self):
		if self.k - 8 >= 0:
			self.k -= 8
			for i in range( self.k, self.k+8):
				if i < len( self.listaVoo):
					self.listaMostra[i - self.k] = self.listaVoo[i]
				else:
					self.listaMostra[i - self.k] =  ''
		print (self.listaMostra)
	pass

class Manager( ScreenManager):
	pass

class VisualizadorV5App( App):
	def build( self):
		pass

if __name__ == '__main__':
	VisualizadorV5App().run()