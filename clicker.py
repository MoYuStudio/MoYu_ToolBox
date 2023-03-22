
import time

import pyautogui

class 执行器:
    def __init__(self, 输入事件):
        self.输入事件 = 输入事件
        self.计时器 = 0

    def 运行(self):
        print('开始模仿')
        for 事件id in range(len(self.输入事件['输入事件'])):
            事件 = self.输入事件['输入事件'][事件id]
            if 事件[0] == '鼠标移动':
                x, y = 事件[1], 事件[2]
                try:
                    延迟 = 事件[3] - self.输入事件['输入事件'][事件id-1][3]
                    time.sleep(max(0, 延迟))
                except:
                    pass
                pyautogui.moveTo(x, y)
            elif 事件[0] == '鼠标点击':
                x, y = 事件[1], 事件[2]
                button = str(事件[3])
                action = 事件[4]
                try:
                    延迟 = 事件[5] - self.输入事件['输入事件'][事件id-1][5]
                    time.sleep(max(0, 延迟))
                except:
                    pass
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
                try:
                    延迟 = 事件[5] - self.输入事件['输入事件'][事件id-1][5]
                    time.sleep(max(0, 延迟))
                except:
                    pass
                pyautogui.scroll(dx, dy)
            elif 事件[0] == '键盘按下':
                key = 事件[2] if 事件[2] is not None else 事件[1]
                if key == 'Key.space':
                    key = 'space'
                try:
                    延迟 = 事件[3] - self.输入事件['输入事件'][事件id-1][3]
                    time.sleep(max(0, 延迟))
                except:
                    pass
                pyautogui.press(key)
            elif 事件[0] == '键盘释放':
                pass
            
        print('结束模仿')