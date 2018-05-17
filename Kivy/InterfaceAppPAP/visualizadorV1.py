from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen

import random


def getListaVoo( n):
	listaVoo = []
	for i in range( n):
		listaVoo.append( [ i + 1, 'Voo '+str( i * ( 3**3) + 10)])
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
	listaMostra = []
	k = 0
	for i in range( k, k+8):
		if i < len( listaVoo):
			listaMostra.append( listaVoo[ i])
		else:
			listaMostra.append( [ 0, ''])
	print (listaMostra)

	def retornaMostra( self, i):
		return self.listaMostra[ self.k + i][ 1]

	def nextMostra( self):
		if self.k + 8 < len( self.listaVoo):
			self.k += 8
			del self.listaMostra[:]
			for i in range( self.k, self.k+8):
				if i < len( self.listaVoo):
					self.listaMostra.append( self.listaVoo[ i])
				else:
					self.listaMostra.append( [ 0, ''])
		print ( self.listaMostra)

	def lastMostra( self):
		if self.k - 8 >= 0:
			self.k -= 8
			del self.listaMostra[:]
			for i in range( self.k, self.k+8):
				if i < len( self.listaVoo):
					self.listaMostra.append( self.listaVoo[ i])
				else:
					self.listaMostra.append( [ 0, ''])
		print (self.listaMostra)
	pass

class Manager( ScreenManager):
	pass

class VisualizadorV5App( App):
	def build( self):
		pass

if __name__ == '__main__':
	VisualizadorV5App().run()