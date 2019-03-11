# coding: utf-8
# 定义音符酱类(Define Pikachu Class)
import cocos
import os

class eight_note(cocos.sprite.Sprite):
    def __init__(self):
        super(eight_note,self).__init__('resources/eight_note.png')
        # 是否可以跳跃
        self.can_jump = False
        # 速度
        self.speed = 0
        #锚点
        self.image_anchor = 0, 0
        #音符酱的位置
        self.position = 80, 280
        self.scheduled(self.update)
    # #声控跳跃
    # def jump(self, h):
    #
    # #重力下落
    # def fall(self, y):
    #
    # #着陆静止
    # def stay(self, dt):
    #
    # #重置
    # def reset(self):