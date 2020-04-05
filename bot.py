import numpy as np
import PIL
import cv2
import pyautogui
import time
from PIL import ImageGrab
from directkeys import PressKey,ReleaseKey, W,A,S,D


def draw_lines(img,lines):
    try:
        for line in lines:
            coord= line[0]
            cv2.line(img,(coord[0],coord[1]),(coord[2],coord[3]),[255,255,255],3)
    except:
            pass

def roi(img,vertices):
    mask=np.zeros_like(img)
    cv2.fillPoly(mask,vertices,255)
    masked=cv2.bitwise_and(img,mask)
    return  masked


def process_img(original_image):

    processed_img = cv2.cvtColor(original_image,cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img,threshold1=200,threshold2=300)
    processed_img=cv2.GaussianBlur(processed_img,(5,5),0)
    vertices = np.array([[10,500],[10,300],[300,200],[500,200],[800,300],[800,500]])

    process_img=roi(processed_img,[vertices])

    #krawedzie
    lines = cv2.HoughLinesP(processed_img,1,np.pi/180,180,np.array([]),20,15)
    draw_lines(processed_img,lines)

    return processed_img

for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)

#print('down')
#PressKey(W)
#time.sleep(i+1)
#print('up')
#ReleaseKey(W)



last_time = time.time()
while(True):
    screen = np.array(ImageGrab.grab(bbox=(0,40,800,640)))
    new_screen = process_img(screen)
    print ('Klatki {}'.format(time.time()-last_time))
    last_time= time.time()
    cv2.imshow('window',new_screen)
    #kolor cv2.imshow('window',cv2.cvtColor(screen,cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break



