import pyautogui
import time

screenWidth, screenHieght = pyautogui.size()

time.sleep(5)

while(True):
    mousePositionX, mousePositionY = pyautogui.position()
    pixelColor = pyautogui.pixel(mousePositionX, mousePositionY)
    try:
        pyautogui.locateOnScreen("images/fishingMessage.png", confidence=0.9, grayscale=True)
        pyautogui.rightClick()
        time.sleep(3)
        pyautogui.rightClick()
    except:    
        try:
            pyautogui.locateOnScreen("images/fishingPoleCasted.png", confidence=0.65, grayscale=True)
            print("pole")
        except:
            pyautogui.press('esc')
            break
        

    time.sleep(.5)



    
        
    
    
    



