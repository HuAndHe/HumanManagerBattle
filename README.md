# HumanManagerBattle
  Python实现人机象棋对战,数据分析python +Tenstensorflow
  第一次部署项目到git仓库
  第一步完成项目时间规划
  每晚22：00定时推到github上
  象棋规则及界面实现步骤：
	1.绘制棋盘
	2.绘制棋子
	3.绘制带棋子的棋盘
	4.走棋规则
	5.吃子规则
	6.走棋
	7.判断是否赢棋
	8.按键功能
	9.美化
	10.音效

	
  学习pygame库的使用
  注册下载pygame 
	  py -m pip install -U pygame --user
  演示pygame自带demo
	  py -m pygame.examples.aliens
  查看当前机器支持的显示模式：
	  pygame.display.list_modes()
  全屏显示：
  screen = pygame.display.set_mode((640, 480), FULLSCREEN, 32)
  可变尺寸的显示：
  screen = pygame.display.set_mode((640, 480), RESIZABLE, 32)
  其他、复合模式：
  screen = pygame.display.set_mode((640, 480), HWSURFACE | FULLSCREEN, 32)
  查看当前系统支持的所有字体
  pygame.font.get_fonts()

  font 使用步骤：
  my_font = pygame.font.SysFont("arial", 16)	 字体名 大小
  text_surface = my_font.render("Pygame is cool!", True, (0,0,0), (255, 255, 255))  文字 是否开启锯齿 字体颜色 背景颜色
  screen.blit(text_surface, (x, y)) 
  
  
  学习pygame Vector向量的知识：
  python2.x 使用gameobjects
  python3.x 使用https://www.pygame.org/wiki/2DVectorClass
  
 2019/4/18学习任务 继续学习pygame（10）  修改论文 开始制作答辩ppt
  键盘事件：
   pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_SPACE]:
        # Space key has been pressed
        fire()

 2019/4/22 修改毕设，论文