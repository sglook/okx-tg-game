import pyautogui
import time

position1 = (1274, 513)
position2 = (1275, 513)
position3 = (1212, 650)

toggle = True
click_count = 0

def click():
    global toggle, click_count

    if toggle:
        pyautogui.click(position1)
        pyautogui.click(position3)
        time.sleep(0.3)
        pyautogui.click(position1)
        print(f"Clicked at {position1}")
    else:
        pyautogui.click(position2)
        pyautogui.click(position3)
        time.sleep(0.3)
        pyautogui.click(position2)
        print(f"Clicked at {position2}")

    toggle = not toggle
    click_count += 1

    if click_count >= 18:
        pyautogui.click(position3)
        print("Pausing for 10 seconds...")
        for i in range(25):
            print(f"Resuming in {25 - i} minutes...")
            time.sleep(60)
        click_count = 0
    else:
        time.sleep(8.3)

print("Auto clicker started. Press Ctrl+C to stop.")

try:
    while True:
        click()
except KeyboardInterrupt:
    print("Auto clicker stopped.")
