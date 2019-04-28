import turtle
#定义画布大小及顶点位置
turtle.setup(width=800, height=880, startx=600, starty=0)
turtle.screensize(300, 300, "#D6C49E")
#定义画笔
t=turtle.Pen()
t.speed(5)      #移动速度
t.pencolor()  #颜色
t.pensize(1.5)  #宽度
#绘制横线
t.penup()      #抬起
t.goto(-240,270)   #起始点
t.pendown()      #下笔
for i in range(1,6,1): 
    t.forward(480)  #画480px----------------------- 往返  5*2=10横线
    t.penup()    #抬起
    t.right(90)  #右转90度
    t.forward(60)  #移动60px
    t.right(90)    #右转90度
    t.pendown()   #下笔
    t.forward(480)  #画480px
    t.penup()   #抬起
    t.left(90)   #左转90度
    t.forward(60)  #移动60px
    t.left(90)   #左转90度
    t.pendown()   #下笔
#绘制竖线
t.left(90)
t.penup()
t.forward(60)
t.pendown()
for i in range(1,5,1):
    t.forward(240)
    t.penup()
    t.forward(60)
    t.pendown()
    t.forward(240)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.forward(240)
    t.penup()
    t.forward(60)
    t.pendown()
    t.forward(240)
    t.left(90)
    t.forward(60)
    t.left(90)
t.forward(540)
t.left(90)
t.forward(480)
t.left(90)
t.forward(540)
#绘制斜线
t.left(90)
t.forward(180)
t.left(45)
t.forward(120*1.414)
t.left(45)
t.forward(-120)
t.left(45)
t.forward(120*1.414)
t.penup()
t.goto(-60,270)
t.pendown()
t.right(180)
t.forward(120*1.414)
t.right(45)
t.forward(-120)
t.right(45)
t.forward(120*1.414)
#需要调用的函数
def angle(x,y):
    t.penup()
    t.goto(x+5,y+5)
    t.pendown()
    t.setheading(0)  #设置当前角度朝向
    t.forward(5)
    t.goto(x+5,y+5)
    t.left(90)
    t.forward(5)
    t.penup()
    t.goto(x+5,y-5)
    t.pendown()
    t.setheading(0)
    t.forward(5)
    t.goto(x+5,y-5)
    t.left(90)
    t.forward(-5)
    t.penup()
    t.goto(x-5,y+5)
    t.pendown()
    t.setheading(0)
    t.forward(-5)
    t.goto(x-5,y+5)
    t.left(90)
    t.forward(5)
    t.penup()
    t.goto(x-5,y-5)
    t.pendown()
    t.setheading(0)
    t.forward(-5)
    t.goto(x-5,y-5)
    t.left(90)
    t.forward(-5)

def a(x,y):
    t.penup()
    t.goto(x-5,y+5)
    t.pendown()
    t.setheading(0)
    t.forward(-5)
    t.goto(x-5,y+5)
    t.left(90)
    t.forward(5)
    t.penup()
    t.goto(x-5,y-5)
    t.pendown()
    t.setheading(0)
    t.forward(-5)
    t.goto(x-5,y-5)
    t.left(90)
    t.forward(-5)

def v(x,y):
    t.penup()
    t.goto(x+5,y+5)
    t.pendown()
    t.setheading(0)
    t.forward(5)
    t.goto(x+5,y+5)
    t.left(90)
    t.forward(5)
    t.penup()
    t.goto(x+5,y-5)
    t.pendown()
    t.setheading(0)
    t.forward(5)
    t.goto(x+5,y-5)
    t.left(90)
    t.forward(-5)
    t.penup()
#修饰炮和兵所在点
angle(180,150)
angle(-180,150)
angle(180,-150)
angle(-180,-150)
angle(-120,90)
angle(0,90)
angle(120,90)
angle(-120,-90)
angle(0,-90)
angle(120,-90)

a(240,90)
a(240,-90)
v(-240,-90)
v(-240,90)
#绘制一个长方形外围线，设置笔的粗细
t.penup()
t.goto(-250,-280)
t.pendown()
t.pensize(8)
t.forward(560)
t.right(90)
t.forward(500)
t.right(90)
t.forward(560)
t.right(90)
t.forward(500)
t.right(90)

turtle.done()
