import pyautogui
import time

screenWidth, screenHieght = pyautogui.size()


while(True):
    mousePositionX, mousePositionY = pyautogui.position()
    pixelColor = pyautogui.pixel(mousePositionX, mousePositionY)
    try:
        area = pyautogui.locateOnScreen("images/image.png", confidence=0.9)
        pyautogui.rightClick()
        time.sleep(3)
        pyautogui.rightClick()
    except:
        pass
        
    time.sleep(.5)
        
    
    
    



