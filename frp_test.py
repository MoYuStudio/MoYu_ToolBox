import subprocess

# 启动frpc客户端
frpc_path = "frp/frpc"
config_file = "frp/frpc.ini"

process = subprocess.Popen([frpc_path, "-c", config_file])

# # 停止frpc客户端
# process.terminate()

# # 重启frpc客户端
# process.terminate()
# process = subprocess.Popen([frpc_path, "-c", config_file])