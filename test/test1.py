import win32api
import win32con
import win32gui
import time
import pyautogui
import pywinauto
from pywinauto.application import Application
from pywinauto.findwindows import find_elements

# 获取所有可见窗口元素
windows = find_elements(visible_only=True)

# 创建一个空集合来存储窗口类名和窗口标题
unique_window_info = set()

# 将每个窗口的类名和标题添加到集合中
for window in windows:
    unique_window_info.add((window.class_name, window.name))

# 打印唯一的窗口类名和标题
for class_name, title in unique_window_info:
    print(f"{class_name}: {title}")

# 查找具有特定标题的窗口
target_class_name = "Notepad"  # 请替换为您要查找的窗口类名
target_title = "Notepad"  # 请替换为您要查找的窗口标题

# Find the window by its class name and window title
hwnd = win32gui.FindWindow(target_class_name, target_title)

# Bring the window to the foreground
win32gui.SetForegroundWindow(hwnd)

# Get the button's position relative to the window
button_x = 500
button_y = 500

# Calculate the position of the button on the screen
left, top, right, bottom = win32gui.GetWindowRect(hwnd)
button_pos = (left + button_x, top + button_y)

# Set the cursor position to the button
win32api.SetCursorPos(button_pos)

# Simulate a left-click on the button
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, button_pos[0], button_pos[1], 0, 0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, button_pos[0], button_pos[1], 0, 0)

# Type 'halo world'
# Set the text of the window
text = "Hello, world!"
# win32api.SendMessage(hwnd, win32con.WM_SETTEXT, 0, text)