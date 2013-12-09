#!/usr/bin/python
import pygame, sys
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()
windowSurfaceObj = pygame.display.set_mode((349,314))
print "Loading music files..."
introSound = pygame.mixer.Sound("intro.ogg")
loopSound = pygame.mixer.Sound("loop.ogg")
bgmChannel = pygame.mixer.Channel(0)
print "Playing intro..."
bgmChannel.play(introSound)
print "Queueing rest of song..."
bgmChannel.queue(loopSound)
print "Loading image...\nMISSINGNO."
background = pygame.image.load("background.png")
backgroundRect = background.get_rect()

while True:
	bgmChannel.queue(loopSound)
	for event in pygame.event.get():
		if event.type == QUIT:
			print "Quitting..."
			pygame.quit()
			sys.exit()

		else:
			pass

	windowSurfaceObj.blit(background, backgroundRect)
	pygame.display.update()
	fpsClock.tick(30)
