import pyautogui
import time
import keyboard
import logging

#Params of logging
logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

#Techical pause
TechPause = 0.1
#region-(left, top, wight, heigth)

########################################################
class  MyRegion:

    #Base size of region
    BaseHeight = 50
    BaseWight = 50
    BaseShiftLeft = -BaseWight/2
    BaseShiftTop = -0.9*BaseHeight

    def __init__(self, x, y):
     self.left = int(x + MyRegion.BaseShiftLeft) 
     self.top =  int(y + MyRegion.BaseShiftTop) 
     self.wight = MyRegion.BaseWight
     self.height = MyRegion.BaseHeight

    def getTurple(self):
        return (self.left, self.top, self.wight, self.height)

########################################################
     
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

########################################################
        
DiffInterval = 7

def DiffValueFromList(listX):

    if (listX is None or len(listX) == 0): 
        return None 
    
    listX = sorted(listX)

    AnsList = []
    AnsList.append(listX[0])

    for i in range(1, len(listX)):
        if (listX[i] - AnsList[-1] > DiffInterval):
            AnsList.append(listX[i])
    
    return AnsList

########################################################
def findPopl(KlevRegion: MyRegion):

    image_location = pyautogui.locateAllOnScreen('image/poplovok.png', 
                                                    confidence=0.90, region=KlevRegion.getTurple(), 
                                                    limit = 10,
                                                    grayscale=False)
    listX = []

    if image_location is not None:  
        for order in image_location:
            listX.append(order.left)

    if (listX is None):
        return None
    
    DListX = DiffValueFromList(listX)

    return DListX
########################################################
#Maximum dif int between AllCoords and Coords
MaxDif = 3
#MaxSearchTime
MaxST = 30

def findKlev(x:int, y:int, NumFR):

    KlevRegion = MyRegion(x, y)

    ########################################################
    #Make screenshot of region
    im = pyautogui.screenshot(region=KlevRegion.getTurple())
    im.save(r"findedImage/region.png") 
    
    ########################################################

    #Coordinates of all poplovoks

    allCoordsPopl = []

    ########################################################
    #Find coordinates of all poplovok
    startTime = time.time()
    while (1):
        
        time.sleep(TechPause)

        if (time.time() - startTime > MaxST):
            logging.exception("Too long find of all coordinates")
            return -1
        
        # logging.info("Try to find all popl")

        coordsPopl = findPopl(KlevRegion)

        if (coordsPopl is None):
            continue

        if (len(coordsPopl) == NumFR):
            allCoordsPopl = coordsPopl
            break


    ##########################################################
    

    logging.info("All Coordinate of Popl is" + str(allCoordsPopl))    

    ##########################################################
    #Find Kleving rob
    
    startTime = time.time()

    while (1):
        
        time.sleep(TechPause)

        if (time.time() - startTime > MaxST):
            logging.exception("Too long find of Kleving rob")
            return -1
        
        # logging.info("Try to find Kleving rob")

        coordsPopl = findPopl(KlevRegion)
        ################################################
        #Check coordsPopl
        if (coordsPopl is None):
            logging.exception("No popl in FindKlevin rob")
            return 1 

        if (len(coordsPopl) == NumFR):
            continue

        if (len(coordsPopl) > NumFR):
            logging.exception("Num of popl bigger than NunFR")
            continue
        ################################################
        for i in range(0, len(allCoordsPopl)):
            flag = False
            for j in range(0, len(coordsPopl)):
                if (abs(allCoordsPopl[i]-coordsPopl[j])<MaxDif):
                    flag = True
            if (not flag):
                logging.info("Rob is finded. It's " + str(i+1))
                return i+1
            
    logging.error("logic ERROR in findKlev")    
    return -1
    

########################################################


    
########################################################
    
# keyboard.wait('l')

# MousePos = pyautogui.position()
# KlevRegion = MyRegion(MousePos.x, MousePos.y)


# count = 0
# while (1):
#     count+=1
#     n = findKlev(MousePos.x, MousePos.y, 3)
#     im = pyautogui.screenshot(region=KlevRegion.getTurple())
#     im.save(r"findedImage/" + str(count) + "_" + str(n) + ".png") 
#     print("Rob is finded! It's " + str(n))