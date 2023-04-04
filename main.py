
# === MoYuToolBox 摸鱼工具箱 ===
#   Develop BY WilsonVinson      
# pyinstaller --onefile --windowed --icon=data/icon/icon.ico main.py
# pyinstaller --noconfirm --onedir --windowed --icon=data/icon/icon.ico --add-data "C:\Users\WilsonVinson\AppData\Local\Programs\Python\Python311\Lib\site-packages/customtkinter;customtkinter/"  "main.py"
# https://www.lfd.uci.edu/~gohlke/pythonlibs
# pip install -r requirements.txt

import os
import sys
import time
import datetime
import threading
import webbrowser
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox

from PIL import Image, ImageTk
import customtkinter
import pyautogui
import pystray

import module.json_driver as json_driver
import module.autoinput_recorder as autoinput_recorder
import module.autoinput_executor as autoinput_executor
import module.minecraft_server as minecraft_server
import module.bilibili_live as bilibili_live

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        # 设置样式
        style = ttk.Style()
        style.configure("TNotebook", borderwidth=0, padding=0)

        # configure window
        self.title("MoYu ToolBox 摸鱼工具箱")
        self.iconbitmap("data/icon/icon.ico")
        self.geometry(f"{600}x{400}")

        # 配置网格布局 (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # 创建带有小部件的侧边栏框架
        self.sidebar_frame = customtkinter.CTkFrame(self, width=100, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=9, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(9, weight=1)
        self.sidebar_frame.lift()
        
        # 添加小部件到侧边栏框架
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="MoYu ToolBox", font=customtkinter.CTkFont('Microsoft YaHei', size=24, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="主页", font=customtkinter.CTkFont('Microsoft YaHei', size=16, weight="bold"), command=lambda: self.notebook.select(self.page_home))
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="自动化", font=customtkinter.CTkFont('Microsoft YaHei', size=16, weight="bold"), command=lambda: self.notebook.select(self.page_auto))
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="MC", font=customtkinter.CTkFont('Microsoft YaHei', size=16, weight="bold"), command=lambda: self.notebook.select(self.page_mc))
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, text="小破站", font=customtkinter.CTkFont('Microsoft YaHei', size=16, weight="bold"), command=lambda: self.notebook.select(self.page_bilibili))
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        self.sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame, text="设置", font=customtkinter.CTkFont('Microsoft YaHei', size=16, weight="bold"), command=lambda: self.notebook.select(self.page_setting))
        self.sidebar_button_5.grid(row=5, column=0, padx=20, pady=10)
        self.sidebar_button_6 = customtkinter.CTkButton(self.sidebar_frame, text="关于", font=customtkinter.CTkFont('Microsoft YaHei', size=16, weight="bold"), command=lambda: self.notebook.select(self.page_about))
        self.sidebar_button_6.grid(row=6, column=0, padx=20, pady=10)
        
        # # 创建页面
        # self.notebook = ttk.Notebook(self, style="HiddenTab")
        # self.notebook.grid(row=0, column=1, rowspan=9, columnspan=3, sticky="nsew")
        
        # 创建 Notebook
        self.notebook = ttk.Notebook(self)
        self.notebook_style = ttk.Style()
        self.notebook_style.configure("TNotebook", background="transparent")
        self.notebook.lower()
                
        self.page_home = tkinter.Frame(self.notebook, highlightthickness=0)
        self.page_auto = tkinter.Frame(self.notebook, highlightthickness=0)
        self.page_mc = tkinter.Frame(self.notebook, highlightthickness=0)
        self.page_bilibili = tkinter.Frame(self.notebook, highlightthickness=0)
        self.page_download = tkinter.Frame(self.notebook, highlightthickness=0)
        self.page_setting = tkinter.Frame(self.notebook, highlightthickness=0)
        self.page_about = tkinter.Frame(self.notebook, highlightthickness=0)
        
        self.notebook.add(self.page_home, text="主页")
        self.notebook.add(self.page_auto, text="自动化")
        self.notebook.add(self.page_mc, text="MC")
        self.notebook.add(self.page_bilibili, text="小破站")
        self.notebook.add(self.page_download, text="下载")
        self.notebook.add(self.page_setting, text="设置")
        self.notebook.add(self.page_about, text="关于")
        self.notebook.select(self.page_home)

        self.notebook.place(x=325, y=-32)
        
        self.page_home_group()
        self.page_auto_group()
        self.page_mc_group()
        self.page_bilibili_group()
        self.page_setting_group()
        self.page_about_group()
        
        self.notebook_color = '#1b1c22'
        self.page_home.configure(bg=self.notebook_color)
        self.page_auto.configure(bg=self.notebook_color)
        self.page_mc.configure(bg=self.notebook_color)
        self.page_bilibili.configure(bg=self.notebook_color)
        self.page_setting.configure(bg=self.notebook_color)
        self.page_about.configure(bg=self.notebook_color)
        
        # 绑定窗口大小变化的事件
        self.bind("<Configure>", self.on_window_resize)

    def on_window_resize(self, event):
        # 计算Notebook的新大小
        self.window_width = int(self.winfo_width())
        self.window_height = int(self.winfo_height())
        # 设置Notebook的新大小
        self.notebook.config(width=self.window_width-325, height=self.window_height+32)

    def page_home_group(self):
        def open_website():
            url = "https://space.bilibili.com/103589775"
            webbrowser.open(url)
            
        moyu_button = customtkinter.CTkButton(self.page_home, text='一键摸鱼',font=('Microsoft YaHei', 32), command=open_website)
        moyu_button.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
    
    def page_auto_group(self):
        
        recorder_obj = autoinput_recorder.Recorder()
        
        # create tabview
        tabview = customtkinter.CTkTabview(self.page_auto, width=350, height=350)
        tabview.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

        tabview.add("自动输入")
        tabview.add("链式启动")
        
        def page_auto_input_group():
            def start_recording(recorder_obj, status_label_var):
                global auto_input_thread
                auto_input_thread = threading.Thread(target=recorder_obj.run)
                auto_input_thread.start()
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
                global auto_input_thread
                file_name = file_name_entry.get()
                if not file_name:
                    file_name = 'user'
                data = json_driver.json_read(f'data/json/{file_name}.json')
                loop_count = loop_var.get()
                executor_obj = autoinput_executor.Executor(data, loop_count)
                auto_input_thread = threading.Thread(target=executor_obj.run())
                auto_input_thread.start()
                status_label_var.set('执行中')
                try:
                    auto_input_thread.join()
                    status_label_var.set('就绪')
                except Exception as e:
                    print(f"Error: {e}")
                    status_label_var.set('发生错误')

            def clear_records(recorder_obj):
                recorder_obj.events.clear()

            global loop_var
            status_label_var = StringVar()
            status_label_var.set('就绪')
            status_label = customtkinter.CTkLabel(master=tabview.tab("自动输入"), textvariable=status_label_var, anchor=W, font=('Microsoft YaHei', 12))
            status_label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

            file_name_label = customtkinter.CTkLabel(master=tabview.tab("自动输入"), text='输入文件名:', font=('Microsoft YaHei', 12))
            file_name_label.place(relx=0.1, rely=0.2, anchor=tkinter.W)
            # file_name_label.config(bg=page_auto_input['bg'])

            file_name_entry = customtkinter.CTkEntry(master=tabview.tab("自动输入"), width=200)
            file_name_entry.insert(0, 'user') 
            file_name_entry.place(relx=0.65, rely=0.2, anchor=tkinter.CENTER)

            record_button = customtkinter.CTkButton(master=tabview.tab("自动输入"), text='开始记录', font=('Microsoft YaHei', 12), command=lambda: start_recording(recorder_obj, status_label_var))
            record_button.place(relx=0.25, rely=0.4, anchor=tkinter.CENTER)

            stop_button = customtkinter.CTkButton(master=tabview.tab("自动输入"), text='结束记录', font=('Microsoft YaHei', 12), command=lambda: stop_recording(recorder_obj, status_label_var, file_name_entry))
            stop_button.place(relx=0.75, rely=0.4, anchor=tkinter.CENTER)
            
            loop_label = customtkinter.CTkLabel(master=tabview.tab("自动输入"), text='循环次数(-1无限循环):', font=('Microsoft YaHei', 12))
            loop_label.place(relx=0.1, rely=0.5)

            loop_var = IntVar(value=1)
            loop_spinbox = customtkinter.CTkEntry(master=tabview.tab("自动输入"), width=150, font=('Microsoft YaHei', 12), textvariable=loop_var)
            loop_spinbox.place(relx=0.5, rely=0.5)

            execute_button = customtkinter.CTkButton(master=tabview.tab("自动输入"), text='开始执行', font=('Microsoft YaHei', 12), command=lambda: start_execution(status_label_var,file_name_entry))
            execute_button.place(relx=0.25, rely=0.7, anchor=tkinter.CENTER)

            clear_button = customtkinter.CTkButton(master=tabview.tab("自动输入"), text='清空记录', font=('Microsoft YaHei', 12), command=lambda: clear_records(recorder_obj))
            clear_button.place(relx=0.75, rely=0.7, anchor=tkinter.CENTER)
        
        def page_auto_launch_group():
            def open_folder():
                folder_path = f'{os.getcwd()}/data/auto_launch'
                os.startfile(folder_path)
            def open():
                folder_path = f'{os.getcwd()}/data/auto_launch'
                for file in os.listdir(folder_path):
                    file_path = os.path.join(folder_path, file)
                    os.startfile(file_path)
                            
            info_label = customtkinter.CTkLabel(master=tabview.tab("链式启动"), text='把快捷方式放入文件夹在需要时一键打开', font=('Microsoft YaHei', 16))
            info_label.place(relx=0.05, rely=0.1, anchor=tkinter.W)
            
            open_folder_button = customtkinter.CTkButton(master=tabview.tab("链式启动"), text='打开文件夹', font=('Microsoft YaHei', 12), command=lambda: open_folder())
            open_folder_button.place(relx=0.05, rely=0.3)
            
            open_button = customtkinter.CTkButton(master=tabview.tab("链式启动"), text='打开文件', font=('Microsoft YaHei', 12), command=lambda: open())
            open_button.place(relx=0.55, rely=0.3)
        
        page_auto_input_group()
        page_auto_launch_group()

    def page_mc_group(self):
        def minecraft_server_install(file_folder, server_version, server_build, status_label):
            global server
            status_label.configure(text="服务器安装中")
            server = minecraft_server.MinecraftServer(server_version=server_version, server_build=server_build)
            server.install_server()
            status_label.configure(text="服务器安装成功")

        def minecraft_server_start(file_folder, server_version, max_memory, min_memory, log_text, output_label=None):
            global server
            server = minecraft_server.MinecraftServer(file_folder=file_folder, server_version=server_version)

            server.start_server(max_memory=max_memory, min_memory=min_memory, output_label=log_text)

            if server.server_status == "未安装":
                log_text.config(state="normal")
                log_text.insert(END, "服务器未安装，请先安装服务器\n")
                log_text.config(state="disabled")
                return
            
        global max_memory_entry, min_memory_entry, version_combobox
        server = minecraft_server.MinecraftServer()
        version_label = customtkinter.CTkLabel(self.page_mc, text="服务器版本：", font=('Microsoft YaHei', 12))
        version_label.place(relx=0.1, rely=0.05)
        version_combobox = customtkinter.CTkComboBox(self.page_mc,values=server.server_version_list)
        version_combobox.set(server.server_version_list[-1])
        version_combobox.place(relx=0.3, rely=0.05)
        
        build_label = customtkinter.CTkLabel(self.page_mc, text="版本构建(留空自动最新)：", font=('Microsoft YaHei', 12))
        build_label.place(relx=0.1, rely=0.15)
        build_entry = customtkinter.CTkEntry(self.page_mc, width=150, font=('Microsoft YaHei', 12))
        build_entry.insert(0, '') 
        build_entry.place(relx=0.5, rely=0.15)

        max_memory_label = customtkinter.CTkLabel(self.page_mc, text="最大内存：", font=('Microsoft YaHei', 12))
        max_memory_label.place(relx=0.1, rely=0.25)
        max_memory_entry = customtkinter.CTkEntry(self.page_mc, width=200, font=('Microsoft YaHei', 12))
        max_memory_entry.insert(0, '4G') 
        max_memory_entry.place(relx=0.3, rely=0.25)

        min_memory_label = customtkinter.CTkLabel(self.page_mc, text="最小内存：", font=('Microsoft YaHei', 12))
        min_memory_label.place(relx=0.1, rely=0.35)
        min_memory_entry = customtkinter.CTkEntry(self.page_mc, width=200, font=('Microsoft YaHei', 12))
        min_memory_entry.insert(0, '2G') 
        min_memory_entry.place(relx=0.3, rely=0.35)

        status_label = customtkinter.CTkLabel(self.page_mc, text="", font=('Microsoft YaHei', 12))
        status_label.place(relx=0.1, rely=0.45)

        install_button = customtkinter.CTkButton(self.page_mc, text='安装服务器', font=('Microsoft YaHei', 12), command=lambda: minecraft_server_install(file_folder="minecraft/server", server_version=version_combobox.get(), server_build=build_entry.get(), status_label=status_label))
        install_button.place(relx=0.1, rely=0.55)

        start_button = customtkinter.CTkButton(self.page_mc, text='启动服务器', font=('Microsoft YaHei', 12), command=lambda: minecraft_server_start(file_folder="minecraft/server", server_version=version_combobox.get(), max_memory=max_memory_entry.get(), min_memory=min_memory_entry.get(), log_text=log_text, ))
        start_button.place(relx=0.55, rely=0.55)

        log_text = Text(self.page_mc, width=48, height=7, state="disabled")
        log_text.place(relx=0.1, rely=0.65)

    def page_bilibili_group(self):
        
        def bilibili_thread_start():
            global bilibili_danmu
            bilibili_danmu = bilibili_live.BilibiliLive(roomid=roomid_entry.get())
            bilibili_danmu.tts_engine = tts_engine_combobox.get()
            bilibili_thread = threading.Thread(target=bilibili_danmu.run, daemon=True)
            bilibili_thread.start()

        def bilibili_thread_stop():
            bilibili_danmu.stop_thread = True
            
        roomid_label = customtkinter.CTkLabel(self.page_bilibili, text="房间号：", font=('Microsoft YaHei', 16))
        roomid_label.place(relx=0.1, rely=0.05)
        roomid_entry = customtkinter.CTkEntry(self.page_bilibili, width=200, font=('Microsoft YaHei', 16))
        roomid_entry.insert(0, '7193936') 
        roomid_entry.place(relx=0.3, rely=0.05)
        
        tts_engine_label = customtkinter.CTkLabel(self.page_bilibili, text="TTS引擎：", font=('Microsoft YaHei', 12))
        tts_engine_label.place(relx=0.1, rely=0.15)
        tts_engine_combobox = customtkinter.CTkComboBox(self.page_bilibili,values=['pyttsx3', 'google'])
        tts_engine_combobox.set('pyttsx3')
        tts_engine_combobox.place(relx=0.3, rely=0.15)

        open_button = customtkinter.CTkButton(self.page_bilibili, text='开启', font=('Microsoft YaHei', 16), command=lambda: bilibili_thread_start())
        open_button.place(relx=0.1, rely=0.6)

        close_button = customtkinter.CTkButton(self.page_bilibili, text='关闭', font=('Microsoft YaHei', 16), command=lambda: bilibili_thread_stop())
        close_button.place(relx=0.55, rely=0.6)

    def page_setting_group(self):
        def change_appearance_mode_event(new_appearance_mode: str):
            customtkinter.set_appearance_mode(new_appearance_mode)
        def change_scaling_event(new_scaling: str):
            new_scaling_float = int(new_scaling.replace("%", "")) / 100
            customtkinter.set_widget_scaling(new_scaling_float)
            
        appearance_mode_label = customtkinter.CTkLabel(self.page_setting, text="主题(目前有BUG):", font=('Microsoft YaHei', 16), anchor="w")
        appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.page_setting, values=["Light", "Dark", "System"],
                                                                       command=change_appearance_mode_event)
        appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        scaling_label = customtkinter.CTkLabel(self.page_setting, text="UI比例(目前有BUG):", font=('Microsoft YaHei', 16), anchor="w")
        scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        scaling_optionemenu = customtkinter.CTkOptionMenu(self.page_setting, values=["80%", "90%", "100%", "110%", "120%"],
                                                          command=change_scaling_event)
        scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

    def page_about_group(self):
        
        about_frame = customtkinter.CTkFrame(self.page_about)
        about_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        image_file = Image.open("data/icon/icon_x500.png")
        tk_image = ImageTk.PhotoImage(image_file)
        icon_label = customtkinter.CTkLabel(about_frame, text='',image=tk_image)
        icon_label.pack()
        
        title_label = customtkinter.CTkLabel(about_frame, text='MoYu ToolBox', font=('Microsoft YaHei', 32))
        title_label.pack()
        
        copyright_label = customtkinter.CTkLabel(about_frame, text='Powered BY ChatGPT   Developed BY WilsonVinson', font=('Microsoft YaHei', 10))
        copyright_label.pack()

    
if __name__ == "__main__":
    app = App()
    app.mainloop()
