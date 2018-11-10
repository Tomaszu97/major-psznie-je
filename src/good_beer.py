from game_object import *

class GoodBeer(GameObject):
	
	def __init__(self, picture):
		GameObject.__init__(self, picture)
		self.type = ObjectType.GOOD_BEER