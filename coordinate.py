import pyautogui
import time

try:
    while True:
        # 获取当前鼠标位置的坐标
        current_mouse_x, current_mouse_y = pyautogui.position()
        print(f"Current mouse position: ({current_mouse_x}, {current_mouse_y})")
        time.sleep(2)  # 每2秒获取一次坐标
except KeyboardInterrupt:
    print("Program stopped.")
