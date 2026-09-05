import pyautogui
import time

screenWidth, screenHieght = pyautogui.size()
fishCaught = 0

time.sleep(5)

while(True):
    mousePositionX, mousePositionY = pyautogui.position()
    pixelColor = pyautogui.pixel(mousePositionX, mousePositionY)
    try:
        pyautogui.locateOnScreen("images/fishingMessage.png", confidence=0.9, grayscale=True)
        pyautogui.rightClick()
        fishCaught += 1
        time.sleep(3)
        pyautogui.rightClick()
    except:    
        try:
            pyautogui.locateOnScreen(("images/fishingPoleCasted.png" or "images/fishingMessage.png"), confidence=0.7, grayscale=True)
        except:
            pyautogui.press('esc')
            print(f"Fish Caught: {fishCaught}")
            break
        

    time.sleep(.5)



    
        
    
    
    



