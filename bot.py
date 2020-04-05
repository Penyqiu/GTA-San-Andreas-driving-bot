import numpy as np
import PIL
import cv2
import time
from PIL import ImageGrab

def process_img(original_image):

    processed_img = cv2.cvtColor(original_image,cv2.COLOR_BGR2GRAY)

last_time = time.time()
while(True):
    screen = np.array(ImageGrab.grab(bbox=(0,40,800,640)))
    print ('Klatki {}'.format(time.time()-last_time))
    last_time= time.time()
    cv2.imshow('window',cv2.cvtColor(screen,cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break



