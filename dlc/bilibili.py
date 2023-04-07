
import asyncio
import threading

import customtkinter

import module.bilibili_live as bilibili_live

class PageBiliBili:
    def __init__(self,page):
        self.page = page
        
        self.roomid_label = customtkinter.CTkLabel(self.page, text="房间号：", font=('Microsoft YaHei', 16))
        self.roomid_label.place(relx=0.1, rely=0.05)
        self.roomid_entry = customtkinter.CTkEntry(self.page, width=200, font=('Microsoft YaHei', 16))
        # self.roomid_entry.insert(0, '7193936') 
        self.roomid_entry.place(relx=0.3, rely=0.05)
        
        # self.tts_engine_label = customtkinter.CTkLabel(self.page, text="TTS引擎：", font=('Microsoft YaHei', 12))
        # self.tts_engine_label.place(relx=0.1, rely=0.15)
        # self.tts_engine_combobox = customtkinter.CTkComboBox(self.page,values=['pyttsx3', 'google'])
        # self.tts_engine_combobox.set('pyttsx3')
        # self.tts_engine_combobox.place(relx=0.3, rely=0.15)

        self.open_button = customtkinter.CTkButton(self.page, text='开启', font=('Microsoft YaHei', 16), command=lambda: self.bilibili_thread_start())
        self.open_button.place(relx=0.1, rely=0.6)

        self.close_button = customtkinter.CTkButton(self.page, text='关闭', font=('Microsoft YaHei', 16), command=lambda: self.bilibili_thread_stop())
        self.close_button.place(relx=0.55, rely=0.6)
    
    def bilibili_thread_start(self):
        global bilibili_danmu, bilibili_thread
        bilibili_danmu = bilibili_live.BilibiliLive(roomid=self.roomid_entry.get())
        bilibili_thread = threading.Thread(target=asyncio.run, args=(bilibili_danmu.run(),))
        bilibili_thread.start()

    def bilibili_thread_stop(self):
        bilibili_thread.cancel()
        bilibili_thread.join()
        