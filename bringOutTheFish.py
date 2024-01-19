import keyboard
import pyautogui
import time
import logging
from windowLocationPP3 import windowLocationPP3

#Params of logging
logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w")

TechPause = 0.1

#################################
def choose_fishing_rob (RobIndex):
    keyboard.send(str(RobIndex))
    keyboard.send(str(RobIndex))
#################################
#PowerLineShiftLeft
PLShiftLeft = 441
#PowerLineShiftTop
PLShiftTop = 682
#PowerLineHeight
PowerLineHeight = 40
PowerLineWeight = 370


def powerLineLocation():

    WinPP3 = windowLocationPP3()
    if (WinPP3 is not None):
        return (WinPP3.left + PLShiftLeft, WinPP3.top + PLShiftTop,
                PowerLineWeight, PowerLineHeight)
    else:
        return None

#################################
def bringOutTheFish(RobIndex:int):

    PLLoc = powerLineLocation()

    if (PLLoc is None):
        logging.exception("Cant Find Power Line")
        return -1
    
    if (RobIndex > 3 or RobIndex < 1):
        logging.exception("Wrong Rob Index in bringOutTheFish")
        return -1
    
    choose_fishing_rob(RobIndex)

    keyboard.send('space')

    startTime = time.time()
    sadokTime = time.time()
    while(time.time()-startTime<10):
        pyautogui.keyDown('g')
        
        if (time.time() - sadokTime > 1):
            if pyautogui.locateOnScreen("image/sadok.png", confidence=0.95) is not None:
                pyautogui.keyDown('g')
                keyboard.send('space')
                logging.info('We catched fish!!!')
                return 1
            sadokTime = time.time()
        
        if (pyautogui.locateOnScreen("image/powerLine.png", confidence=0.95,
                                    region=PLLoc) )is not None:
            logging.info('This fish is too Big!')
            pyautogui.keyUp('g')
            keyboard.send('space')
            return 1
        
    if (time.time() - startTime > 10):
        keyboard.send('space')
        logging.exception("Too long bringing out")
        return -1


# keyboard.wait('l')

# # # MousePos = pyautogui.position()
# # # print(MousePos)
# # # im = pyautogui.screenshot(region=powerLineLocation())
# # # im.save(r"findedImage/powerLineSr.png") 


# bringOutTheFish(1)