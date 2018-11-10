import sys
import pygame
from pygame.locals import *
from pygame.time import *
from pygame.key import *
from pygame.sprite import *
from enum import Enum

class ObjectType(Enum):
	NULL = 0
	PLAYER = 1
	GOOD_BEER = 2
	BAD_BEER = 3

class GameObject(Sprite):
	speed = 5
	rotation_speed = 0
	movement_vector = [0,0]
	rotation = 0
	type = ObjectType.NULL
	
	def __init__(self, picture):
		Sprite.__init__(self)
		self.image = pygame.image.load(picture).convert_alpha()
		self.rect = self.image.get_rect()
		self.original_image = self.image
	
	def setPosition(self, x, y):
		self.rect.x = x
		self.rect.y = y
	
	def move(self, x, y):
		self.rect.x += x
		self.rect.y += y
		
	def updateMovement(self):
		self.move(self.movement_vector[0], self.movement_vector[1])
		self.rotate(self.rotation_speed)
		
	def isColliding(self, otherObject):
		if(self.rect.colliderect(otherObject.rect)):
			return True
		else:
			return False
			
	def rotate(self, angle):
		self.rotation += angle
		self.image = pygame.transform.rotate(self.original_image, self.rotation)
		self.rect = self.image.get_rect(center=self.rect.center)