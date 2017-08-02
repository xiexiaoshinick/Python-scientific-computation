# coding=utf-8
from visual import *
keys = label()  # 用于显示文字的标签
while True: 
    if scene.kb.keys: # 如果有按键按下
        s = scene.kb.getkey()  # 获得按键信息
        keys.text += s + "," 
        print s