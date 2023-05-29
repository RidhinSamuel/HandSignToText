"""# import the opencv library
import cv2
  
f=open(f"Model/labels.txt")
r=f.readlines()
#print(read)
#define a video capture object
vid = cv2.VideoCapture(0)

while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
  
    # Display the resulting frame
    cv2.imshow('frame', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()"""
import os

os.mkdir("Data/W")
os