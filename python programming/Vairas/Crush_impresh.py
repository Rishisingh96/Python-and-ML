import pyautogui
import time
time.sleep(6)
count = 0
while count<=500:
    pyautogui.typewrite("I love you 💕😍" +str(count))
    pyautogui.press("enter")
    count = count+1;
    