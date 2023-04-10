
import asyncio
import json
import zlib
import threading

import websockets
import pyttsx3

class BilibiliLive:
    def __init__(self,roomid):
        self.roomid = roomid
        self.uri = "wss://broadcastlv.chat.bilibili.com/sub"
        self.data_raw = bytes.fromhex(self.encode(self.roomid))
        self.stop_event = threading.Event()
        
        self.tts_engine_voice = 1
        self.tts_engine_rate = 180
        self.tts_engine_volume = 5
        
    async def onmessage(self,ws):
        while True:
            greeting = await ws.recv()
            self.decode(greeting)


    async def sendHB(self,ws):
        hb = "00000010001000010000000200000001"
        while True:
            await asyncio.sleep(30)
            await ws.send(bytes.fromhex(hb))


    def decode(self,data):
        packetLen = int(data[:4].hex(), 16)
        ver = int(data[6:8].hex(), 16)
        op = int(data[8:12].hex(), 16)

        if len(data) > packetLen:  # 防止
            self.decode(data[packetLen:])
            data = data[:packetLen]

        if ver == 2:
            data = zlib.decompress(data[16:])
            self.decode(data)
            return

        if op == 5:
            try:
                jd = json.loads(data[16:].decode('utf-8', errors='ignore'))
                
                if jd['cmd'] == 'SEND_GIFT':  # 礼物
                    print(str(jd["data"]["uname"]) + ": " + str(jd["data"]["giftName"]) + "X" + str(jd["data"]["num"]))
                    self.pyttsx3_engine.say("感谢" + str(jd["data"]["uname"]) + "赠送了" + str(jd["data"]["num"]) + "个" + str(jd["data"]["giftName"]))
                    self.pyttsx3_engine.runAndWait()
                    
                elif jd['cmd'] == 'SUPER_CHAT_MESSAGE_JPN':  # sc醒目提醒
                    print(str(jd["data"]["user_info"]["uname"]) + ": " + str(jd["data"]["message"]))
                    self.pyttsx3_engine.say("SC留言" + str(jd["data"]["user_info"]["uname"]) + "说:" + str(jd["data"]["message"]))
                    self.pyttsx3_engine.runAndWait()
                
                elif jd['cmd'] == 'DANMU_MSG':  # 普通弹幕消息
                    print(str(jd['info'][2][1]) + ": " + str(jd['info'][1]))
                    self.pyttsx3_engine.say(str(jd['info'][2][1]) + "说" + str(jd['info'][1]))
                    self.pyttsx3_engine.runAndWait()
                
            except Exception as e:
                pass


    def encode(self,roomid):
        a = '{"roomid":' + str(roomid) + '}'
        data = []
        for s in a:
            data.append(ord(s))
        return "000000{}001000010000000700000001".format(hex(16 + len(data))[2:]) + "".join(
            map(lambda x: x[2:], map(hex, data)))


    async def run(self):
        self.pyttsx3_engine = pyttsx3.init()
        self.pyttsx3_engine.setProperty('voice', self.tts_engine_voice)
        self.pyttsx3_engine.setProperty('rate', self.tts_engine_rate)
        self.pyttsx3_engine.setProperty('volume', self.tts_engine_volume)
        self.pyttsx3_engine.say(' 欢迎使用摸鱼工具箱 哔哩哔哩弹幕姬 ')
        self.pyttsx3_engine.runAndWait()
        
        async with websockets.connect(self.uri) as websocket:
            await websocket.send(self.data_raw)

            self.tasks = [
                asyncio.create_task(self.sendHB(websocket)),
                asyncio.create_task(self.onmessage(websocket)),
            ]

            while not self.stop_event.is_set():
                await asyncio.sleep(1)

            # stop the tasks
            for task in self.tasks:
                task.cancel()

            # wait for the tasks to finish
            await asyncio.gather(*self.tasks, return_exceptions=True)

        self.pyttsx3_engine.stop()

    def _run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            loop.run_until_complete(self.run())
        finally:
            loop.run_until_complete(loop.shutdown_asyncgens())
            loop.close()

    def start(self):
        self.thread = threading.Thread(target=self._run)
        self.thread.start()

    def stop(self):
        self.stop_event.set()

if __name__ == '__main__':

    roomid = 7193936
    bilibili_danmu = BilibiliLive(roomid)
    asyncio.create_task(bilibili_danmu.run())