import pyautogui 
import time
import os, shutil


time.sleep(3)

Mposition = pyautogui.position()

# print("Mause pos is ", pyautogui.position())

# im = pyautogui.screenshot(region=(Mposition.x,Mposition.y, 100, 200))
# im.save(r"poplovok.png") 

timeBefore = time.time()

image_location = pyautogui.locateAllOnScreen('poplovok.png', confidence=0.999, region=(921, 596, 60, 50))

print(time.time() - timeBefore)

if image_location is not None:  
     for order in image_location:
            print (order)
            im = pyautogui.screenshot(region=(order.left, order.top, 100, 50))
            name ="findedImage/" + str (order.left) + ".png"
            im.save(name) 
else:
    print("Image not found")

# print(time.time() - timeBefore)