import socket
import struct
import threading

# 弹幕服务器地址
danmu_server = ('broadcastlv.chat.bilibili.com', 2244)

# 发送心跳包线程
class SendHeartBeat(threading.Thread):
    def __init__(self, sock, payload, interval):
        threading.Thread.__init__(self)
        self._sock = sock
        self._payload = payload
        self._interval = interval
        self._stopped = False

    def run(self):
        while not self._stopped:
            self._sock.send(self._payload)
            threading.Event().wait(self._interval)

    def stop(self):
        self._stopped = True


# 解析弹幕消息
def parse_danmu(data):
    if len(data) < 16:
        return
    msg_length, msg_type, _, _, _, msg = struct.unpack('!IHHII', data[:16]) + (data[16:],)
    if msg_type == 5:
        print(f'[弹幕] {msg.decode("utf-8")}')
    elif msg_type == 8:
        print(f'[礼物] {msg.decode("utf-8")}')

# 连接弹幕服务器
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(danmu_server)

    # 发送认证信息
    auth_payload = '0000001c001000010000000200000000'.encode('utf-8')
    sock.send(struct.pack('!I', len(auth_payload)) + auth_payload)

    # 发送加入房间消息
    room_id = 7193936 # 直播间 ID
    join_room_payload = f'0000001c00100001000000070000000{{"roomid":{room_id}}}'.encode('utf-8')
    sock.send(struct.pack('!I', len(join_room_payload)) + join_room_payload)

    # 发送心跳包
    heartbeat_payload = '00000010001000010000000200000001'.encode('utf-8')
    heartbeat_thread = SendHeartBeat(sock, heartbeat_payload, 30)
    heartbeat_thread.start()

    # 接收数据
    while True:
        try:
            data = sock.recv(4096)
            if not data:
                break
            if data[:4] == b'\x00\x00\x00\x0c':  # 收到心跳回应
                continue
            parse_danmu(data)
        except Exception as e:
            print(f'Error: {e}')
            break

    # 停止心跳包线程
    heartbeat_thread.stop()
    heartbeat_thread.join()
