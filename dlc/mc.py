
import tkinter

import customtkinter

import module.minecraft_server as minecraft_server

class PageMC:
    def __init__(self,page):
        self.page = page
        
        global max_memory_entry, min_memory_entry, version_combobox
        server = minecraft_server.MinecraftServer()
        version_label = customtkinter.CTkLabel(self.page, text="服务器版本：", font=('Microsoft YaHei', 12))
        version_label.place(relx=0.1, rely=0.05)
        version_combobox = customtkinter.CTkComboBox(self.page,values=server.server_version_list)
        version_combobox.set(server.server_version_list[-1])
        version_combobox.place(relx=0.3, rely=0.05)
        
        build_label = customtkinter.CTkLabel(self.page, text="版本构建(留空自动最新)：", font=('Microsoft YaHei', 12))
        build_label.place(relx=0.1, rely=0.15)
        build_entry = customtkinter.CTkEntry(self.page, width=150, font=('Microsoft YaHei', 12))
        build_entry.insert(0, '') 
        build_entry.place(relx=0.5, rely=0.15)

        max_memory_label = customtkinter.CTkLabel(self.page, text="最大内存：", font=('Microsoft YaHei', 12))
        max_memory_label.place(relx=0.1, rely=0.25)
        max_memory_entry = customtkinter.CTkEntry(self.page, width=200, font=('Microsoft YaHei', 12))
        max_memory_entry.insert(0, '4G') 
        max_memory_entry.place(relx=0.3, rely=0.25)

        min_memory_label = customtkinter.CTkLabel(self.page, text="最小内存：", font=('Microsoft YaHei', 12))
        min_memory_label.place(relx=0.1, rely=0.35)
        min_memory_entry = customtkinter.CTkEntry(self.page, width=200, font=('Microsoft YaHei', 12))
        min_memory_entry.insert(0, '2G') 
        min_memory_entry.place(relx=0.3, rely=0.35)

        status_label = customtkinter.CTkLabel(self.page, text="", font=('Microsoft YaHei', 12))
        status_label.place(relx=0.1, rely=0.45)

        install_button = customtkinter.CTkButton(self.page, text='安装服务器', font=('Microsoft YaHei', 12), command=lambda: self.minecraft_server_install(file_folder="minecraft/server", server_version=version_combobox.get(), server_build=build_entry.get(), status_label=status_label))
        install_button.place(relx=0.1, rely=0.55)

        start_button = customtkinter.CTkButton(self.page, text='启动服务器', font=('Microsoft YaHei', 12), command=lambda: self.minecraft_server_start(file_folder="minecraft/server", server_version=version_combobox.get(), max_memory=max_memory_entry.get(), min_memory=min_memory_entry.get(), log_text=log_text, ))
        start_button.place(relx=0.55, rely=0.55)

        log_text = tkinter.Text(self.page, width=48, height=7, state="disabled")
        log_text.place(relx=0.1, rely=0.65)
    
    def minecraft_server_install(self,file_folder, server_version, server_build, status_label):
        global server
        status_label.configure(text="服务器安装中")
        server = minecraft_server.MinecraftServer(server_version=server_version, server_build=server_build)
        server.install_server()
        status_label.configure(text="服务器安装成功")

    def minecraft_server_start(self, file_folder, server_version, max_memory, min_memory, log_text, output_label=None):
        global server
        server = minecraft_server.MinecraftServer(file_folder=file_folder, server_version=server_version)

        server.start_server(max_memory=max_memory, min_memory=min_memory, output_label=log_text)

        if server.server_status == "未安装":
            log_text.config(state="normal")
            log_text.insert(tkinter.END, "服务器未安装，请先安装服务器\n")
            log_text.config(state="disabled")
            return