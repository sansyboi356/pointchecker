## Cocain imports
import time
import AppOpener as AO 
import pyautogui as pag
import autoit as AI
import ait
## begin the fuckery (for a second time)
pag.hotkey("ctrl" , "win" , "right")
AO.open("brave")
time.sleep(1)
## defines
def leftclick (X , Y, lc = 1, spd = -1):
    AI.mouse_click(x = X, y = Y, clicks = lc, speed = spd)
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
AI.send("l")
##open cv time YIPPE
