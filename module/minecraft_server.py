
import os
import threading
import tkinter as tk

import requests
import subprocess

class MinecraftServer:
    def __init__(self, file_folder='minecraft/server', server_version='', server_build=''):
        self.file_folder = file_folder
        self.server_version = server_version
        self.server_build = server_build
        self.server_url = f"https://papermc.io/api/v2/projects/paper"
        
        # self.file_path = os.path.join(file_folder, "server.jar")
        self.server_status = "未安装"
        self.output_label = None

    def install_server(self):
        
        if not os.path.exists(self.file_folder):
            os.makedirs(self.file_folder)

        if self.server_version == '':
            response = requests.get(f"{self.server_url}")
            version_data = response.json()
            self.server_version = version_data["versions"][-1]

        if self.server_build == '':
            response = requests.get(f"{self.server_url}/versions/{self.server_version}")
            version_data = response.json()
            self.server_build = version_data["builds"][0]

        response = requests.get(f"{self.server_url}/versions/{self.server_version}/builds/{self.server_build}")
        build_data = response.json()

        jar_name = build_data["downloads"]["application"]["name"]
        jar_url = f"{self.server_url}/versions/{self.server_version}/builds/{self.server_build}/downloads/{jar_name}"
        jar_path = os.path.join(self.file_folder, f"core.jar")
        if not os.path.exists(jar_path):
            print(f"正在下载 PaperMC {self.server_version} {self.server_build} 版本的 jar 文件...")
            response = requests.get(jar_url)
            with open(jar_path, "wb") as f:
                f.write(response.content)
            print(f"已下载到 {jar_path}")
            eula_path = os.path.join(self.file_folder, "eula.txt")
            with open(eula_path, "w") as f:
                f.write("eula=true")
        else:
            print(f"{jar_path} 已存在，无需下载。")

    def start_server(self, max_memory="4G", min_memory="2G", output_label=None):
        jar_file = os.path.join(os.getcwd()+'/'+self.file_folder, f"core.jar")
        print(jar_file)
        if not os.path.exists(jar_file):
            print("服务器文件不存在，请先安装服务器")
            return
        start_command = f"java -Xmx{max_memory} -Xms{min_memory} -jar {jar_file} nogui"
        process = subprocess.Popen(start_command, cwd=self.file_folder, stdout=subprocess.PIPE)

        self.server_status = "运行中"
        
        # 在新线程中读取子进程输出
        threading.Thread(target=self.read_output, args=(process.stdout, output_label)).start()

    def read_output(self, stdout, output_label):
        for line in iter(stdout.readline, b''):
            # print(line.decode('utf-8').strip())
            if output_label:
                output_label.config(state="normal")
                output_label.insert(tk.END, line.decode('utf-8'))
                output_label.see(tk.END)
                output_label.config(state="disabled")
        
if __name__ == '__main__':
    server = MinecraftServer("minecraft/server", "1.17.1")
    server.install_server()
    server.start_server()
