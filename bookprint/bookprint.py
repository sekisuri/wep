from PIL import ImageGrab
import pyautogui
import time

print("3초 후 시작")
time.sleep(3)
 
for i in range(5):
    time.sleep(3)
    img=ImageGrab.grab()
    saveas= str(i) + ".png" 
   # img.save(saveas)
    print(saveas)
   # pyautogui.scroll(100)
   # pyautogui.press('rigit')
    pyautogui.keyDown('right')
    time.sleep(1)
    pyautogui.keyUp('right')



