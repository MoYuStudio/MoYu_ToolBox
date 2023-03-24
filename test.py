import os
import requests

# PaperMC 官方下载页面 URL
url_prefix = "https://papermc.io/api/v2/projects/paper"

# 要下载的 PaperMC 版本和构建版本
version = ""
build = ""

# 下载文件保存的文件夹
folder = "papermc_jars"
if not os.path.exists(folder):
    os.makedirs(folder)

if version == '':
    # 获取最新版本的 PaperMC
    response = requests.get(f"{url_prefix}")
    version_data = response.json()
    print(version_data)  # Print the response for debugging purposes
    version = version_data["versions"][-1]

if build == '':
    response = requests.get(f"{url_prefix}/versions/{version}")
    version_data = response.json()
    build = version_data["builds"][0]

# 获取构建版本的详细信息
response = requests.get(f"{url_prefix}/versions/{version}/builds/{build}")
build_data = response.json()

# 下载构建版本的 jar 文件
jar_name = build_data["downloads"]["application"]["name"]
jar_url = f"{url_prefix}/versions/{version}/builds/{build}/downloads/{jar_name}"
jar_path = os.path.join(folder, f"paper-{version}-{build}.jar")
if not os.path.exists(jar_path):
    print(f"正在下载 PaperMC {version} {build} 版本的 jar 文件...")
    response = requests.get(jar_url)
    with open(jar_path, "wb") as f:
        f.write(response.content)
    print(f"已下载到 {jar_path}")
else:
    print(f"{jar_path} 已存在，无需下载。")
