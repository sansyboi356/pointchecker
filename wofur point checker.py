import time
import AppOpener as AO 
import pyautogui as pag
import autoit as AI
import os
from PIL import ImageGrab
import pytesseract  # Import for OCR
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
import re  # Import for cleaning the extracted text
import python_imagesearch
from python_imagesearch.imagesearch import imagesearch
import pygetwindow as pgw

# Begin the program
pag.hotkey("ctrl", "win", "right")
AO.open("brave")
time.sleep(1)

# Variables and paths
ssfolder = "C:/projects/pointchecker/Images"
textfolder = "C:/projects/pointchecker/Text"
path1 = os.path.join(ssfolder, "screenshot1.png")
path2 = os.path.join(ssfolder, "screenshot2.png")
path3 = os.path.join(ssfolder, "screenshot3.png")
path4 = os.path.join(ssfolder, "screenshot4.png")
path5 = os.path.join(ssfolder, "screenshot5.png")  # 5th screenshot path
text_file_path = os.path.join(textfolder, "extracted_text.txt")  # Text file path

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
time.sleep(25)
leftclick(1445, 123)

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

# Open the guild menu
AI.send("L")
time.sleep(20)

# Get the Roblox window
window = pgw.getWindowsWithTitle("Roblox")[0]
left, top, right, bottom = window.left, window.top, window.right, window.bottom

# Define coordinates for the cropped area
capture_x1 = left + 1130
capture_y1 = top + 226
capture_x2 = left + 1500
capture_y2 = top + 670

# Function to capture and save a cropped screenshot, then scroll down
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

# Define coordinates where "50/50" should appear (adjust these as needed)
text_capture_x1 = left + 1122
text_capture_y1 = top + 102
text_capture_x2 = left + 1361
text_capture_y2 = top + 175

# Function to check for "50/50" text using OCR
def check_for_text():
    # Capture the area where "50/50" text should appear
    text_screenshot = ImageGrab.grab(bbox=(text_capture_x1, text_capture_y1, text_capture_x2, text_capture_y2))
    
    # Use OCR to extract the text from the screenshot
    extracted_text = pytesseract.image_to_string(text_screenshot, lang='jpn')
    
    # Strip everything except digits and slashes
    clean_text = re.sub(r'[^\d/]', '', extracted_text)
    
    print(f"Extracted text (cleaned): {clean_text}")
    
    # Check if the cleaned text contains "50/50"
    return "50/50" in clean_text

# Click to get onto the list
leftclick(1479, 413)

# Capture and save the first four screenshots
capture_and_scroll(path1)
capture_and_scroll(path2)
capture_and_scroll(path3)
capture_and_scroll(path4)

# Check if "50/50" is present before taking the 5th screenshot
if check_for_text():
    print("50/50 found, capturing the 5th screenshot.")
    capture_and_scroll(path5)
else:
    print("50/50 not found, skipping the 5th screenshot.")

# Function to extract text from screenshots and save to a text file
def extract_text_to_file(paths, text_file):
    with open(text_file, 'w', encoding='utf-8') as f:  # Specify utf-8 encoding
        for path in paths:
            # Use OCR to extract the text from the screenshot
            extracted_text = pytesseract.image_to_string(path, lang='jpn')  # Ensure you're using the correct path
            f.write(extracted_text + "\n")  # Write the extracted text to the file

# List of paths for all screenshots
screenshot_paths = [path1, path2, path3, path4, path5]

# Extract text and save to the specified text file
extract_text_to_file(screenshot_paths, text_file_path)

print("Text extraction complete. Check the text file for results.")
