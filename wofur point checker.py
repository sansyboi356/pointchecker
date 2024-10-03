## Cocain imports
import time
import AppOpener as AO 
import pyautogui as pag
import autoit as AI
## begin the fuckery (for a second time)
pag.hotkey("ctrl" , "win" , "right")
AO.open("brave")
time.sleep(1)
# define
def leftclick (X , Y, lc = 1, spd = -1):
    AI.mouse_click(x = X, y = Y, clicks = lc, speed = spd)
## back to the scheduled program
leftclick(282, 83)
pag.typewrite("https://www.roblox.com/games/2727067538/2X-World-Zero-Anime-RPG")
pag.hotkey("enter")
time.sleep(5)
leftclick(1432, 618)
time.sleep(20)
leftclick(962, 920)
time.sleep(35)

