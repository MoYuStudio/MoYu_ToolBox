import time
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
target_class_name = "WeChatMainWndForPC"  # 请替换为您要查找的窗口类名
target_title = "微信"  # 请替换为您要查找的窗口标题
target_window = None

for window in windows:
    if window.class_name == target_class_name and window.name == target_title:
        target_window = window
        break

if target_window is not None:
    # 使用找到的窗口类名进行连接
    app = Application().connect(class_name=target_window.class_name)
    app_window = app.top_window()  # 获取最上层的窗口

    # 将窗口最大化
    app_window.maximize()

    # 访问菜单
    menu = app_window.menu()
    print(menu)
else:
    print(f"Window with class name '{target_class_name}' and title '{target_title}' not found.")
