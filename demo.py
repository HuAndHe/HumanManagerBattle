#_*_coding:utf-8 _*_
import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen=pygame.display.set_mode((800,800),0,32)
pygame.display.set_caption("中国AI象棋")
screen.fill((255,255,255))
screen.set_clip(0, 0, 600, 650)
#竖线
pygame.draw.line(screen, (222, 125, 44), (75, 0), (75, 280), 1)
pygame.draw.line(screen, (222, 125, 44), (150, 0), (150, 280), 1)
pygame.draw.line(screen, (222, 125, 44), (225, 0), (225, 280), 1)
pygame.draw.line(screen, (222, 125, 44), (300, 0), (300, 280), 1)
pygame.draw.line(screen, (222, 125, 44), (375, 0), (375, 280), 1)
pygame.draw.line(screen, (222, 125, 44), (450, 0), (450, 280), 1)
pygame.draw.line(screen, (222, 125, 44), (525, 0), (525, 280), 1)

pygame.draw.line(screen, (222, 125, 44), (75, 370), (75, 650), 1)
pygame.draw.line(screen, (222, 125, 44), (150, 370), (150, 650), 1)
pygame.draw.line(screen, (222, 125, 44), (225, 370), (225, 650), 1)
pygame.draw.line(screen, (222, 125, 44), (300, 370), (300, 650), 1)
pygame.draw.line(screen, (222, 125, 44), (375, 370), (375, 650), 1)
pygame.draw.line(screen, (222, 125, 44), (450, 370), (450, 650), 1)
pygame.draw.line(screen, (222, 125, 44), (525, 370), (525, 650), 1)
#横线
pygame.draw.line(screen, (0, 0, 255), (0, 70), (600, 70), 1)
pygame.draw.line(screen, (0, 0, 255), (0, 140), (600, 140), 1)
pygame.draw.line(screen, (0, 0, 255), (0, 210), (600, 210), 1)
pygame.draw.line(screen, (0, 0, 255), (0, 280), (600, 280), 1)
pygame.draw.line(screen, (0, 0, 255), (0, 370), (600, 370), 1)
pygame.draw.line(screen, (0, 0, 255), (0, 440), (600, 440), 1)
pygame.draw.line(screen, (0, 0, 255), (0, 510), (600, 510), 1)
pygame.draw.line(screen, (0, 0, 255), (0, 580), (600, 580), 1)
#斜线
pygame.draw.line(screen, (222, 125, 44), (225, 0), (375, 140), 1)
pygame.draw.line(screen, (222, 125, 44), (375, 0), (225, 140), 1)

pygame.draw.line(screen, (222, 125, 44), (225, 510), (375, 650), 1)
pygame.draw.line(screen, (222, 125, 44), (375, 510), (225, 650), 1)
#边框
pygame.draw.rect(screen,(0,0,0),((0,0),(600,650)),3)
while True:
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.display.quit()
			exit()
	pygame.display.update()