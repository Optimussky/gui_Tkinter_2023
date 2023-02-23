import pyautogui
import numpy as np
import cv2
import time

"""
Doc pyautogui:
We will use this tool for extracting the screen size of the users
display screen, as well as to take screenshots of the screen to pile 
up the images accordingly. The process will be:

# Obtaning the screen height and width

screenWidth, screenHeight = pyautogui.size()
screen_size = (screenWidth, screenHeight)
print(screen_size)
"""

# Obtaning the screen height and width

screenWidth, screenHeight = pyautogui.size()
screen_size = (screenWidth, screenHeight)
print(screen_size)


"""
The screen width and height are stored as a tuple in the screen 
size variable.
We will utilize this later for writting the image information, If the viewers 
are not familiar with the pyautogui tool, I would recommend checking out other 
projects:
AI Voice Assistant with this toolkit
https://towardsdatascience.com/build-your-own-ai-voice-assistant-to-control-your-pc-f4112a664db2




"""


"""
3.- Defining all the essential parameters:

In this step, we will define all the essential parameters that are 
required for creating the project. Firstly, we will define the 
four-character code in a variable. The four-character code contains a 
unique ASCII code for uniquely indentifying numerous different types 
of data formats. Once we hace defined a specific four-character code, we can 
assign a filename corresponding to the particular code. In this case, we have 
used the *'MJPG' four-character code and assingned the file name with  
the .avi video format.

We can the proceed to create an output result variable tha will write the 
screen capture video recording. We will difeine the file name, the 
four-character code, the number of frames, and the display resolution. Finally, 
we will set time recordings by defining the start times, the total duration, and the end 
time. 

"""



"""
# Creating th 4-character code of codec user to compress the frames
four_cc = cv2.VideoWriter_fourcc(*'MJPG')

# Output directory
file_name = 'screen_test.avi'
result = cv2.VideoWriter(file_name,
                         four_cc,
                         30.0,
                         screen_size)

# Seting the starting timer for the required duration
start_time = time.time()
duration = 15
end_time = start_time + duration

"""




# Creating th 4-character code of codec user to compress the frames
four_cc = cv2.VideoWriter_fourcc(*'MJPG')

# Output directory
file_name = 'screen_test.avi'
result = cv2.VideoWriter(file_name,
                         four_cc,
                         30.0,
                         screen_size)

# Seting the starting timer for the required duration
start_time = time.time()
duration = 15
end_time = start_time + duration

"""
There might be certain time fluctuations while running the code.
Hance, it is always a good idea to give an increased duration for 
recording the screen. Even if the record time is more, we can edit
or alter the desired path later. If you want to save the captured
screen recording in the form of a .mp4 video format, the following
four-character code and file name shown in the below code snippet
can be used.


# mp4 format
fourc_cc = cv2.VideoWritter_fourcc(*'mp4v')
file_name = 'screen_test.mp4'
"""


"""
4.- Creating the screen capture loop:

Finally, we can proceed to create the screen capture loop through 
which we can take screenshots and start piling up each of the recorded 
images accordingly. We will convert the captured screenshots into numpy arrays 
for simplicity of use and then convert them into RGB images. The default 
image color in open-CV is the BGR format. Hence, it is often a good idea 
to convert them. The BGR images are saved, and once the current time 
starts to exceed the end time loop, we can break the while loop and release the 
screen capture


"""
while True:
    # Record the screenshots of each image to create a vide
    images = pyautogui.screenshot()
    frames = np.array(images)
    frames_RGB = cv2.cvtColor(grames, cv2.COLOR_BGR2RGB)

    # saving the result
    result.write(frames_RGB)

    # Break the loop after the specific time has exceeded
    current_time = time.time()
    if current_time >= end_time:
        break

result.release()
print("OUTPU SAVED AS", file_name)

"""
We can notice that we have a video recording of the screen capture saved in 
the working directory the desired format. In the nex section, the readers
can access the complete code and also get a smaill glimpse of the 
recording proces tha we compute.
"""

# Complete Code:


"""
You can choose to increase the duration if you want to increase the time 
duration of the screen recording. For further improvements on this project, I 
would suggest creatting a GUI interface with a record button opinion. The 
screen recording would continue intul the button was clicked again.
"""