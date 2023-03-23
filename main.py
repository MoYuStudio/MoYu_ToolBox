
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
from PIL import Image, ImageTk

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

def start_execution(status_label_var):
    file_name = file_name_entry.get()
    if not file_name:
        file_name = 'user'
    data = json_driver.json_read(f'data/{file_name}.json')
    executor_obj = executor.Executor(data)
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
    
    # root = tk.Tk()
    style = Style(theme='minty')# python -m ttkbootstrap
    root = style.master
    
    root.title('AutoClicker 自动点击器')
    root.iconbitmap("icon.ico")
    root.geometry("600x600")
    root.resizable(False, False)
    root.configure(bg='#F0F0F0')
    root.attributes("-alpha", 0.95)
    
    custom_font_0 = font.Font(family='黑体', size=12)#, weight='bold'
    custom_font_1 = font.Font(family='黑体', size=9)
    custom_font_2 = font.Font(family='黑体', size=24)

    screen_width, screen_height = pyautogui.size()
    
    image_file = Image.open("icon_x500.png")
    tk_image = ImageTk.PhotoImage(image_file)
    icon_label = tk.Label(root, image=tk_image)
    icon_label.place(x=5, y=5)
    icon_label.config(bg=root['bg'])
    
    title_label = Label(root, text='AutoClick 自动点击器', font=custom_font_2)
    title_label.place(x=95, y=25)
    title_label.config(bg=root['bg'])
        
    label1 = Label(root, text=('屏幕分辨率 '+str(screen_width)+'x'+str(screen_height)), font=custom_font_0)
    label1.place(x=25, y=100)
    label1.config(bg=root['bg'])
    
    status_label_var = StringVar()
    status_label_var.set('就绪')
    status_label = Label(root, textvariable=status_label_var, bd=1, relief=SUNKEN, anchor=W, font=custom_font_0)
    status_label.place(x=500, y=100)
    
    file_name_label = Label(root, text='输入文件名（可选）:', font=custom_font_0)
    file_name_label.place(x=25, y=150)
    file_name_label.config(bg=root['bg'])
    
    file_name_entry = Entry(root, width=26)
    file_name_entry.place(x=270, y=150)

    record_button = Button(root, text='开始记录',width=15, height=2, font=custom_font_0, command=lambda: start_recording(recorder_obj, status_label_var))
    record_button.place(x=25, y=200)

    stop_button = Button(root, text='结束记录',width=15, height=2, font=custom_font_0, command=lambda: stop_recording(recorder_obj, status_label_var, file_name_entry))
    stop_button.place(x=300, y=200)

    execute_button = Button(root, text='开始执行',width=15, height=2, font=custom_font_0, command=lambda: start_execution(status_label_var))
    execute_button.place(x=25, y=300)

    clear_button = Button(root, text='清空记录',width=15, height=2, font=custom_font_0, command=lambda: clear_records(recorder_obj))
    clear_button.place(x=300, y=300)
    
    copyright_label = Label(root, text='Power BY ChatGPT   Develop BY WilsonVinson', font=custom_font_1)
    copyright_label.place(x=100, y=560)
    copyright_label.config(bg=root['bg'])

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

    sys.exit(0)
