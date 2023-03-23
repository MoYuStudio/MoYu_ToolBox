import os
import requests

# 创建文件夹
file_folder = "minecraft/server"
if not os.path.exists(file_folder):
    os.makedirs(file_folder)

# 下载Spigot mc核心
server_version = "1.12.2"
server_url = f"https://cdn.getbukkit.org/spigot/spigot-{server_version}.jar"
file_path = os.path.join(file_folder, "server.jar")

response = requests.get(server_url, stream=True)
if response.status_code == 200:
    with open(file_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
else:
    print("下载Spigot mc核心失败")
