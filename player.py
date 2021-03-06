#!/usr/bin/python
from __future__ import print_function # to make print() work on py2.7
import pygame, sys
from pygame.locals import *

def select_song(title):
    """Changes the song to be played"""
    if title:
        import os
        os.chdir(title)
        print("Changing dir to", title)

# If none specified then load song in current dir
#select_song("DPPtChampion") # uncomment for Cynthia's battle theme

if len(sys.argv) == 2:
    select_song(sys.argv[1])
elif len(sys.argv) > 2:
    print("Too many arguments.")
    quit()

pygame.init()
fpsClock = pygame.time.Clock()

title = None
width = 349
height = 314
bgimage = "background.png"

print("Getting title of song...")

try:
    attrib_file = open("attrib", 'r')
    title = attrib_file.readline().strip()
    bgimage = attrib_file.readline().strip()
    dimensions = attrib_file.readline().strip()

    dimensions_list = dimensions.split(',')
    width, height = dimensions_list
    width, height = int(width), int(height)

finally:
    if not title:
        title = "Failed to load title of song..."

    print("The title shall be \"{}\"".format(title))
    pygame.display.set_caption(title)

windowSurfaceObj = pygame.display.set_mode((width,height))
print("Loading music files...")
introSound = pygame.mixer.Sound("intro.ogg")
loopSound = pygame.mixer.Sound("loop.ogg")
bgmChannel = pygame.mixer.Channel(0)
print("Playing intro...")
bgmChannel.play(introSound)
print("Queueing rest of song...")
bgmChannel.queue(loopSound)
print("Loading image...\nMISSINGNO.")
background = pygame.image.load("background.png")
backgroundRect = background.get_rect()

paused = False
started = True
while True:
    if started:
        bgmChannel.queue(loopSound)
    for event in pygame.event.get():
        if event.type == QUIT:
            print("Quitting...")
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if paused:
                bgmChannel.unpause()
                paused = False
            else:
                bgmChannel.pause()
                paused = True
                
        elif event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_s]:
                bgmChannel.stop()
                started = False

            elif pressed[pygame.K_r]:
                print("Restarting music...")
                bgmChannel.play(introSound)
                started = True

            elif pressed[pygame.K_p] or pressed[pygame.K_SPACE]:
                if paused:
                    bgmChannel.unpause()
                    paused = False
                else:
                    bgmChannel.pause()
                    paused = True
            else:
                pass

        else:
            pass

    windowSurfaceObj.blit(background, backgroundRect)
    pygame.display.update()
    fpsClock.tick(30)
