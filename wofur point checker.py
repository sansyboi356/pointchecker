import time
import AppOpener as AO 
import pyautogui as pag
import autoit as AI
import os
from PIL import ImageGrab
import python_imagesearch
from python_imagesearch.imagesearch import imagesearch
import pygetwindow as pgw

## begin the program
pag.hotkey("ctrl", "win", "right")
AO.open("brave")
time.sleep(1)

## variables and paths
ssfolder = "C:/projects/pointchecker/Images"
path1 = os.path.join(ssfolder , "screenshot1.png")
path2 = os.path.join(ssfolder , "screenshot2.png")
path3 = os.path.join(ssfolder , "screenshot3.png")
path4 = os.path.join(ssfolder , "screenshot4.png")
path5 = os.path.join(ssfolder , "screenshot5.png")

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

# Retry mechanism for finding and clicking the play button image
while True:
    position = imagesearch("C:/projects/pointchecker/screen finder/playbutton.png")
    
    if position[0] != -1:
        print(f"Image found at {position}. Clicking now...")
        leftclick(position[0], position[1])
        break
    else:
        print("Image not found, retrying in 2 seconds...")
        time.sleep(2)
        
time.sleep(35)

## Open the guild menu
AI.send("L")
time.sleep(10)

# Get the Roblox window
window = pgw.getWindowsWithTitle("Roblox")[0]
left, top, right, bottom = window.left, window.top, window.right, window.bottom

# Define coordinates for the cropped area
capture_x1 = left + 1130
capture_y1 = top + 226
capture_x2 = left + 1500
capture_y2 = top + 670

# Function to capture and save the cropped screenshot, then scroll down
def capture_and_scroll(path):
    # Take a new screenshot of the Roblox window
    screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
    
    # Crop the screenshot to the desired area
    cropped_screenshot = screenshot.crop((capture_x1, capture_y1, capture_x2, capture_y2))
    
    # Save the cropped screenshot
    cropped_screenshot.save(path)
    
    # Scroll down
    AI.mouse_wheel("down", clicks=3)
    time.sleep(2)  # Give some time for the screen to update

# leftclick to get onto the list
leftclick(1479, 413)

# Capture and save the first screenshot
capture_and_scroll(path1)

# Capture and save the second screenshot after scrolling
capture_and_scroll(path2)

# Capture and save the third screenshot after scrolling
capture_and_scroll(path3)

# Capture and save the fourth screenshot after scrolling
capture_and_scroll(path4)

# Capture and save the fith screenshot after scrolling
capture_and_scroll(path5)
