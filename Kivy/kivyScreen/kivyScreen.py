from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition

from kivy.uix.widget import Widget
from kivy.uix.image import Image


class Mapa( Image):
	wimg = Image( source = 'mapa_Razavia_v2.png')

class TelaInicial( Screen):
	pass

class Tela1( Screen):
	pass

class Tela2( Screen):
	pass

class ScreenManagement( ScreenManager):
	pass

interface = Builder.load_file( "main.kv")

class MainApp( App):
	def build( self):
		return interface

if __name__ == '__main__':
	MainApp().run()