
from gtts import gTTS
import pygame

# 定义要转换为语音的文本
text = "Hello,早上好"

# 设置语言和其他参数
language = 'zh-CN' #'zh-CN' 'zh-TW'
slow_audio_speed = False

# 创建一个 gTTS 对象
my_audio = gTTS(text=text, lang=language, slow=slow_audio_speed)

# 保存生成的音频文件
my_audio.save("output_audio.mp3")

# 播放生成的音频文件（仅限于 macOS 和 Linux，Windows 用户需要使用其他方法）
# os.system("mpg321 output_audio.mp3")

# 初始化 pygame
pygame.mixer.init()

# 加载音频文件
pygame.mixer.music.load("output_audio.mp3")

# 播放音频文件
pygame.mixer.music.play()

# 等待音频播放结束
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)