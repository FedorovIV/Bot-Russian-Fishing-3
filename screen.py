import pyautogui 
import time
import keyboard

keyboard.wait('l')

im = pyautogui.screenshot()
im.save(r"image/toEat.png") 