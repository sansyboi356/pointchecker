## Cocain imports
import time
import AppOpener as AO 
import pyautogui as pag
import autoit as AI
import ait
import cv2 as ocv
import pytesseract as pyt
import os
import PIL
import pygetwindow as pgw
import mss 
import mss.tools
from PIL import ImageGrab
import python_imagesearch 
from python_imagesearch.imagesearch import imagesearch
## begin the fuckery (for a second time)
pag.hotkey("ctrl", "win", "right")
AO.open("brave")
time.sleep(1)

## variables and whatnot
ssfolder = "C:/projects/pointchecker/Images"
path1 = os.path.join(ssfolder , "screenshot1.png")
path2 = os.path.join(ssfolder , "screenshot2.png")
path3 = os.path.join(ssfolder , "screenshot3.png")


# Mouse click helper function
def leftclick(X, Y, lc=1, spd=-1):
    AI.mouse_click(x=X, y=Y, clicks=lc, speed=spd)

# Navigate to the game URL
leftclick(1821, 69)
time.sleep(.5)
leftclick(282, 83)
pag.typewrite("https://www.roblox.com/games/2727067538/2X-World-Zero-Anime-RPG")
pag.hotkey("enter")
time.sleep(5)

# Click 'Play' button
leftclick(1432, 618)
time.sleep(20)

# Search for the play button image on the screen
position = imagesearch("C:/projects/pointchecker/screen finder/playbutton.png")

## finds the play button and if it doesnt find it retries
while True:
    position = imagesearch("C:/projects/pointchecker/screen finder/playbutton.png")
    
    # If image is found, click and break the loop
    if position[0] != -1:
        print(f"Image found at {position}. Clicking now...")
        leftclick(position[0], position[1])
        break
    else:
        print("Image not found, retrying in 2 seconds...")
        time.sleep(2)  # Wait 2 seconds before retrying
        
time.sleep(35)

##ok we have roblox open, now we go to open the guild menu
AI.send("L")
time.sleep(10)
##open cv time YIPPE

# gets window to read and hopefully screenshot
window = pgw.getWindowsWithTitle("Roblox")[0]
##x,y coords
left, top, right, bottom = window.left, window.top, window.right, window.bottom

capture_x1 = left + 1130
capture_y1 = top + 226
capture_x2 = left + 1500
capture_y2 = top + 649

screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
## cropped ver
cropped_screenshot = screenshot.crop((capture_x1, capture_y1, capture_x2, capture_y2))
## first screenshot acquired
cropped_screenshot.save(path1)
time.sleep(2)

