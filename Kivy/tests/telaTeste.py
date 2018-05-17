from kivy.app import App
#from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.image import Image

Builder.load_string("""
<Tela1>:
	BoxLayout:
		size: 50, 50
		Button:
			size: 20, 50
			text: 'Selecao de Voo'
			on_press:
				root.manager.current = 'selecaoVoo'

<Tela2>:
	BoxLayout:
		size: 50, 50
		Button:
			size: 20, 50
			text: 'voo1'
			on_press:
				root.manager.current = 'mostraVoo'
		Button:
			size: 20, 50
			text: 'voo2'
			on_press:
				root.manager.current = 'mostraVoo'

<Tela3>:
	BoxLayout:
		size: 50, 50
		Button:
			size: 20, 50
			text: 'test'
			on_press:
				root.manager.current = 'menu'
""")

class Tela1( Screen):
	pass

class Tela2( Screen):
	pass

class Tela3( Screen):
	pass


sm  = ScreenManager()
sm.add_widget( Tela1( name = 'menu'))
sm.add_widget( Tela2( name = 'selecaoVoo'))
sm.add_widget( Tela3( name = 'mostraVoo'))

sm.display = 'menu'


class TelaApp( App):

	def build( self):
		return sm

if __name__ == '__main__':
	TelaApp().run()