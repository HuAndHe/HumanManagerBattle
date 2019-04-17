# _*_ coding:utf-8 _*_
import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen=pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption("pygame的第二个程序")

font=pygame.font.SysFont("arial",16)

font_height=font.get_linesize()
event_text=[]

while True:
	event=pygame.event.get()
	event_text.append(str(event))

	event_text=event_text[-480/font_height:]

	if event.type==QUIT:
		exit()
	screen.fill((255,255,255))
	y=480-font_height
	for text in reversed(event_text):
		screen.blit(font.render(text,True,(0,0,0)),(0,y))

		y-=font_height
	pygame.display.update()