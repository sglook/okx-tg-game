import pyautogui
import time

position1 = (100, 200)
position2 = (300, 400)
# 自行修改按键坐标，可通过另一个脚本查看两个按键的坐标

toggle = True
click_count = 0

def click():
    global toggle, click_count

    if toggle:
        pyautogui.click(position1)
        print(f"Clicked at {position1}")
    else:
        pyautogui.click(position2)
        print(f"Clicked at {position2}")

    toggle = not toggle
    click_count += 1

    if click_count >= 10:
        print("Pausing for 820 seconds...")
        time.sleep(820)  
        click_count = 0
    else:
        time.sleep(8)  

print("Auto clicker started. Press Ctrl+C to stop.")

try:
    while True:
        click()
except KeyboardInterrupt:
    print("Auto clicker stopped.")
