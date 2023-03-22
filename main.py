
# === The Imitation Game 模仿游戏 ===

import sys

import keyboard

import json_driver
import listener
import clicker

json文件路径 = 'setting.json'

print(' === The Imitation Game 模仿游戏 === ')
print('      Develop BY WilsonVinson       ')
print('')
print('           按下F12 开始学习           ')
print('            按下1 开始模仿            ')
print('')

while True:
    key = keyboard.read_event()
    
    if key.event_type == keyboard.KEY_DOWN:
        if key.name == 'f12': 
            记录器 = listener.记录器()
            记录器.运行()
        if key.name == 'a':
            print('run')
            数据 = json_driver.json文件读取('user.json')
            执行器 = clicker.执行器(数据)
            执行器.运行()

sys.exit(0)