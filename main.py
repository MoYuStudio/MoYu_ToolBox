
# === The Imitation Game 模仿游戏 ===

import sys

import pyautogui
import keyboard

import json_driver
import listener

json文件路径 = 'setting.json'

print(' === The Imitation Game 模仿游戏 === ')
print('      Develop BY WilsonVinson       ')
print('')
print('           按下F12 开始学习           ')
print('            按下1 开始模仿            ')
print('')

while True:
    # 检测按键并阻塞，直到按键被按下
    key = keyboard.read_event()
    
    # 检查是否为按下事件
    if key.event_type == keyboard.KEY_DOWN:
        if key.name == 'f12':
            记录器 = listener.记录器()
            记录器.开始()
        if key.name == 'a':
            print('run')

sys.exit(0)