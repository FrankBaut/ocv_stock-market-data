import mss
import numpy as np
import time
import cv2
import numpy
import pytesseract
import matplotlib.pyplot as plt
from datetime import datetime
from time import mktime

#Import tesseract from text recognition
pytesseract.pytesseract.tesseract_cmd =  r'/home/frank/anaconda3/bin/tesseract'

file = open("prices.txt","a") #open a file to save records
prec = []
with mss.mss() as sct:
    # Part of the screen to capture(a pixel box)
    monitor = {"top": 393, "left": 52, "width": 155, "height": 50}
    while "Screen capturing":
        last_time = time.time() #get time
        # Get raw pixels from the screen, save it to a Numpy array
        img = numpy.array(sct.grab(monitor))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(img)
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        prec.append('{:<10}{:<10}{:<10}{:<10}'.format('time: ',current_time,'price: ',text))
        file.writelines(prec)
        print('{:<10}{:<10}{:<10}{:<10}'.format('time: ',current_time,'price: ',text))
        cv2.imshow('Price',img)
        #waitKey to fix frames per second
        # Press "q" to quit
        if cv2.waitKey(800) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
