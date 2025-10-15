import pyautogui
import time

print("Наведи мышку на нужное место! Координаты появятся через 5 секунд...")
time.sleep(5)
print(pyautogui.position())


