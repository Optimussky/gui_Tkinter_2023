# Importing the necessary libraries
import pyautogui
import numpy as np
import cv2
import time

# Obtaining the screen height and width
screenWidth, screenHeight = pyautogui.size()
screen_size = (screenWidth, screenHeight)
print(screen_size)

# Creating the 4-character code of codec used to compress the frames
four_cc = cv2.VideoWriter_fourcc(*'MJPG')

"""
# mp4 format
four_cc = cv2.VideoWriter_fourcc(*'mp4v')
file_name = 'screen_test.mp4'
"""

# Output directory
file_name = 'screen_test.avi'
result = cv2.VideoWriter(file_name, 
                         four_cc,
                         30.0,
                         screen_size)


time_duration = int(input("Introduce la cantidad de segundos a grabar: "))
# Setting the starting timer for the required duration
start_time = time.time()
duration = time_duration
end_time = start_time + duration

while True:
    # Record the screenshots of each image to create a video
    images = pyautogui.screenshot()
    frames = np.array(images)
    frames_RGB = cv2.cvtColor(frames, cv2.COLOR_BGR2RGB)

    # Saving the result
    result.write(frames_RGB)

    # Breaking the loop after the specific time has exceeded
    current_time = time.time()
    if current_time >= end_time:
        break

result.release()
print("OUTPUT SAVED AS", file_name)