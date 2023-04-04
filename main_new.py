
# === MoYuToolBox 摸鱼工具箱 ===
#   Develop BY WilsonVinson   

import customtkinter
import PIL

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
        self.tabview.add("主页")
        self.tabview.add("自动化")
        self.tabview.add("B站")
        self.tabview.add("MC")
        self.tabview.add("设置")
        
        
        image_file = PIL.Image.open("data/icon/icon_x500.png")
        tk_image = PIL.ImageTk.PhotoImage(image_file)
        icon_label = customtkinter.CTkLabel(self.tabview.tab("主页"), text='',image=tk_image)
        icon_label.pack()
        
        title_label = customtkinter.CTkLabel(self.tabview.tab("主页"), text='MoYu ToolBox', font=('Microsoft YaHei', 32))
        title_label.pack()
        
        copyright_label = customtkinter.CTkLabel(self.tabview.tab("主页"), text='Powered BY ChatGPT   Developed BY WilsonVinson', font=('Microsoft YaHei', 10))
        copyright_label.pack()

        self.bind("<Configure>", self.on_window_resize)

    def on_window_resize(self, event):
        self.tabview.configure(width=event.width - 20, height=event.height - 10)

if __name__ == "__main__":
    app = App()
    app.mainloop()