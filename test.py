import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# 创建 Notebook 控件
notebook = ttk.Notebook(root)

# 创建多个选项卡
tab1 = tk.Frame(notebook)
tab2 = tk.Frame(notebook)

# 向选项卡添加控件
tk.Label(tab1, text="这是选项卡1").pack(padx=20, pady=20)
tk.Label(tab2, text="这是选项卡2").pack(padx=20, pady=20)

# 添加选项卡到 Notebook 控件中
notebook.add(tab1, text="选项卡1")
notebook.add(tab2, text="选项卡2")

notebook.pack()

root.mainloop()