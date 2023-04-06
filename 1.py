import asyncio
import json
import zlib

import websockets


async def onmessage(ws):
    while True:
        greeting = await ws.recv()
        decode(greeting)


async def sendHB(ws):
    while True:
        await asyncio.sleep(30)
        await ws.send(bytes.fromhex(hb))


def decode(data):
    packetLen = int(data[:4].hex(), 16)
    ver = int(data[6:8].hex(), 16)
    op = int(data[8:12].hex(), 16)

    if len(data) > packetLen:  # 防止
        decode(data[packetLen:])
        data = data[:packetLen]

    if ver == 2:
        data = zlib.decompress(data[16:])
        decode(data)
        return

    if op == 5:
        try:
            jd = json.loads(data[16:].decode('utf-8', errors='ignore'))
            if jd['cmd'] == 'DANMU_MSG':  # 普通弹幕消息
                print(jd['info'][2][1], ': ', jd['info'][1])
            elif jd['cmd'] == 'SUPER_CHAT_MESSAGE_JPN':  # sc醒目提醒
                print(jd["data"]["user_info"]["uname"],
                      ":", jd["data"]["message"])
            elif jd['cmd'] == 'SEND_GIFT':  # 礼物
                print(jd["data"]["uname"],
                      ":", jd["data"]["giftName"], "X", jd["data"]["num"])
        except Exception as e:
            pass


def encode(roomid):
    a = '{"roomid":' + str(roomid) + '}'
    data = []
    for s in a:
        data.append(ord(s))
    return "000000{}001000010000000700000001".format(hex(16 + len(data))[2:]) + "".join(
        map(lambda x: x[2:], map(hex, data)))


async def main():
    roomid = 22117557
    uri = "wss://broadcastlv.chat.bilibili.com/sub"
    data_raw = bytes.fromhex(encode(roomid))
    async with websockets.connect(uri) as websocket:
        await websocket.send(data_raw)

        tasks = [asyncio.create_task(
            sendHB(websocket)), asyncio.create_task(onmessage(websocket))]
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    hb = "00000010001000010000000200000001"
    asyncio.run(main())
