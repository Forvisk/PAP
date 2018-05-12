from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class TelaLogin( GridLayout):

	def __init__( self, **kwargs):
		super(LoginScreen, self).__init__( **kwargs)
		self.cols = 2
		self.add_widget( Label( text = 'Usuario: '))
		self.usuario = TextInput( multiline = False)
		self.add_widget( self.usuario)
		self.add_widget( Label( text = 'Senha:'))
		self.senha = TextInput( multiline = False)
		self.add_widget( self.senha)

class MyApp( App):

	def build( self):
		return LoginScreen()


if __name__ == '__main__':
	MyApp().run()
