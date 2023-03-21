
from pynput import mouse

def 鼠标移动(x, y): # on_move=鼠标移动, 
    print("鼠标移动到了 ({0}, {1})".format(x, y))

def 鼠标按下(x, y, button, 按下):
    if 按下:
        print("按下")
        print("{0}, {1}".format(x, y))
    else:
        print("释放")

def 鼠标滚轮(x, y, dx, dy):
    print("鼠标滚轮滚动了 {0} 像素".format(dy))

鼠标监听器 = mouse.Listener(on_click=鼠标按下, on_scroll=鼠标滚轮)
鼠标监听器.start()
鼠标监听器.join()
