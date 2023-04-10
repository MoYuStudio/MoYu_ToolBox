
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
        
        self.tts_engine_voice_label = customtkinter.CTkLabel(self.page, text="音效：", font=('Microsoft YaHei', 12))
        self.tts_engine_voice_label.place(relx=0.1, rely=0.15)
        self.tts_engine_voice_entry = customtkinter.CTkEntry(self.page, width=100, font=('Microsoft YaHei', 16))
        self.tts_engine_voice_entry.insert(0, '1') 
        self.tts_engine_voice_entry.place(relx=0.3, rely=0.15)
        
        self.tts_engine_rate_label = customtkinter.CTkLabel(self.page, text="音调：", font=('Microsoft YaHei', 12))
        self.tts_engine_rate_label.place(relx=0.1, rely=0.25)
        self.tts_engine_rate_entry = customtkinter.CTkEntry(self.page, width=100, font=('Microsoft YaHei', 16))
        self.tts_engine_rate_entry.insert(0, '180') 
        self.tts_engine_rate_entry.place(relx=0.3, rely=0.25)
        
        self.tts_engine_volume_label = customtkinter.CTkLabel(self.page, text="音量：", font=('Microsoft YaHei', 12))
        self.tts_engine_volume_label.place(relx=0.1, rely=0.35)
        self.tts_engine_volume_entry = customtkinter.CTkEntry(self.page, width=100, font=('Microsoft YaHei', 16))
        self.tts_engine_volume_entry.insert(0, '5') 
        self.tts_engine_volume_entry.place(relx=0.3, rely=0.35)

        self.open_button = customtkinter.CTkButton(self.page, text='开启', font=('Microsoft YaHei', 16), command=lambda: self.bilibili_thread_start())
        self.open_button.place(relx=0.1, rely=0.6)

        self.close_button = customtkinter.CTkButton(self.page, text='关闭', font=('Microsoft YaHei', 16), command=lambda: self.bilibili_thread_stop())
        self.close_button.place(relx=0.55, rely=0.6)
        
    def bilibili_thread(self):
        
        self.bilibili_danmu.start()
        
    def bilibili_thread_start(self):
        self.bilibili_danmu = bilibili_live.BilibiliLive(roomid=self.roomid_entry.get())
        self.bilibili_danmu.tts_engine_voice = self.tts_engine_voice_entry.get()
        self.bilibili_danmu.tts_engine_rate = self.tts_engine_rate_entry.get()
        self.bilibili_danmu.tts_engine_volume = self.tts_engine_volume_entry.get()
        
        self.threading = threading.Thread(target=self.bilibili_thread)
        self.threading.start()

    def bilibili_thread_stop(self):
        if hasattr(self, 'bilibili_danmu'):
            self.bilibili_danmu.stop_event.set()
        if hasattr(self, 'threading'):
            self.threading.join()