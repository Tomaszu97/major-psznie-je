from game_object import *

class BadBeer(GameObject):
	
	def __init__(self, picture):
		GameObject.__init__(self, picture)
		self.type = ObjectType.BAD_BEER