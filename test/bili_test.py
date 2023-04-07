import websocket
import json
import time
from threading import Timer

def on_message(ws, message):
    # Handle incoming message here
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("Connection closed")

def on_open(ws):
    # Send authentication message to server
    roomid = 6136246,  # Replace with the ID of the live room you want to join
    def encode(self,roomid):
        a = '{"roomid":' + str(roomid) + '}'
        data = []
        for s in a:
            data.append(ord(s))
        return "000000{}001000010000000700000001".format(hex(16 + len(data))[2:]) + "".join(
            map(lambda x: x[2:], map(hex, data)))
    
    auth_message = json.dumps(encode(roomid)).encode("utf-8")
    ws.send(auth_message)

    # Start heartbeat timer
    def send_heartbeat():
        heartbeat_data = {
            "cmd": "heartbeat",
            "ts": int(time.time() * 1000),
        }
        heartbeat_message = json.dumps(heartbeat_data).encode("utf-8")
        ws.send(heartbeat_message)

        # Schedule next heartbeat
        heartbeat_interval = 30  # Heartbeat every 30 seconds
        heartbeat_timer = Timer(heartbeat_interval, send_heartbeat)
        heartbeat_timer.start()

    # Start first heartbeat
    send_heartbeat()

if __name__ == "__main__":
    # Set up WebSocket connection
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
        "wss://broadcastlv.chat.bilibili.com/sub",
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
    )
    ws.on_open = on_open

    # Start WebSocket connection
    ws.run_forever()