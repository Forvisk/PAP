from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image

class Mapa( Widget):
	wimg = Image( source = 'mapa_Razavia_v2.png')

class MapaApp( App):

	def build( self):
		return Mapa()


if __name__ == '__main__':
	MapaApp().run()