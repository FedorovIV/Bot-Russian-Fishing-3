from sdelat_zabros import sdelat_zabros
from sdelat_zabros import sdelat_perezabros
from findKlev import findKlev
from bringOutTheFish import bringOutTheFish

import keyboard
import mouse 
import pyautogui
import time
import logging
import asyncio

#Params of logging
logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w")


#NumFR - number of fishing robs
NumFR = 3 

#Techical pause
TechPause = 0.1

###############################

#Wait until l and mouse click
keyboard.wait('l')
MousePos = pyautogui.position()
###############################
#sdelat zabros
for i in range(0, 2):
    sdelat_zabros(MousePos.x, MousePos.y, NumFR)
###############################

while (1):

    sdelat_perezabros(NumFR)

    RobIndex = findKlev(MousePos.x, MousePos.y, NumFR)

    if (RobIndex == -1):
        logging.warning("RobIndex in main is -1 after findKlev")
        continue
    
    if (bringOutTheFish(RobIndex) == -1):
        logging.warning("May be some problems in bringing out fish")     
        continue


