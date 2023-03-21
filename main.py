
# === AutoClicker 自动点击器 ===

import os
import sys
import json
import subprocess

import pyautogui
import keyboard

运行 = True
鼠标监听器开关 = False

json文件路径 = 'setting.json'

process = None

def json文件读取(json文件路径):
    with open(json文件路径) as 文件:
        数据 = json.load(文件)
    return 数据

def json文件写入(json文件路径,写入数据):
    with open(json文件路径, 'w') as 文件:
        json.dump(写入数据, 文件)

def 键盘输入(输入事件):
    print(输入事件.name)
    if 输入事件.name == 'f12':
        sys.exit(0)
    if 输入事件.name == 'f10':
        process = subprocess.Popen(["python", "mouse_listener.py"])
    if 输入事件.name == 'a':
        try:
            process.terminate()
            if process.poll() is None:
                os.kill(process.pid, 9)
        except:
            pass

def 键盘释放(输入事件):
    print("键盘按键", 输入事件.name, "被释放")

while 运行:
    keyboard.on_press(键盘输入)
    keyboard.wait()
    
sys.exit(0)