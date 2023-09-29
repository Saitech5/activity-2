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




//This is the code which i wrote sai: 
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
# Introduce a typo in the following line
 frmae = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Typo: Should be 'frame', not 'frmae'
# Write the frame to the output
output.write(frmae)  # Typo: Should be 'frame', not 'frmae'
# Break the loop on 'q' key press

