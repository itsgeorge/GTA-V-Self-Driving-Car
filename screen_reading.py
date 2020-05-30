# inspiration:
# https://pythonprogramming.net/game-frames-open-cv-python-plays-gta-v/
# 
# 
# let's grab screens 

import numpy as np
from PIL import ImageGrab
import cv2
import time
import mss 

def process_img(image):
    original_image = image
    # convert to gray
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # edge detection
    processed_img =  cv2.Canny(processed_img, threshold1 = 200, threshold2=300)
    return processed_img

def main():
    if input("Use MSS? yes/no") in ('yes', 'Yes'):
        use_mss = True
    else:
        use_mss = False

    if use_mss:
        sct = mss.mss()

    last_time = time.time()

     # TODO: asssess whether we can use higher resolution for better data
    box = (0, 40, 800, 640)  # bounding box tuple is (left_x, top_y, right_x, bottom_y)
    # 800 by 600 windowed mode, 40 px in tuple accounts for menu bar
    title = 'GTA V Self Driving Window'
    while True:
        if  use_mss:
            screen = np.array(sct.grab(box))
        else:
            screen =  np.array(ImageGrab.grab(bbox=box))
        # print('Frame took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        new_screen = process_img(screen)
        cv2.imshow(title, new_screen)
        #cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

main()