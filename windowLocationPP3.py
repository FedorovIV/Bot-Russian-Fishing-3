import pyautogui
import keyboard



class  MyRegion:

    #Base size of region
    BaseWight = 1280
    BaseHeight = 920

    BaseShiftLeft = 0
    BaseShiftTop = -815

    def __init__(self, x, y):
     self.left = int(x + MyRegion.BaseShiftLeft) 
     self.top =  int(y + MyRegion.BaseShiftTop) 
     self.wight = MyRegion.BaseWight
     self.height = MyRegion.BaseHeight

    def getTurple(self):
        return (self.left, self.top, self.wight, self.height)
    

def windowLocationPP3():

    location = pyautogui.locateOnScreen("image/bucket.png", confidence = 0.95)

    if (location is not None):
        return MyRegion(location.left, location.top)
