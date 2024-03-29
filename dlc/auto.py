
import os
import datetime
import threading
import tkinter

import customtkinter

import module.json_driver as json_driver
import module.autoinput_recorder as autoinput_recorder
import module.autoinput_executor as autoinput_executor

class PageAuto:
    def __init__(self,page):
        self.page = page
        
        self.recorder_obj = autoinput_recorder.Recorder()
        
        self.folder_path = "data/json"  # Replace this with the path to your folder
        
        self.tabview = customtkinter.CTkTabview(self.page, width=550, height=350)
        self.tabview.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.tabview.add("自动输入")
        self.tabview.add("链式启动")
        
        self.auto_input_group()
        self.auto_launch_group()
    
    def auto_input_group(self):

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
        status_label_var = tkinter.StringVar()
        status_label_var.set('就绪')
        
        status_label = customtkinter.CTkLabel(master=self.tabview.tab("自动输入"), textvariable=status_label_var, font=('Microsoft YaHei', 12))
        status_label.place(relx=0.15, rely=0.05, anchor=tkinter.CENTER)
        
        file_name_label = customtkinter.CTkLabel(master=self.tabview.tab("自动输入"), text='创建新文件:', font=('Microsoft YaHei', 14))
        file_name_label.place(relx=0.1, rely=0.15, anchor=tkinter.W)
        # file_name_label.config(bg=page_auto_input['bg'])
        
        file_name_entry = customtkinter.CTkEntry(master=self.tabview.tab("自动输入"), width=200, placeholder_text='不创建或不覆盖则留空')
        # file_name_entry.insert(0, '请输入文件名')
        file_name_entry.place(relx=0.45, rely=0.15, anchor=tkinter.CENTER)
        
        file_label = customtkinter.CTkLabel(master=self.tabview.tab("自动输入"), text="选择已有的文件：", font=('Microsoft YaHei', 14))
        file_label.place(relx=0.1, rely=0.25)
        file_list = [os.path.splitext(file)[0] for file in os.listdir(self.folder_path) if file.endswith(".json")]
        file_combobox = customtkinter.CTkComboBox(master=self.tabview.tab("自动输入"),values=file_list)
        file_combobox.set(file_list[0])
        file_combobox.place(relx=0.35, rely=0.25)

        record_button = customtkinter.CTkButton(master=self.tabview.tab("自动输入"), text='开始记录', font=('Microsoft YaHei', 14), command=lambda: start_recording(self.recorder_obj, status_label_var))
        record_button.place(relx=0.25, rely=0.45, anchor=tkinter.CENTER)

        stop_button = customtkinter.CTkButton(master=self.tabview.tab("自动输入"), text='结束记录', font=('Microsoft YaHei', 14), command=lambda: stop_recording(self.recorder_obj, status_label_var, file_name_entry))
        stop_button.place(relx=0.55, rely=0.45, anchor=tkinter.CENTER)
        
        loop_label = customtkinter.CTkLabel(master=self.tabview.tab("自动输入"), text='循环次数(-1无限循环):', font=('Microsoft YaHei', 14))
        loop_label.place(relx=0.1, rely=0.55)

        loop_var = tkinter.IntVar(value=1)
        loop_spinbox = customtkinter.CTkEntry(master=self.tabview.tab("自动输入"), width=150, font=('Microsoft YaHei', 14), textvariable=loop_var)
        loop_spinbox.place(relx=0.4, rely=0.55)

        execute_button = customtkinter.CTkButton(master=self.tabview.tab("自动输入"), text='开始执行', font=('Microsoft YaHei', 14), command=lambda: start_execution(status_label_var,file_combobox))
        execute_button.place(relx=0.25, rely=0.75, anchor=tkinter.CENTER)

        clear_button = customtkinter.CTkButton(master=self.tabview.tab("自动输入"), text='清空记录', font=('Microsoft YaHei', 14), command=lambda: clear_records(self.recorder_obj))
        clear_button.place(relx=0.55, rely=0.75, anchor=tkinter.CENTER)
        
        self.page.columnconfigure(0, weight=1)
        self.page.rowconfigure(0, weight=1)
        
    def auto_launch_group(self):
        def open_folder():
            folder_path = f'{os.getcwd()}/data/auto_launch'
            os.startfile(folder_path)
        def open():
            folder_path = f'{os.getcwd()}/data/auto_launch'
            for file in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file)
                os.startfile(file_path)
                        
        info_label = customtkinter.CTkLabel(master=self.tabview.tab("链式启动"), text='把快捷方式放入文件夹在需要时一键打开', font=('Microsoft YaHei', 16))
        info_label.place(relx=0.05, rely=0.1, anchor=tkinter.W)
        
        open_folder_button = customtkinter.CTkButton(master=self.tabview.tab("链式启动"), text='打开文件夹', font=('Microsoft YaHei', 12), command=lambda: open_folder())
        open_folder_button.place(relx=0.05, rely=0.3)
        
        open_button = customtkinter.CTkButton(master=self.tabview.tab("链式启动"), text='打开文件', font=('Microsoft YaHei', 12), command=lambda: open())
        open_button.place(relx=0.55, rely=0.3)