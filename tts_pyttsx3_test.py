import pyttsx3

# 初始化TTS引擎
engine = pyttsx3.init()

# 设置一些属性，如语音速度、音量等
engine.setProperty('rate', 150)  # 语音速度
engine.setProperty('volume', 2)  # 音量大小

# 要转换为语音的文本
text = "Hello,早上好"

# 用引擎播放文本
engine.say(text)

# 等待所有已经添加到队列中的任务完成
engine.runAndWait()