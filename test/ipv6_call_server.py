import socket
import threading

def receive_data(sock):
    while True:
        try:
            data = sock.recv(1024).decode('utf-8')
            print(data)
        except:
            break

def send_data(sock):
    while True:
        data = input()
        sock.send(data.encode('utf-8'))

def start_chat():
    # create socket and connect to server
    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    server_addr = ('2001:db8::1', 12345)
    sock.connect(server_addr)

    # start receiving and sending threads
    receive_thread = threading.Thread(target=receive_data, args=(sock,))
    receive_thread.start()

    send_thread = threading.Thread(target=send_data, args=(sock,))
    send_thread.start()

if __name__ == '__main__':
    start_chat()