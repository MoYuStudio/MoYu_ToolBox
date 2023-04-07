
import asyncio
import threading

import customtkinter

import module.bilibili_live as bilibili_live
import module.thread_plus as thread_plus

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
        self.tts_engine_rate_entry.insert(0, '230') 
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
    
    def bilibili_thread_start(self):
        self.bilibili_danmu = bilibili_live.BilibiliLive(roomid=self.roomid_entry.get())
        self.bilibili_danmu.tts_engine_voice = self.tts_engine_voice_entry.get()
        self.bilibili_danmu.tts_engine_rate = self.tts_engine_rate_entry.get()
        self.bilibili_danmu.tts_engine_volume = self.tts_engine_volume_entry.get()
        self.bilibili_thread = thread_plus.ThreadPlus(target=asyncio.run, args=(self.bilibili_danmu.run(),))
        self.bilibili_thread.start()

    def bilibili_thread_stop(self):
        if self.bilibili_thread:
            self.bilibili_thread.stop()
            # bilibili_thread.join()
            self.bilibili_thread = None

        # Get the running event loop
        loop = asyncio.get_event_loop()

        # Stop all running tasks
        tasks = asyncio.all_tasks(loop=loop)
        for task in tasks:
            task.cancel()

        # Run the event loop until all tasks are canceled
        loop.run_until_complete(asyncio.gather(*tasks, return_exceptions=True))

        # Stop the event loop
        loop.stop()
        loop.close()

