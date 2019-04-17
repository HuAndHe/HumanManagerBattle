# _*_ coding: utf-8 _*_
#两张背景图片的路径
background_img='img/sushiplate.jpg'
mouse_img='img/fugu.png'
#导入pygame 库
import pygame
from pygame.locals import *
#向sys借一个exit函数来退出程序
from sys import exit

#初始化pygame
pygame.init()

#创建一个窗口 set_mode会返回一个Surface对象  分辨率 标志位  色深
screen=pygame.display.set_mode((640,480),0,32)
#设置窗口标题
pygame.display.set_caption("第一个pygame界面")

#加载并转换图像
background=pygame.image.load(background_img).convert()
 #加载并转换图像，图像要有有Alpha通道，保留了Alpha 通道信息（可以简单理解为透明的部分）
mouse_cursor=pygame.image.load(mouse_img).convert_alpha()

#游戏主循环
while True:
	for event in pygame.event.get():
		if event.type==QUIT:
			exit()
	 #将背景图画上去，blit是个重要函数，第一个参数为一个Surface对象，第二个为左上角位置。
	screen.blit(background,(0,0))
	x,y=pygame.mouse.get_pos()

	x-=mouse_cursor.get_width()/2
	y-=mouse_cursor.get_height()/2


	screen.blit(mouse_cursor,(x,y))
	#刷新画面
	pygame.display.update()

	#pygame.display.flip()是交替显示的意思
