
import datetime

from pynput import mouse, keyboard

import json_driver

class Recorder:
    def __init__(self):
        self.recording = False
        self.events = []
        self.start_time = None

    def on_move(self, x, y):
        if self.recording:
            elapsed_time = datetime.datetime.now() - self.start_time
            print(f"已记录 {elapsed_time.total_seconds()} 秒")
            self.events.append(['mouse_move', x, y, elapsed_time.total_seconds()])

    def on_click(self, x, y, button, pressed):
        if self.recording:
            elapsed_time = datetime.datetime.now() - self.start_time
            action = 'mouse_press' if pressed else 'mouse_release'
            self.events.append(['mouse_click', x, y, str(button), action, elapsed_time.total_seconds()])

    def on_scroll(self, x, y, dx, dy):
        if self.recording:
            elapsed_time = datetime.datetime.now() - self.start_time
            self.events.append(['mouse_scroll', x, y, dx, dy, elapsed_time.total_seconds()])

    def on_press(self, key):
        if self.recording:
            elapsed_time = datetime.datetime.now() - self.start_time
            try:
                char = key.char
            except AttributeError:
                char = None
            self.events.append(['keyboard_press', str(key), char, elapsed_time.total_seconds()])

    def on_release(self, key):
        if self.recording:
            elapsed_time = datetime.datetime.now() - self.start_time
            try:
                char = key.char
            except AttributeError:
                char = None
            self.events.append(['keyboard_release', str(key), char, elapsed_time.total_seconds()])

    def run(self):
        with mouse.Listener(on_click=self.on_click, on_scroll=self.on_scroll) as m_listener, \
             keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as k_listener:
            m_listener.join()
            k_listener.join()
