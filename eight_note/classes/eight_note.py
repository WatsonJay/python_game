# coding: utf-8
# 定义音符酱类(Define Pikachu Class)
import cocos
import os

class eight_note(cocos.sprite.Sprite):
    def __init__(self):
        super(eight_note,self).__init__('resources/eight_note.png')
        # 是否可以跳跃
        self.can_jump = False
        self.on_land = False
        # 速度
        self.speed = 0
        #锚点
        self.image_anchor = 0, 0
        #音符酱的位置
        self.position = 80, 280
        self.schedule(self.fall)
    #声控跳跃
    def jump(self, height):
        if self.can_jump == True:
            self.can_jump = False
            self.on_land = False
            self.y += height
            self.speed = max(min(height/100, 5), 1)
    #重力下落
    def fall(self, dt):
        if self.on_land == False:
            self.speed += 10*dt
            self.y -= self.speed
            if self.y < -85:
                self.reset()
    #着陆静止
    def stay(self, height):
        self.can_jump = True
        self.on_land = True
        self.speed = 0
        self.y = height
    #重置
    def reset(self):
        self.parent.reset()
        self.able_jump = False
        self.speed = 0
        self.position = 80, 280