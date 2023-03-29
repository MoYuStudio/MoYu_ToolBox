
import os
import time
import json
import requests
import pyttsx3
import threading

class BilibiliLive:
    def __init__(self, roomid=7193936, sleep_time=1):
        self.roomid = roomid
        self.sleep_time = sleep_time
        self.url = f"https://api.live.bilibili.com/xlive/web-room/v1/dM/gethistory?roomid={roomid}"
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', 1)
        self.engine.setProperty('rate', 230)
        self.engine.setProperty('volume', 0.8)
        self.danmuhistory = []
        self.last_timestamp = ''
        self.stop_thread = False

    def show(self, danmulist):
        for i in range(len(danmulist)):
            print('[{0}] {1} : {2}'.format(danmulist[i]['timeline'], danmulist[i]['nickname'], danmulist[i]['text']))
            self.engine.say(danmulist[i]['nickname'] + '说：' + danmulist[i]['text'])
            self.engine.runAndWait()

    def fetch_danmu(self):
        r = requests.get(self.url)
        message = json.loads(r.text)
        return message['data']['room']

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

            time.sleep(self.sleep_time)

if __name__ == "__main__":
    roomid = 7193936
    bilibili_danmu = BilibiliLive(roomid)
    danmu_thread = threading.Thread(target=bilibili_danmu.run)
    danmu_thread.start()
    
