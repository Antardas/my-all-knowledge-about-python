from time import sleep
import pyautogui
sleep(5)
for i in range(1, 100):
    pyautogui.typewrite("Vai apni onek valo manus")
    pyautogui.press("enter")
    sleep(0.2)
