# -*- coding: utf-8 -*-
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
timer_badguys = 100
badguys = []
healthvalue = 194


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
youwin_img = pygame.image.load("resources/images/youwin.png")
gameover_img = pygame.image.load("resources/images/gameover.png")
bad_rabbit = bad_rabbit1
#加载城堡健康值
health_bar = pygame.image.load("resources/images/healthbar.png")
health = pygame.image.load("resources/images/health.png")
#射手兔位置
rabbit_pos = [100, 100]
#是否按着键
key_press = [False, False, False, False]

# 不停地循环执行接下来的部分
# running变量会跟踪游戏是否结束
running = True
# exitcode变量会跟踪玩家是否胜利
exitcode = False
#代码主体
while running:
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
        type = random.randint(1, 4)
        if type == 1:
            bad_rabbit = bad_rabbit1
        elif type == 2:
            bad_rabbit = bad_rabbit2
        elif type == 3:
            bad_rabbit = bad_rabbit3
        else:
            bad_rabbit = bad_rabbit4
        badguys.append([bad_rabbit, 640, random.randint(50, 430)])
        timer_badguys = random.randint(40, 60)
    #初始化序列
    index_badguys = 0
    #屏幕上绘制坏蛋
    for badguy in badguys:
        #坏蛋随机向前移动
        badguy[1] -= random.randint(1,7)
        #获取相应的坏蛋实体
        badrect = pygame.Rect(badguy[0].get_rect())
        badrect.top = badguy[2]
        badrect.left = badguy[1]
        #判断是否进入兔子窝
        if badrect.left < 64:
            healthvalue -= 10
            badguys.pop(index_badguys)
        # 初始化序列
        index_bullets = 0
        #判断子弹是否击中
        for bullet in bullets:
            bulletrect = pygame.Rect(rabbit_bullet.get_rect())
            bulletrect.top = bullet[2]
            bulletrect.left = bullet[1]
            if badrect.colliderect(bulletrect):
                account[1] += 1
                badguys.pop(index_badguys)
                bullets.pop(index_bullets)
            index_bullets += 1
        index_badguys += 1
    #随机添加不同的坏蛋
    for badguy in badguys:
        screen.blit(badguy[0], (badguy[1], badguy[2]))
    # 添加一个计时
    # 使用了PyGame默认的大小为24的字体来显示时间信息。
    font = pygame.font.Font(None, 24)
    survivedtext = font.render(str((90000 - pygame.time.get_ticks()) // 60000) + ":" +
                                   str((90000 - pygame.time.get_ticks()) // 1000 % 60).zfill(2), True, (0, 0, 0))
    textRect = survivedtext.get_rect()
    textRect.topright = [635, 5]
    screen.blit(survivedtext, textRect)
    # 画出城堡健康值
    # 首先画了一个全红色的生命值条。然后根据城堡的生命值往生命条里面添加绿色。
    screen.blit(health_bar, (5, 5))
    for health1 in range(healthvalue):
        screen.blit(health, (health1 + 8, 8))
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
    #判断
    if pygame.time.get_ticks() >= 90000:
        running = False
        exitcode = True
    if healthvalue <= 0:
        running = False
        exitcode = False
    if account[1] != 0:
        accuracy = (account[1]/account[0])*100
        accuracy = ("%.2f" % accuracy)
    else:
        accuracy = 0

if exitcode == False:
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Accuracy: " + str(accuracy) + "%", True, (255, 0, 0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery + 24
    screen.blit(gameover_img, (0, 0))
    screen.blit(text, textRect)
else:
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Accuracy: " + str(accuracy) + "%", True, (0, 255, 0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery + 24
    screen.blit(youwin_img, (0, 0))
    screen.blit(text, textRect)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.flip()