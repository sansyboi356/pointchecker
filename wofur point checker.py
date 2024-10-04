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


## begin the fuckery (for a second time)
pag.hotkey("ctrl" , "win" , "right")
AO.open("brave")
time.sleep(1)
## defines

## so I dont have to write it over and over
def leftclick (X , Y, lc = 1, spd = -1):
    AI.mouse_click(x = X, y = Y, clicks = lc, speed = spd)

## for image writing bs
ssfolder = "C:/projects/pointchecker/Images"
path = os.path.join(ssfolder, "screenshot.png")



## back to the scheduled program
leftclick(282, 83)
## game website
pag.typewrite("https://www.roblox.com/games/2727067538/2X-World-Zero-Anime-RPG")
pag.hotkey("enter")
time.sleep(5)
## clicks play
leftclick(1432, 618)
time.sleep(20)
## clicks play (with intent)
leftclick(962, 920)
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

cropped_screenshot.save(path)
