
import os
import time
import json
import requests
import pyttsx3
import threading
from gtts import gTTS
from io import BytesIO
import pygame

class BilibiliLive:
    def __init__(self, roomid=7193936, sleep_time=1):
        self.roomid = roomid
        self.sleep_time = sleep_time
        self.url = f"https://api.live.bilibili.com/xlive/web-room/v1/dM/gethistory?roomid={roomid}"
        
        self.danmuhistory = []
        self.gifts = []
        self.last_timestamp = ''
        self.stop_thread = False
        
        self.tts_engine = 'pyttsx3' # ['pyttsx3', 'google']
        
        self.pyttsx3_engine = pyttsx3.init()
        self.pyttsx3_engine.setProperty('voice', 1)
        self.pyttsx3_engine.setProperty('rate', 230)
        self.pyttsx3_engine.setProperty('volume', 0.8)
        
        self.google_language = 'zh-CN' #'zh-CN' 'zh-TW'
        self.google_slow_audio_speed = False
        pygame.mixer.init()
        

    def show(self, danmulist):
        for i in range(len(danmulist)):
            print('[{0}] {1} : {2}'.format(danmulist[i]['timeline'], danmulist[i]['nickname'], danmulist[i]['text']))
            
            if self.tts_engine ==  'pyttsx3':
                self.pyttsx3_engine.say(danmulist[i]['nickname'] + '说：' + danmulist[i]['text'])
                self.pyttsx3_engine.runAndWait()

            if self.tts_engine == 'google':

                google_tts_audio = gTTS(text=' '+danmulist[i]['nickname'] + '说：' + danmulist[i]['text'], lang=self.google_language, slow=self.google_slow_audio_speed)

                audio_stream = BytesIO()
                google_tts_audio.write_to_fp(audio_stream)
                audio_stream.seek(0)

                # 加载音频流
                pygame.mixer.music.load(audio_stream)

                # 播放音频文件
                pygame.mixer.music.play()

                # 等待音频播放结束
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)

    def fetch_danmu(self):
        r = requests.get(self.url)
        message = json.loads(r.text)
        return message['data']['room']
    
    def fetch_gifts(self):
        url = f"https://api.live.bilibili.com/gift/v2/live/receive_record?roomid={self.roomid}&page=1"
        r = requests.get(url)
        data = r.json()
        if data["code"] == 0:
            return data["data"]["list"]
        else:
            return []

    def run(self):
        initial_danmu = self.fetch_danmu()
        if len(initial_danmu) > 0:
            self.danmuhistory += initial_danmu
            self.last_timestamp = self.danmuhistory[-1]['timeline']

        while not self.stop_thread:
            os.system("cls")
            danmu_new = self.fetch_danmu()

            if len(self.danmuhistory) == 0:
                if len(danmu_new) == 1:
                    self.danmuhistory += danmu_new
                    self.show(self.danmuhistory)
                time.sleep(self.sleep_time)
                continue

            new_danmaku_list = []
            for i in range(len(danmu_new)):
                if danmu_new[i]['timeline'] > self.last_timestamp:
                    new_danmaku_list.append(danmu_new[i])

            if new_danmaku_list:
                self.last_timestamp = new_danmaku_list[-1]['timeline']
                self.danmuhistory += new_danmaku_list
                self.show(new_danmaku_list)
                
            new_gifts = self.fetch_gifts()
            for gift in new_gifts:
                if gift not in self.gifts:
                    self.gifts.append(gift)
                    thank_msg = f"{gift['uname']} 赠送了 {gift['num']} 个 {gift['gift_name']}，感谢支持！"
                    self.engine.say(thank_msg)
                    self.engine.runAndWait()

            time.sleep(self.sleep_time)

if __name__ == "__main__":
    roomid = 7193936
    bilibili_danmu = BilibiliLive(roomid)
    danmu_thread = threading.Thread(target=bilibili_danmu.run)
    danmu_thread.start()
    
