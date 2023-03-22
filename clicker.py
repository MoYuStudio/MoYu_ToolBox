
import time

import pyautogui

class 执行器:
    def __init__(self, 输入事件):
        self.输入事件 = 输入事件

    def 运行(self):
        for 事件 in self.输入事件['输入事件']:
            if 事件[0] == '鼠标移动':
                x, y = 事件[1], 事件[2]
                delay = 事件[3] - (self.输入事件['输入事件'][0][3] if len(self.输入事件['输入事件']) > 0 else 0) # 计算与开始时间的时间差
                time.sleep(max(0, delay)) # 等待时间差
                pyautogui.moveTo(x, y)
            elif 事件[0] == '鼠标点击':
                x, y = 事件[1], 事件[2]
                button = str(事件[3])
                action = 事件[4]
                delay = 事件[5] - (self.输入事件['输入事件'][0][3] if len(self.输入事件['输入事件']) > 0 else 0) # 计算与开始时间的时间差
                time.sleep(max(0, delay)) # 等待时间差
                if button == 'Button.left':
                    if action == '鼠标按下':
                        pyautogui.mouseDown(x, y, button='left')
                    else:
                        pyautogui.mouseUp(x, y, button='left')
                elif button == 'Button.right':
                    if action == '鼠标按下':
                        pyautogui.mouseDown(x, y, button='right')
                    else:
                        pyautogui.mouseUp(x, y, button='right')
            elif 事件[0] == '鼠标滚动':
                dx, dy = 事件[3], 事件[4]
                delay = 事件[5] - (self.输入事件['输入事件'][0][3] if len(self.输入事件['输入事件']) > 0 else 0) # 计算与开始时间的时间差
                time.sleep(max(0, delay)) # 等待时间差
                pyautogui.scroll(dx, dy)
            elif 事件[0] == '键盘按下':
                key = 事件[2] if 事件[2] is not None else 事件[1]
                delay = 事件[3] - (self.输入事件['输入事件'][0][3] if len(self.输入事件['输入事件']) > 0 else 0) #
                time.sleep(max(0, delay)) # 等待时间差
                pyautogui.press(key)
            elif 事件[0] == '键盘释放':
                pass