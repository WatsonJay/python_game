# coding: utf-8
import cocos
import os
import struct
from pyaudio import PyAudio, paInt16
from cocos.sprite import Sprite
from classes.block import Block
from classes.eight_note import eight_note

# 定义八分音符酱游戏
# eight note run Class
class eight_note_game(cocos.layer.ColorLayer):
    def __init__(self):
        #初始化窗体（R ,G ,B ,Light ,Width, Height）
        super(eight_note_game, self).__init__(255, 255, 255, 255, 800, 600)
        # 初始化参数
        # frames_per_buffer
        self.numSamples = 1000
        #音量条
        self.vbar = Sprite("resources/black.png")
        self.vbar.position = 50, 450
        self.vbar.scale_y = 0.1
        self.vbar.image_anchor = 0, 0
        self.add(self.vbar)
        # 音量示数
        self.label = cocos.text.Label(
            '音量：',
            font_name='Times New Roman', #字体样式
            font_size=10, #字体大小
            color=(0, 0, 0, 255), #字体颜色
            anchor_x='center', anchor_y='center' #字体位置
        )
        self.label.position = 30, 455
        self.add(self.label)

        #输入声音
        audio = PyAudio()
        SampleRate = int(audio.get_default_input_device_info()['defaultSampleRate'])#读取默认的速率
        self.stream = audio.open(
            format=paInt16,
            channels=1,
            input=True,
            rate=SampleRate,
            frames_per_buffer=self.numSamples)

        #创建八分音符酱

        #创建地板

        #游戏主循环
        self.schedule(self.loop)


    # 碰撞检测
    # def collide(self):

    #游戏循环定义
    def loop(self, dt):
        #获取玩家的音量
        audio_data = self.stream.read(self.numSamples)
        length = len(audio_data)
        k= max(struct.unpack('%dh' % (length//2), audio_data))
        if k<0:
            voice_level = 0
        else:
            voice_level = k
        self.vbar.scale_x = voice_level / 10000.0

if __name__ == '__main__':
	cocos.director.director.init(caption="八分音符酱~~")
	cocos.director.director.run(cocos.scene.Scene(eight_note_game()))