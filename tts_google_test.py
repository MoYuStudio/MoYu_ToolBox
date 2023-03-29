from io import BytesIO
from gtts import gTTS
import pygame

# 定义要转换为语音的文本
text = "0 Hello,早上好"

# 设置语言和其他参数
language = 'zh-CN' #'zh-CN' 'zh-TW'
slow_audio_speed = False

# 创建一个 gTTS 对象
my_audio = gTTS(text=text, lang=language, slow=1.5)

# 生成音频流
audio_stream = BytesIO()
my_audio.write_to_fp(audio_stream)
audio_stream.seek(0)

# 初始化 pygame
pygame.mixer.init()

# 加载音频流
pygame.mixer.music.load(audio_stream)

# 播放音频文件
pygame.mixer.music.play()

# 等待音频播放结束
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
