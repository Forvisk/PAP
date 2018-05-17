from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint


class JogoPong( Widget):
	bola = ObjectProperty( None)
	jogador1 = ObjectProperty( None)
	jogador2 = ObjectProperty( None)

	def serve_bola( self, vel=( 4, 0)):
		self.bola.center = self.center
		self.bola.velocidade = vel


	def atualiza( self, dt):
		self.bola.move()

		self.jogador1.rebate_bola( self.bola)
		self.jogador2.rebate_bola( self.bola)

		# rebat eem cima e em baixo
		if ( self.bola.y < 0) or ( self.bola.top > self.height):
			self.bola.velocidade_y *= -1

		# se a bola bate na esquerda e direita e marca pontos
		if ( self.bola.x < 0):
			self.jogador2.ponto += 1
			self.serve_bola( vel = ( 4, 0))
		if ( self.bola.right > self.width):
			self.jogador1.ponto += 1
			self.serve_bola( vel = ( -4, 0))
		pass

	def on_touch_move( self, touch):
		if ( touch.x < self.width /3):
			self.jogador1.center_y = touch.y

		if ( touch.x > self.width /3):
			self.jogador2.center_y = touch.y


class BolaPong( Widget):

	# velocidade da bola
	velocidade_x = NumericProperty(0)
	velocidade_y = NumericProperty(0)

	velocidade = ReferenceListProperty( velocidade_x, velocidade_y)

	def move( self):
		self.pos = Vector( *self.velocidade) + self.pos
		
class PaletaPong( Widget):

	ponto = NumericProperty(0)

	def rebate_bola( self, bola):
		if( self.collide_widget( bola)):
			maisVelocidade = 1.1
			mudancaDirecao = 0.02 * Vector( 0, bola.center_y - self.center_y)
			bola.velocidade = maisVelocidade * ( mudancaDirecao - bola.velocidade)

class PongApp( App):
	
	def build(self):
		jogo = JogoPong()
		jogo.serve_bola()
		Clock.schedule_interval( jogo.atualiza, 1.0/60.0)
		return jogo

if __name__ == '__main__':
	PongApp().run()