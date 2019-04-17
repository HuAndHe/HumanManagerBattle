# _*_ coding:utf-8 _*_
import pygame
from pygame.locals import *
from sys import exit
background_path="img/sushiplate.jpg"
pygame.init()
screen=pygame.display.set_mode((640,480),0,32)
background=pygame.image.load(background_path).convert()
pygame.display.set_caption("pygame的第三个程序")

FullScreen=False

while True:
	for event in pygame.event.get():
		if event.type==QUIT:
			exit()
	if event.type==KEYDOWN:
		if event.key==K_f:
			FullScreen = not FullScreen
			if FullScreen:
				screen=pygame.display.set_mode((640,480),FULLSCREEN,32)
			else:
				screen=pygame.display.set_mode((640,480),0,32)
	screen.blit(background,(0,0))
	pygame.display.update()
