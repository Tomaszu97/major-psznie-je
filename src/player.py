from game_object import *
from pygame.mixer import *
import sys

class Player(GameObject):
	
	points = 0
	life = 7
	
	def __init__(self, picture):
		GameObject.__init__(self, picture)
		self.type = ObjectType.PLAYER
		self.ding = Sound('../data/ding.ogg')
	
	def isColliding(self, otherObject):
		if(GameObject.isColliding(self, otherObject)):
			self.ding.stop()
			self.ding.play()
			if(otherObject.type == ObjectType.GOOD_BEER):
				self.points += 10
				if(self.points % 100) == 0 and self.life < 8:
					self.life += 1
				otherObject.type = ObjectType.NULL
				
			elif(otherObject.type == ObjectType.BAD_BEER):
				self.life -= 1
				if(self.life <= 0): sys.exit()
				otherObject.type = ObjectType.NULL
			return True
		else:
			return False