
import pyttsx3

engine = pyttsx3.init()

# 获取当前声音
# voices = engine.getProperty('voices')

# 更改声音属性
engine.setProperty('voice', 1)  # 0 为男声，1 为女声

# 更改语速
engine.setProperty('rate', 230)  # 默认为 200

# 更改音量
engine.setProperty('volume', 0.8)  # 默认为 1

# 测试输出
engine.say('你好，世界！')
engine.runAndWait()