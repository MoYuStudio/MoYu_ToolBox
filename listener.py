
from pynput import mouse, keyboard

import json_driver

class 记录器:
    def __init__(self):
        self.正在记录 = False
        self.输入事件 = []

    def on_move(self, x, y):#on_move=self.on_move, 
        if self.正在记录:
            self.输入事件.append(['鼠标移动', x, y])

    def on_click(self, x, y, button, pressed):
        if self.正在记录:
            action = '键盘按下' if pressed else '键盘释放'
            self.输入事件.append(['鼠标点击', x, y, str(button), action])

    def on_scroll(self, x, y, dx, dy):
        if self.正在记录:
            self.输入事件.append(['鼠标滚动', x, y, dx, dy])

    def on_press(self, key):
        if self.正在记录:
            try:
                char = key.char
            except AttributeError:
                char = None
            self.输入事件.append(['键盘按下', str(key), char])

    def on_release(self, key):
        if self.正在记录:
            try:
                char = key.char
            except AttributeError:
                char = None
            self.输入事件.append(['键盘释放', str(key), char])

    def on_key_press(self, key):
        try:
            if key == keyboard.Key.f12:
                if not self.正在记录:
                    print('开始记录')
                    self.输入事件.clear()
                    self.正在记录 = True
                else:
                    print('停止记录')
                    self.正在记录 = False
                    写入数据 = {'输入事件':self.输入事件}
                    json_driver.json文件写入('user.json',写入数据)
                    
        except AttributeError:
            pass

    def 开始(self):
        with mouse.Listener(on_click=self.on_click, on_scroll=self.on_scroll) as m_listener, keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as k_listener, keyboard.Listener(on_press=self.on_key_press) as f_listener:
            m_listener.join()
            k_listener.join()
            f_listener.join()

if __name__ == '__main__':
    记录器 = 记录器()
    记录器.开始()
