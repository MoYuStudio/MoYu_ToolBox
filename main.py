
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

def start_recording(recorder_obj, status_label_var):
    recorder_obj.recording = True
    recorder_obj.events.clear()
    recorder_obj.start_time = datetime.datetime.now()
    status_label_var.set('记录中')

def stop_recording(recorder_obj, status_label_var, file_name_entry):
    recorder_obj.recording = False
    file_name = file_name_entry.get()
    if not file_name:
        file_name = 'user'
    data = {'input_event': recorder_obj.events}
    json_driver.json_write(f'data/{file_name}.json', data)
    status_label_var.set('就绪')

def start_execution(executor_obj, status_label_var):
    threading2 = threading.Thread(target=executor_obj.run)
    threading2.start()
    status_label_var.set('执行中')

def clear_records(recorder_obj):
    recorder_obj.events.clear()

if __name__ == '__main__':
    
    recorder_obj = recorder.Recorder()
    threading1 = threading.Thread(target=recorder_obj.run)
    threading1.start()
    
    try:
        data = json_driver.json_read('data/user.json')
    except:
        json_driver.json_write(f'data/user.json', {'input_event': []})
        data = json_driver.json_read('data/user.json')
    executor_obj = executor.Executor(data)
    
    root = tk.Tk()
    root.title('AutoClicker')
    # root.geometry("300x200")

    screen_width, screen_height = pyautogui.size()
        
    label1 = Label(root, text=('屏幕分辨率 '+str(screen_width)+'x'+str(screen_height)))
    label1.grid(row=0,column=0)
    
    status_label_var = StringVar()
    status_label_var.set('就绪')
    status_label = Label(root, textvariable=status_label_var, bd=1, relief=SUNKEN, anchor=W)
    status_label.grid(row=0,column=1)
    
    file_name_label = Label(root, text='输入文件名（可选）:')
    file_name_label.grid(row=1,column=0)
    
    file_name_entry = Entry(root, width=10)
    file_name_entry.grid(row=1,column=1)

    record_button = tk.Button(root, text='开始记录', command=lambda: start_recording(recorder_obj, status_label_var))
    record_button.grid(row=2,column=0)

    stop_button = tk.Button(root, text='结束记录', command=lambda: stop_recording(recorder_obj, status_label_var, file_name_entry))
    stop_button.grid(row=2,column=1)

    execute_button = tk.Button(root, text='开始执行', command=lambda: start_execution(executor_obj, status_label_var))
    execute_button.grid(row=3,column=0)

    clear_button = tk.Button(root, text='清空记录', command=lambda: clear_records(recorder_obj))
    clear_button.grid(row=3,column=1)
    
    copyright_label = Label(root, text='Develop BY WilsonVinson  ')
    copyright_label.grid(row=4,column=0)

    root.mainloop()

    sys.exit(0)
