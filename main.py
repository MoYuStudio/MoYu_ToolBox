
# === MoYuToolBox 摸鱼工具箱 ===
#   Develop BY WilsonVinson   

# pyinstaller --noconfirm --onedir --windowed --icon=data/icon/icon.ico --add-data "C:\Users\WilsonVinson\AppData\Local\Programs\Python\Python311\Lib\site-packages/customtkinter;customtkinter/"  "main.py"
# pip install -r requirements.txt

import os

import customtkinter

import module.json_driver as json_driver

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.config = json_driver.json_read("data/config.json")

        customtkinter.set_appearance_mode(self.config["window"]["mode"])  # Modes: "System" (standard), "Dark", "Light"
        customtkinter.set_default_color_theme(self.config["window"]["theme"])  # Themes: "blue" (standard), "green", "dark-blue"

        self.title("MoYu ToolBox 摸鱼工具箱")
        self.iconbitmap("data/icon/icon.ico")
        self.geometry(f"{600}x{400}")
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.tabview = customtkinter.CTkTabview(self,width=10,height=10)
        self.tabview.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        if os.path.exists("dlc/auto.py"):
            import dlc.auto
            self.tabview.add("自动化")
            page_auto = dlc.auto.PageAuto(self.tabview.tab("自动化"))
            
        if os.path.exists("dlc/bilibili.py"):
            import dlc.bilibili
            self.tabview.add("B站")
            page_bilibili = dlc.bilibili.PageBiliBili(self.tabview.tab("B站"))

        if os.path.exists("dlc/mc.py"):
            import dlc.mc
            self.tabview.add("MC")
            page_mc = dlc.mc.PageMC(self.tabview.tab("MC"))
        
        if len(self.tabview.children)-2 <= 1:
            self.tabview.add(" MoYu ToolBox ")
            
            info_label = customtkinter.CTkLabel(self.tabview.tab(" MoYu ToolBox "), text='安装任意DLC以开始', font=('Microsoft YaHei', 32))
            info_label.pack()
            
        self.tabview.add("设置")
        self.page_setting_group()

        self.bind("<Configure>", self.on_window_resize)

    def on_window_resize(self, event):
        self.tabview.configure(width=event.width - 20, height=event.height - 10)
        
    def page_setting_group(self):
        def change_appearance_mode_event(new_appearance_mode: str):
            customtkinter.set_appearance_mode(new_appearance_mode)
        def change_scaling_event(new_scaling: str):
            new_scaling_float = int(new_scaling.replace("%", "")) / 100
            customtkinter.set_widget_scaling(new_scaling_float)
            
        appearance_mode_label = customtkinter.CTkLabel(self.tabview.tab("设置"), text="主题:", font=('Microsoft YaHei', 16), anchor="w")
        appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.tabview.tab("设置"), values=["Light", "Dark", "System"], command=change_appearance_mode_event)
        appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        appearance_mode_optionemenu.set("System")
        
        scaling_label = customtkinter.CTkLabel(self.tabview.tab("设置"), text="UI比例:", font=('Microsoft YaHei', 16), anchor="w")
        scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        scaling_optionemenu = customtkinter.CTkOptionMenu(self.tabview.tab("设置"), values=["80%", "90%", "100%", "110%", "120%"], command=change_scaling_event)
        scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))
        scaling_optionemenu.set("100%") 
        
if __name__ == "__main__":
    app = App()
    app.mainloop()