import pyttsx3

engine = pyttsx3.init()

# 获取所有可用的声音
voices = engine.getProperty('voices')
print(voices)

# # 遍历所有声音并选择您喜欢的萝莉音
# for voice in voices:
#     print(voice.id, voice.name)
#     if "Loli" in voice.name:  # 假设"Loli"在您喜欢的萝莉音声音包的名称中
#         engine.setProperty('voice', voice.id)
#         break

# 设置速率和音量
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.8)

# 使用新的声音说一句话
engine.say("Hello, I am a Loli voice.")
engine.runAndWait()