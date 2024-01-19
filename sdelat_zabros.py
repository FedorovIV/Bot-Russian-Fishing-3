from pyautogui import click
import time
import keyboard
import mouse
import pyautogui

TechPause = 0.1
#######################################

#sleep after choose
SleepAC = 0.2

def choose_fishing_rob (num):
    keyboard.send(str(num))
    keyboard.send(str(num))

    time.sleep(SleepAC)

#######################################
    
#sleep after zabros
SleepAZ = 0.7    
# Dis - Distance between poplovok
DisBP = 10

# NumFR - Number of fishing rob
# The fishing rods should be on the left of clix(x, y)
def sdelat_zabros(x:int, y:int, NumFR:int):

    match NumFR:
        case 1:
            startpos = x
        case 2:
            startpos = int(x - DisBP/2)
        case 3:
            startpos = int(x - DisBP*1.5)
        case _:
            raise ValueError('NumFR shood be between 1 and 3')
    
    for i in range(1, NumFR + 1):
        choose_fishing_rob(i)        
        keyboard.send('space')
        time.sleep(TechPause*5)
        keyboard.send('space')
        time.sleep(TechPause*5)

        click(startpos + (i-1)*DisBP, y)    
         
        time.sleep(SleepAZ)
#######################################
#sleep after perezabros
SleepAP = SleepAZ
def sdelat_perezabros(NumFR:int):
    for i in range(1, NumFR + 1):
        choose_fishing_rob(i)        
        keyboard.send('space')
        time.sleep(TechPause*5)
        keyboard.send('space')
        time.sleep(TechPause*5)
        keyboard.send('t')
        time.sleep(SleepAP)