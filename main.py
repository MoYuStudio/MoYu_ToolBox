
# === MoYuToolBox 摸鱼工具箱 ===
#   Develop BY WilsonVinson      
# pyinstaller --onefile --windowed --icon=icon/icon.ico main.py

import sys
import datetime
import threading
import webbrowser
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox

from PIL import Image, ImageTk
from ttkbootstrap import Style
import pyautogui

import module.json_driver as json_driver
import module.recorder as recorder
import module.executor as executor
import module.minecraft_server as minecraft_server

run = True

def open_website():
    url = "https://space.bilibili.com/103589775"
    webbrowser.open(url)

def start_recording(recorder_obj, status_label_var):
    global threading1
    threading1 = threading.Thread(target=recorder_obj.run)
    threading1.start()
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
    json_driver.json_write(f'data/json/{file_name}.json', data)
    status_label_var.set('就绪')

def start_execution(status_label_var, file_name_entry):
    global threading2
    file_name = file_name_entry.get()
    if not file_name:
        file_name = 'user'
    data = json_driver.json_read(f'data/json/{file_name}.json')
    loop_count = loop_var.get()
    executor_obj = executor.Executor(data, loop_count)
    threading2 = threading.Thread(target=executor_obj.run())
    threading2.start()
    status_label_var.set('执行中')
    try:
        threading2.join()
        status_label_var.set('就绪')
    except Exception as e:
        print(f"Error: {e}")
        status_label_var.set('发生错误')

def clear_records(recorder_obj):
    recorder_obj.events.clear()
    
def minecraft_server_install(file_folder, server_version,server_build,status_label,):
    global server
    status_label.config(text="服务器安装中")
    server = minecraft_server.MinecraftServer(server_version=server_version,server_build=server_build)
    server.install_server()
    status_label.config(text="服务器安装成功")
    
def minecraft_server_start(file_folder, server_version, max_memory, min_memory, log_text, output_label=None):
    global server
    server = minecraft_server.MinecraftServer(file_folder=file_folder, server_version=server_version)
        
    server.start_server(max_memory=max_memory, min_memory=min_memory, output_label=log_text)

    if server.server_status == "未安装":
        log_text.config(state="normal")
        log_text.insert(END, "服务器未安装，请先安装服务器\n")
        log_text.config(state="disabled")
        return
    
def on_closing():
    global run
    root.destroy()
    run = False
    try:
        threading1.join()
    except:
        pass
    try:
        threading2.join()
    except:
        pass

if __name__ == '__main__':
    
    while run:
    
        recorder_obj = recorder.Recorder()
        
        # root = tk.Tk()
        style = Style(theme='darkly')# python -m ttkbootstrap
        root = style.master
        
        notebook = ttk.Notebook(root)
        
        page_home = tk.Frame(notebook)
        page_auto = tk.Frame(notebook)
        page_mc = tk.Frame(notebook)
        page_download = tk.Frame(notebook)
        page_setting = tk.Frame(notebook)
        page_about = tk.Frame(notebook)
        
        custom_font_0 = font.Font(family='黑体', size=12)#, weight='bold'
        custom_font_1 = font.Font(family='黑体', size=9)
        custom_font_2 = font.Font(family='黑体', size=24)
        
        image_file = Image.open("data/icon/icon_x500.png")
        tk_image = ImageTk.PhotoImage(image_file)
        
        root.title('MoYu ToolBox 摸鱼工具箱')
        root.iconbitmap("data/icon/icon.ico")
        root.geometry("600x600")
        root.resizable(False, False)
        root.configure(bg='#F0F0F0')
        root.attributes("-alpha", 0.95)
        
        notebook.add(page_home, text="主页")
        notebook.add(page_auto, text="自动化")
        notebook.add(page_mc, text="MC")
        notebook.add(page_download, text="下载")
        notebook.add(page_setting, text="设置")
        notebook.add(page_about, text="关于")
        notebook.place(x=0, y=0)
        
        def page_home_group():
            moyu_button = Button(page_home, text='一键摸鱼',width=15, height=2, font=custom_font_2, command=open_website)
            moyu_button.place(x=100, y=200)
        
        def page_auto_group():
            global loop_var
            
            status_label_var = StringVar()
            status_label_var.set('就绪')
            status_label = Label(page_auto, textvariable=status_label_var, bd=1, relief=SUNKEN, anchor=W, font=custom_font_0)
            status_label.place(x=500, y=100)
            
            file_name_label = Label(page_auto, text='输入文件名:', font=custom_font_0)
            file_name_label.place(x=25, y=150)
            file_name_label.config(bg=page_auto['bg'])
            
            file_name_entry = Entry(page_auto, width=24)
            file_name_entry.insert(0, 'user') 
            file_name_entry.place(x=300, y=150)

            record_button = Button(page_auto, text='开始记录',width=15, height=2, font=custom_font_0, command=lambda: start_recording(recorder_obj, status_label_var))
            record_button.place(x=25, y=200)

            stop_button = Button(page_auto, text='结束记录',width=15, height=2, font=custom_font_0, command=lambda: stop_recording(recorder_obj, status_label_var, file_name_entry))
            stop_button.place(x=300, y=200)
            
            loop_label = Label(page_auto, text='循环次数(-1无限循环):', font=custom_font_0)
            loop_label.place(x=25, y=290)
            loop_label.config(bg=page_auto['bg'])

            loop_var = IntVar(value=1)
            loop_spinbox = Spinbox(page_auto, from_=-1, to=1000, width=21, font=custom_font_0, textvariable=loop_var)
            loop_spinbox.place(x=300, y=290)

            execute_button = Button(page_auto, text='开始执行',width=15, height=2, font=custom_font_0, command=lambda: start_execution(status_label_var,file_name_entry))
            execute_button.place(x=25, y=350)

            clear_button = Button(page_auto, text='清空记录',width=15, height=2, font=custom_font_0, command=lambda: clear_records(recorder_obj))
            clear_button.place(x=300, y=350)

        def page_mc_group():
            global max_memory_entry, min_memory_entry, version_entry

            version_label = Label(page_mc, text="服务器版本(留空自动最新)：", font=custom_font_1)
            version_label.place(x=25, y=25)
            version_entry = Entry(page_mc, width=20, font=custom_font_0)
            version_entry.insert(0, '') 
            version_entry.place(x=280, y=25)
            
            build_label = Label(page_mc, text="版本构建(留空自动最新)：", font=custom_font_1)
            build_label.place(x=25, y=75)
            build_entry = Entry(page_mc, width=20, font=custom_font_0)
            build_entry.insert(0, '') 
            build_entry.place(x=280, y=75)

            max_memory_label = Label(page_mc, text="最大内存：", font=custom_font_1)
            max_memory_label.place(x=25, y=150)
            max_memory_entry = Entry(page_mc, width=20, font=custom_font_0)
            max_memory_entry.insert(0, '4G') 
            max_memory_entry.place(x=150, y=150)

            min_memory_label = Label(page_mc, text="最小内存：", font=custom_font_1)
            min_memory_label.place(x=25, y=200)
            min_memory_entry = Entry(page_mc, width=20, font=custom_font_0)
            min_memory_entry.insert(0, '2G') 
            min_memory_entry.place(x=150, y=200)

            status_label = Label(page_mc, text="", font=custom_font_0)
            status_label.place(x=25, y=250)

            install_button = Button(page_mc, text='安装服务器', width=15, height=2, font=custom_font_0, command=lambda: minecraft_server_install(file_folder="minecraft/server", server_version=version_entry.get(),server_build=build_entry.get(), status_label=status_label))
            install_button.place(x=25, y=250)

            start_button = Button(page_mc, text='启动服务器', width=15, height=2, font=custom_font_0, command=lambda: minecraft_server_start(file_folder="minecraft/server", server_version=version_entry.get(),max_memory=max_memory_entry.get(), min_memory=min_memory_entry.get(), log_text=log_text, ))

            start_button.place(x=250, y=250)
            
            log_text = Text(page_mc, width=48, height=7, state="disabled")
            log_text.place(x=25, y=350)

        def page_about_group():
            icon_label = tk.Label(page_about, image=tk_image)
            icon_label.place(x=250, y=100)
            icon_label.config(bg=page_about['bg'])
            
            title_label = Label(page_about, text='MoYu ToolBox', font=custom_font_2)
            title_label.place(x=150, y=250)
            title_label.config(bg=page_about['bg'])
            
            copyright_label = Label(page_about, text='Powered BY ChatGPT   Developed BY WilsonVinson', font=custom_font_1)
            copyright_label.place(x=100, y=500)
            copyright_label.config(bg=page_about['bg'])
        
        page_home_group()
        page_auto_group()
        page_mc_group()
        page_about_group()
        
        notebook.pack(expand=True, fill="both")

        root.protocol("WM_DELETE_WINDOW", on_closing)

        root.mainloop()

    sys.exit(0)
