
# === The Imitation Game 模仿游戏 ===

import sys

import keyboard

import json_driver
import listener
import clicker

设置配置路径 = 'setting.json'
输入存档路径 = 'user.json'

print(' === The Imitation Game 模仿游戏 === ')
print('      Develop BY WilsonVinson       ')
print('')
print('           按下F12 开始学习           ')
print('            按下a 开始模仿            ')
print('')

while True:
    键 = keyboard.read_event()
    
    if 键.event_type == keyboard.KEY_DOWN:
        if 键.name == 'f12': 
            记录器 = listener.记录器()
            记录器.运行()
        if 键.name == 'a': 
            print('run')
            数据 = json_driver.json文件读取(输入存档路径)
            执行器 = clicker.执行器(数据)
            执行器.运行()

sys.exit(0)