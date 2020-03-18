from PIL import ImageGrab
import pyautogui
import time


path = "1.png"

print("3초 후 시작")
time.sleep(3)
 
for i in range(5):
    time.sleep(3)
    img=ImageGrab.grab()
    saveas= str(i) + ".png" 
    img.save(saveas)
    pyautogui.scroll(100)


