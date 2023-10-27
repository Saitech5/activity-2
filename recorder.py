import cv2
import numpy as np
import pyautogui

# display screen resolution, get it using pyautogui itself
SCREEN_SIZE = tuple(pyautogui.size())

# define the codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")

# frames per second
fps = 12.0

# create the video write object
out = cv2.VideoWriter("output.avi", fourcc, fps, (SCREEN_SIZE))

# the time you want to record in seconds
record_seconds = 10

for i in range(int(record_seconds * fps)):
    # make a screenshot
    img = pyautogui.screenshot()

    # convert these pixels to a proper numpy array to work with OpenCV
    frame = np.array(img)

    # convert colors from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # write the frame
    out.write(frame)

    # show the frame
    cv2.imshow("screenshot", frame)
    
    # if the user clicks q, it exits
    if cv2.waitKey(1) == ord("q"):
        break

# make sure everything is closed when exited
cv2.destroyAllWindows()
out.release()




##This is the code which i wrote sai: 
import cv2
import pyautogui
# Screen resolution
screen_width = 1920
screen_height = 1080

# Set up video codec and writer
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("recorded.avi", fourcc, 20.0, (screen_width, screen_height))
while True:
# Capture the screen
img = pyautogui.screenshot()

 frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  
# Write the frame to the output
output.write(frame)  
# Break the loop on 'q' key press
 if cv2.waitKey(1) == ord("q"):
        break
# Release resources
output.release()
cv2.destroyAllWindows()



#This is the correct code: 

import datetime
import numpy as np
import cv2
import pyautogui

screen_width, screen_height = pyautogui.size()

time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = f'{time_stamp}.mp4'


fourcc = cv2.VideoWriter_fourcc(*'mp4v')  
captured_video = cv2.VideoWriter(file_name, fourcc, 15.0, (screen_width, screen_height))

while True:
    try:
        img = pyautogui.screenshot()
        img_np = np.array(img)
        img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

        
        captured_video.write(img_final)

        cv2.imshow('Screen Capture', img_final)

        if cv2.waitKey(10) == ord('z'):
            break
    except KeyboardInterrupt:
        break
captured_video.release()
cv2.destroyAllWindows()
