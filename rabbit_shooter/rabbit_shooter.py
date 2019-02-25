#导入pygame库
import pygame
from pygame.locals import *

#初始化pygame
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

#加载射手
rabbit_shoot = pygame.image.load("resources/images/dude.png")
#加载草地
grass = pygame.image.load("resources/images/grass.png")
#加载兔子窝
rabbit_castle = pygame.image.load("resources/images/castle.png")
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
    # 添加兔子射手
    screen.blit(rabbit_shoot, rabbit_pos)
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
        #移动兔子（按住一直动）
        if  event.type == pygame.KEYDOWN:
            if event.key == K_w:
                key_press[0] = True
            if event.key == K_s:
                key_press[1] = True
            if event.key == K_a:
                key_press[2] = True
            if event.key == K_d:
                key_press[3] = True
        if event.type == pygame.KEYUP:
            if event.key == K_w:
                key_press[0] = False
            if event.key == K_s:
                key_press[1] = False
            if event.key == K_a:
                key_press[2] = False
            if event.key == K_d:
                key_press[3] = False

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
