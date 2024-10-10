import time
import AppOpener as AO 
import pyautogui as pag
import autoit as AI
import os
from PIL import ImageGrab
import pytesseract 
import re  
import python_imagesearch
from python_imagesearch.imagesearch import imagesearch
import pygetwindow as pgw

# Begin the program
pag.hotkey("ctrl", "win", "right")
AO.open("brave")
time.sleep(1)

# Variables and paths
ssfolder = "C:/projects/pointchecker/Images"
path1 = os.path.join(ssfolder, "screenshot1.png")
path2 = os.path.join(ssfolder, "screenshot2.png")
path3 = os.path.join(ssfolder, "screenshot3.png")
path4 = os.path.join(ssfolder, "screenshot4.png")
path5 = os.path.join(ssfolder, "screenshot5.png")  # 5th screenshot path
output_txt_path = os.path.join(ssfolder, "screenshot_text_output.txt")  # Output text file path

# Mouse click helper function
def leftclick(X, Y, lc=1, spd=-1):
    AI.mouse_click(x=X, y=Y, clicks=lc, speed=spd)

# Function to capture and save a cropped screenshot, then scroll down
def capture_and_scroll(path, left, top, right, bottom, capture_x1, capture_y1, capture_x2, capture_y2):
    # Take a new screenshot of the Roblox window
    screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
    
    # Crop the screenshot to the desired area
    cropped_screenshot = screenshot.crop((capture_x1, capture_y1, capture_x2, capture_y2))
    
    # Save the cropped screenshot
    cropped_screenshot.save(path)
    
    # Scroll down
    AI.mouse_wheel("down", clicks=3)
    time.sleep(2)  # Give some time for the screen to update

# Function to extract text from a screenshot
def extract_text_from_image(image_path, left, top, right, bottom):
    screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))  # Open the screenshot
    extracted_text = pytesseract.image_to_string(screenshot)  # Extract text using OCR
    return extracted_text

# Write text from screenshots into a text file
def write_text_to_file(text_list, file_path):
    with open(file_path, 'w') as file:
        for i, text in enumerate(text_list):
            file.write(f"Text from screenshot {i+1}:\n")
            file.write(text + "\n")
            file.write("="*40 + "\n")  # Divider between each screenshot's text

# Function to check for "50/50" text using OCR
def check_for_text(left, top, right, bottom, text_capture_x1, text_capture_y1, text_capture_x2, text_capture_y2):
    # Capture the area where "50/50" text should appear
    text_screenshot = ImageGrab.grab(bbox=(text_capture_x1, text_capture_y1, text_capture_x2, text_capture_y2))
    
    # Use OCR to extract the text from the screenshot
    extracted_text = pytesseract.image_to_string(text_screenshot)
    
    # Strip everything except digits and slashes
    clean_text = re.sub(r'[^\d/]', '', extracted_text)
    
    print(f"Extracted text (cleaned): {clean_text}")
    
    # Check if the cleaned text contains "50/50"
    return "50/50" in clean_text

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
time.sleep(10)

# Get the Roblox window
window = pgw.getWindowsWithTitle("Roblox")[0]
left, top, right, bottom = window.left, window.top, window.right, window.bottom

# Define coordinates for the cropped area
capture_x1 = left + 1130
capture_y1 = top + 226
capture_x2 = left + 1500
capture_y2 = top + 670

# Define coordinates where "50/50" should appear 
text_capture_x1 = left + 1130
text_capture_y1 = top + 113
text_capture_x2 = left + 1353
text_capture_y2 = top + 166

# Click to get onto the list
leftclick(1479, 413)

# Capture and save the four screenshots
capture_and_scroll(path1, left, top, right, bottom, capture_x1, capture_y1, capture_x2, capture_y2)
capture_and_scroll(path2, left, top, right, bottom, capture_x1, capture_y1, capture_x2, capture_y2)
capture_and_scroll(path3, left, top, right, bottom, capture_x1, capture_y1, capture_x2, capture_y2)
capture_and_scroll(path4, left, top, right, bottom, capture_x1, capture_y1, capture_x2, capture_y2)

# Extract text from each of the four screenshots
screenshot_texts = [
    extract_text_from_image(path1, left, top, right, bottom),
    extract_text_from_image(path2, left, top, right, bottom),
    extract_text_from_image(path3, left, top, right, bottom),
    extract_text_from_image(path4, left, top, right, bottom)
]

# Write the extracted text into the output text file
write_text_to_file(screenshot_texts, output_txt_path)

# Check if "50/50" is present before taking the 5th screenshot
if check_for_text(left, top, right, bottom, text_capture_x1, text_capture_y1, text_capture_x2, text_capture_y2):
    print("50/50 found, capturing the 5th screenshot.")
    capture_and_scroll(path5, left, top, right, bottom, capture_x1, capture_y1, capture_x2, capture_y2)
else:
    print("50/50 not found, skipping the 5th screenshot.")
