
import time

import pyautogui

class Executor:
    def __init__(self, input_events,loop_count=1):
        self.input_events = input_events
        self.loop_count = loop_count
        self.timer = 0

    def run(self):
        while self.loop_count != 0:
            for event_id in range(0,len(self.input_events['input_event'])-2):
                event = self.input_events['input_event'][event_id]
                if event[0] == 'mouse_move':
                    x, y = event[1], event[2]
                    try:
                        delay = event[3] - self.input_events['input_event'][event_id-1][3]
                        time.sleep(max(0, delay))
                    except:
                        pass
                    pyautogui.moveTo(x, y)
                elif event[0] == 'mouse_click':
                    x, y = event[1], event[2]
                    button = str(event[3])
                    action = event[4]
                    try:
                        delay = event[5] - self.input_events['input_event'][event_id-1][5]
                        time.sleep(max(0, delay))
                    except:
                        pass
                    if button == 'Button.left':
                        if action == 'mouse_press':
                            pyautogui.mouseDown(x, y, button='left')
                        else:
                            pyautogui.mouseUp(x, y, button='left')
                    elif button == 'Button.right':
                        if action == 'mouse_press':
                            pyautogui.mouseDown(x, y, button='right')
                        else:
                            pyautogui.mouseUp(x, y, button='right')
                elif event[0] == 'mouse_scroll':
                    dx, dy = event[3], event[4]
                    try:
                        delay = event[5] - self.input_events['input_event'][event_id-1][5]
                        time.sleep(max(0, delay))
                    except:
                        pass
                    if dx>0 or dy>0:
                        pyautogui.scroll(x=dx, y=dy, clicks=1)
                        pyautogui.scroll(x=dx, y=dy, clicks=1)
                        pyautogui.scroll(x=dx, y=dy, clicks=1)
                    else:
                        pyautogui.scroll(x=dx, y=dy, clicks=-1)
                        pyautogui.scroll(x=dx, y=dy, clicks=-1)
                        pyautogui.scroll(x=dx, y=dy, clicks=-1)
                elif event[0] == 'keyboard_press':
                    key = event[2] if event[2] is not None else event[1]
                    if key == 'Key.space':
                        key = 'space'
                    if key == "Key.backspace":
                        key = 'backspace'
                    try:
                        delay = event[3] - self.input_events['input_event'][event_id-1][3]
                        time.sleep(max(0, delay))
                    except:
                        pass
                    pyautogui.press(key)
                elif event[0] == 'keyboard_release':
                    pass
            if self.loop_count > 0:
                self.loop_count -= 1