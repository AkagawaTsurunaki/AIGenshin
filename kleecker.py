import pyautogui as pg
import time
import keyboard
import threading

click_flag = False
key_f_flag = False
is_instruction_output = True
is_log_output = True

def instruct():

    print("GitHub@AkagawaTsurunaki 原神连点脚本")
    print("按一次Home开始鼠标左键连点操作，按下End暂停鼠标左键连点操作。")
    print("按一次Page Up开始模拟按键F，按下Page Down暂停模拟按键F。")
    print("按一次Esc暂停整个脚本。")
    print("使用config.yaml文件配置是否输出按键信息。")

def start(iio, ilo):
    
    global is_instruction_output
    global is_log_output
    is_instruction_output = iio
    is_log_output = ilo

    # 使用说明
    if is_instruction_output:
        instruct()

    # 新建线程, 执行循环
    # 连点鼠标和连点键盘分别位于不同的线程当中
    click_thread = threading.Thread(target=click_loop)
    click_thread.start()
    key_f_thread = threading.Thread(target=key_f_loop)
    key_f_thread.start()

    # 注册热键
    keyboard.add_hotkey('home', change_click_flag, args=[True])
    keyboard.add_hotkey('end', change_click_flag, args=[False])
    keyboard.add_hotkey('page up', change_key_f_flag, args=[True])
    keyboard.add_hotkey('page down', change_key_f_flag, args=[False])
    keyboard.add_hotkey('esc', stop)

    # 阻塞线程
    keyboard.wait('pause')


def stop():
    global click_flag, key_f_flag, is_log_output
    click_flag = False
    key_f_flag = False
    
    if is_log_output:
        print("%s执行了一次脚本暂停操作。" % time.asctime())


def change_click_flag(b):
    global click_flag
    click_flag = b


def click_loop():

    global click_flag, is_log_output

    while(True):
        if click_flag:
            pg.click()
            if is_log_output:
                print("%s执行了一次左键点击操作。" % time.asctime())
        time.sleep(0.1)


def change_key_f_flag(b):
    global key_f_flag
    key_f_flag = b


def key_f_loop():

    global key_f_flag, is_log_output

    while(True):
        if key_f_flag:
            keyboard.press_and_release('f')
            if is_log_output:
                print("%s执行了一次F键操作。" % time.asctime())
        time.sleep(0.1)

