
# === The Imitation Game 模仿游戏 ===
#      Develop BY WilsonVinson       

import sys
import threading
from tkinter import *

import keyboard

import json_driver
import listener
import bin.clicker as clicker

设置配置路径 = 'setting.json'
输入存档路径 = 'user.json'

def on_hotkey_pressed():
    print('Ctrl+C pressed')
    keyboard.unhook_all()
    
def 记录器按钮():
    记录器 = listener.记录器(True)
    记录器.运行()
    
def 记录器子子线程():
    子线程 = threading.Thread(target=记录器按钮)
    子线程.start()

窗口 = Tk()
窗口.title("AutoClicker")
窗口.geometry("600x600")

label = Label(窗口, text='记录器')
button = Button(窗口, text='开始',command=记录器子子线程)
#entry = Entry(窗口, width=50)

label.pack()
button.pack()
#entry.pack()

窗口.mainloop()

# while True:
#     键 = keyboard.read_event()
    
#     keyboard.add_hotkey('ctrl+c', on_hotkey_pressed)
    
#     if 键.event_type == keyboard.KEY_DOWN:
#        print(键.name)
#        if 键.name == 'f12':
#            记录器 = listener.记录器()
#            记录器.运行()
                
#        if 键.name == 'a': 
#            数据 = json_driver.json文件读取(输入存档路径)
#            执行器 = clicker.执行器(数据)
#            执行器.运行()

sys.exit(0)