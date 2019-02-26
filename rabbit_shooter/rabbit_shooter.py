#导入pygame库
import pygame
from pygame.locals import *
import math
import random

#初始化pygame
pygame.init()
#设定长宽高，并绘制窗体
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
#计数器，用来存放射出的子弹数/射中数
account = [0, 0]
#控制射出的子弹
bullets = []
#子弹速度
bullet_speed = 10
#兔子的角度
rabbit_angle=0.0
# 定义了一个定时器，使得游戏里经过一段时间后就新建一支獾
timer_badguys = 50
badguys = [[640, 100]]
healthvalue = 100


#加载射手
rabbit_shoot = pygame.image.load("resources/images/dude.png")
#加载草地
grass = pygame.image.load("resources/images/grass.png")
#加载兔子窝
rabbit_castle = pygame.image.load("resources/images/castle.png")
#加载兔子子弹
rabbit_bullet = pygame.image.load("resources/images/bullet.png")
#加载坏兔子
bad_rabbit1 = pygame.image.load("resources/images/badguy1.png")
bad_rabbit2 = pygame.image.load("resources/images/badguy2.png")
bad_rabbit3 = pygame.image.load("resources/images/badguy3.png")
bad_rabbit4 = pygame.image.load("resources/images/badguy4.png")
#射手兔位置
rabbit_pos = [100, 100]
#是否按着键
key_press = [False, False, False, False]
#代码主体
while True:
    #背景填充黑色
    screen.fill(0)
    # 添加草地
    for x in range(width//grass.get_width()+1):
        for y in range(height//grass.get_height()+1):
            screen.blit(grass, (x*100, y*100))
    # 添加兔子窝
    screen.blit(rabbit_castle, (0, 30))
    screen.blit(rabbit_castle, (0, 135))
    screen.blit(rabbit_castle, (0, 240))
    screen.blit(rabbit_castle, (0, 345))
    #添加兔子射手
    #screen.blit(rabbit_shoot, rabbit_pos)
    #为使兔子射手跟随鼠标转动，对兔子射手做出处理
    ##1.获取鼠标位置
    mouse_pos = pygame.mouse.get_pos()
    ##2.计算出兔子旋转角度
    rabbit_angle = math.atan2(mouse_pos[1]-(rabbit_pos[1]+rabbit_shoot.get_height()/2), mouse_pos[0]-(rabbit_pos[0]+rabbit_shoot.get_width()/2));
    ##3.旋转兔子射手
    rabbit_shoot_changed = pygame.transform.rotate(rabbit_shoot,360 - (rabbit_angle / math.pi * 180))
    ##4.计算兔子射手位置(保证中心点不变)
    rabbit_pos1 = (rabbit_pos[0]-(rabbit_shoot_changed.get_rect().width-rabbit_shoot.get_width())/2, rabbit_pos[1]-(rabbit_shoot_changed.get_rect().height-rabbit_shoot.get_height())/2)
    ##5.放置兔子
    screen.blit(rabbit_shoot_changed, rabbit_pos1)
    #屏幕上绘制子弹
    for bullet in bullets:
        index = 0
        #计算子弹的移动量
        velx = math.cos(bullet[0]) * bullet_speed
        vely = math.sin(bullet[0]) * bullet_speed
        bullet[1] += velx
        bullet[2] += vely
        #判断子弹超出屏幕，则销毁子弹
        if bullet[1] < -64 or bullet[1] > 640 or bullet[2] < -64 or bullet[2] > 480:
            bullets.pop(index)
        index += 1
        # 重新绘制子弹
        rabbit_bullet_changed = pygame.transform.rotate(rabbit_bullet, 360 - (bullet[0] / math.pi * 180))
        screen.blit(rabbit_bullet_changed, (bullet[1], bullet[2]))
    #创建计时器，根据随机不定时长创建坏蛋
    if timer_badguys == 0:
        badguys.append([640, random.randint(50, 430)])
        timer_badguys = random.randint(15, 35)
    #初始化序列
    index_badguys = 0
    #屏幕上绘制坏蛋
    for badguy in badguys:
        #坏蛋随机向前移动
        badguy[0] -= random.randint(3,9)
        #
    #刷新显示的样子
    pygame.display.flip()
    #监听退出事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #移动兔子（按一下键动一下）
        # if event.type == pygame.KEYDOWN:
        #     if event.key == K_s:
        #         if rabbit_pos[1] <= 310:
        #             rabbit_pos[1] += 5
        #     if event.key == K_w:
        #         if  rabbit_pos[1] >= 100:
        #             rabbit_pos[1] -= 5
        #判定按下按键
        if  event.type == pygame.KEYDOWN:
            if event.key == K_w:
                key_press[0] = True
            if event.key == K_s:
                key_press[1] = True
            if event.key == K_a:
                key_press[2] = True
            if event.key == K_d:
                key_press[3] = True
        #判定松开按键
        if event.type == pygame.KEYUP:
            if event.key == K_w:
                key_press[0] = False
            if event.key == K_s:
                key_press[1] = False
            if event.key == K_a:
                key_press[2] = False
            if event.key == K_d:
                key_press[3] = False
        # 判定发射按键
        if event.type == pygame.MOUSEBUTTONDOWN:
            account[0] += 1
            bullets.append([rabbit_angle, rabbit_pos1[0]+rabbit_shoot_changed.get_rect().width/2, rabbit_pos1[1]+rabbit_shoot_changed.get_rect().height/2])
    # 移动兔子（按住一直动）
    if key_press[0]:
        if  rabbit_pos[1] >= 100:
            rabbit_pos[1] -= 5
    if key_press[1]:
        if rabbit_pos[1] <= 325:
            rabbit_pos[1] += 5
    if key_press[2]:
        if  rabbit_pos[0] >= 100:
            rabbit_pos[0] -= 5
    if key_press[3]:
        if rabbit_pos[0] <= 300:
            rabbit_pos[0] += 5
    timer_badguys -= 1