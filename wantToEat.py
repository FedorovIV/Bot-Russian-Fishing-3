import pyautogui
import keyboard 
import time
import logging
from enum import Enum

#Params of logging
logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

class returnValue(Enum):
    exception = -1
    okay = 1
    haveEat =2 

TechPause = 0.1

def wantToEat(level=0):
    
    if (level == 1):
        keyboard.send('space')
        time.sleep(TechPause*5)
        keyboard.send('space')
        time.sleep(TechPause*5)
        keyboard.send('t')

    time.sleep(TechPause)
    image_location = pyautogui.locateOnScreen('image/wantToEat.png', 
                                              confidence=0.95)
    
    if (image_location is None):
        logging.info("Don't want to eat")
        return returnValue.okay
    
    keyboard.send('space')
    time.sleep(TechPause)

    image_location = pyautogui.locateOnScreen('image/kotelok.png', 
                                              confidence=0.95)
    if (image_location is None):
        logging.exception("Can't find a kotelok")
        return returnValue.exception
    
    pyautogui.click(image_location)

    time.sleep(5*TechPause)
  
    image_location = pyautogui.locateOnScreen('image/toEat.png', 
                                              confidence=0.95)
    
    if (image_location is None):
        logging.exception("Can't find a button <to Eat>")
        return returnValue.exception  

    pyautogui.click(image_location)

    time.sleep(5*TechPause)

    pyautogui.click(image_location)

    time.sleep(TechPause)

    keyboard.send('space')

    logging.info("We have eat!")

    return returnValue.haveEat

