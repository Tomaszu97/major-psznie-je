#! /usr/bin/env python3
##	TJ 2018
##	beer chaser
##	naming convention:
##	filenames	snake_case
##	classes		PascalCase
##	objects		camelCase

import os
import sys
import pygame
from pygame.locals import *
from pygame.time import *
from pygame.key import *
from pygame.mixer import *
from player import Player
from good_beer import *
from bad_beer import *
from game_object import *
from random import *
from pygame.font import *
from itertools import filterfalse

pygame.init()
screen = pygame.display.set_mode((1000,600))

pygame.mixer.music.load('../data/bipbop.ogg')
pygame.mixer.music.play(-1)

scoreFont = Font('../data/comicsans.ttf', 70)

background = GameObject('../data/background.jpg')
player = Player('../data/jajor.png')
player.move(pygame.display.get_surface().get_rect().width/2 - player.rect.width/2, pygame.display.get_surface().get_rect().height/2 - player.rect.height/2)
player.speed = 20
player.rotation_speed = 10
badBottles = []
goodBottles = []
scoreHearts = GameObject('../data/konon.png')

clock = Clock()

while True:
	clock.tick(60)
	#print(clock.get_fps())
	
	##events
	for event in pygame.event.get():
		if event.type is QUIT:
			sys.exit()
	
	
	##inputs
	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_UP]:
		player.move(0, -player.speed)
	if pressed[pygame.K_DOWN]:
		player.move(0, player.speed)
	if pressed[pygame.K_LEFT]:
		player.move(-player.speed, 0)
	if pressed[pygame.K_RIGHT]:
		player.move(player.speed, 0)
	if pressed[pygame.K_ESCAPE]:
		sys.exit()
	
	
	##logic/physics
	#spawn beer randomly
	rnd = randint(0,800)
	
	if rnd in range(0,20):
		badBottles.append(GoodBeer('../data/piast.png'))
		badBottles[-1].move(randint(0, 1000), -149)
		badBottles[-1].movement_vector = (randint(-10, 10), randint(1, 10))
		badBottles[-1].rotation_speed = uniform(-12, 12)
	if rnd in range(20,40):
		badBottles.append(GoodBeer('../data/piast.png'))
		badBottles[-1].move(randint(0, 1000), 599)
		badBottles[-1].movement_vector = (randint(-10, 10), randint(-10, -1))
		badBottles[-1].rotation_speed = uniform(-12, 12)
	if rnd in range(40,50):
		badBottles.append(BadBeer('../data/perla.png'))
		badBottles[-1].move(randint(0, 1000), -149)
		badBottles[-1].movement_vector = (randint(-10, 10), randint(1, 10))
		badBottles[-1].rotation_speed = uniform(-12, 12)
	if rnd in range(50,60):
		badBottles.append(BadBeer('../data/perla.png'))
		badBottles[-1].move(randint(0, 1000), 599)
		badBottles[-1].movement_vector = (randint(-10, 10), randint(-10, -1))
		badBottles[-1].rotation_speed = uniform(-12, 12)
	if rnd == 298:
		for i in range(7):
			badBottles.append(BadBeer('../data/perla.png'))
			badBottles[-1].move(randint(0,1000), -149)
			badBottles[-1].movement_vector = (0,2*i)
	if rnd == 299:
		for i in range(7):
			badBottles.append(BadBeer('../data/perla.png'))
			badBottles[-1].move(-40, randint(0,600))
			badBottles[-1].movement_vector = (2*i,0)
		
		
	#move objects + detect collisions
	#points automatically add to player when collision is detected
	player.updateMovement()
	
	for bottle in goodBottles:
		bottle.updateMovement()
		
	for bottle in badBottles:
		bottle.updateMovement()
	
	goodBottles = [bottle for bottle in goodBottles if not player.isColliding(bottle) and background.isColliding(bottle)]
	badBottles = [bottle for bottle in badBottles if not player.isColliding(bottle) and background.isColliding(bottle)]
	
	##draw
	screen.fill((0,0,0))
	
	screen.blit(background.image, background.rect.topleft)
	screen.blit(player.image, player.rect.topleft)
	for bottle in badBottles:	screen.blit(bottle.image, bottle.rect.topleft)
	for bottle in goodBottles:	screen.blit(bottle.image, bottle.rect.topleft)
	
	label = scoreFont.render(str(player.points), 1, (255,100,0))
	screen.blit(label, (830, 0))
	
	scoreHearts.setPosition(0,0)
	for i in range(0, player.life):
		screen.blit(scoreHearts.image, scoreHearts.rect.topleft)
		scoreHearts.move(100,0)
	
	
	
	pygame.display.flip()
	