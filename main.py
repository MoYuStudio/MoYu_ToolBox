
# ===         AutoClick          ===
# === The Imitation Game 模仿游戏 ===
#      Develop BY WilsonVinson      

import sys
import datetime
import threading
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font
from ttkbootstrap import Style

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
    
def on_closing():
    root.destroy()

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
    
    # root = tk.Tk()
    style = Style(theme='minty')# python -m ttkbootstrap
    root = style.master
    
    root.title('AutoClicker')
    # root.geometry("300x200")
    
    custom_font_0 = font.Font(family='黑体', size=12)#, weight='bold'
    custom_font_1 = font.Font(family='黑体', size=7)

    screen_width, screen_height = pyautogui.size()
    
    title_label = Label(root, text='AutoClick 自动点击器', font=custom_font_0)
    title_label.grid(row=0,column=0)
        
    label1 = Label(root, text=('屏幕分辨率 '+str(screen_width)+'x'+str(screen_height)), font=custom_font_0)
    label1.grid(row=1,column=0)
    
    status_label_var = StringVar()
    status_label_var.set('就绪')
    status_label = Label(root, textvariable=status_label_var, bd=1, relief=SUNKEN, anchor=W, font=custom_font_0)
    status_label.grid(row=1,column=1)
    
    file_name_label = Label(root, text='输入文件名（可选）:', font=custom_font_0)
    file_name_label.grid(row=2,column=0)
    
    file_name_entry = Entry(root, width=10)
    file_name_entry.grid(row=2,column=1)

    record_button = tk.Button(root, text='开始记录', command=lambda: start_recording(recorder_obj, status_label_var), font=custom_font_0)
    record_button.grid(row=3,column=0)

    stop_button = tk.Button(root, text='结束记录', command=lambda: stop_recording(recorder_obj, status_label_var, file_name_entry), font=custom_font_0)
    stop_button.grid(row=3,column=1)

    execute_button = tk.Button(root, text='开始执行', command=lambda: start_execution(executor_obj, status_label_var), font=custom_font_0)
    execute_button.grid(row=4,column=0)

    clear_button = tk.Button(root, text='清空记录', command=lambda: clear_records(recorder_obj), font=custom_font_0)
    clear_button.grid(row=4,column=1)
    
    copyright_label = Label(root, text='Power BY ChatGPT   Develop BY WilsonVinson', font=custom_font_1)
    copyright_label.grid(row=5,column=0)

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

    sys.exit(0)
