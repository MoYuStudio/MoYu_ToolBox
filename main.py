
# ===         AutoClick          ===
# === The Imitation Game 模仿游戏 ===
#      Develop BY WilsonVinson       

import sys
import datetime
import threading
import tkinter as tk
from tkinter import *

import pyautogui

import module.json_driver as json_driver
import module.recorder as recorder
import module.executor as executor

def start_recording(recorder_obj):
    recorder_obj.recording = True
    recorder_obj.events.clear()
    recorder_obj.start_time = datetime.datetime.now()

def stop_recording(recorder_obj):
    recorder_obj.recording = False
    data = {'input_event': recorder_obj.events}
    json_driver.json_write('user.json', data)
    
def start_execution(executor_obj):
    threading2 = threading.Thread(target=executor_obj.run)
    threading2.start()

if __name__ == '__main__':
    
    recorder_obj = recorder.Recorder()
    threading1 = threading.Thread(target=recorder_obj.run)
    threading1.start()
    
    data = json_driver.json_read('data/user.json')
    executor_obj = executor.Executor(data)
    
    root = tk.Tk()
    root.title('AutoClicker')
    root.geometry("600x300")
    
    screen_width, screen_height = pyautogui.size()
        
    label1 = Label(root, text=('屏幕分辨率 '+str(screen_width)+'x'+str(screen_height)))
    label1.pack()
    
    button1 = tk.Button(root, text='开始记录', command=lambda: start_recording(recorder_obj))
    button1.pack()

    button2 = tk.Button(root, text='结束记录', command=lambda: stop_recording(recorder_obj))
    button2.pack()
    
    button3 = tk.Button(root, text='开始执行', command=lambda: start_execution(executor_obj))
    button3.pack()
    
    root.mainloop()
    
    sys.exit(0)

