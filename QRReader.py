#Assignment 10

#Contact Tracing App
#	- Create a python program that will read QRCode using your webcam
#	- You may use any online QRCode generator to create QRCode
#	- All personal data are in QRCode 
#	- You may decide which personal data to include
#	- All data read from QRCode should be stored in a text file including the date and time it was read

#Note: 
#	- Search how to generate QRCode
#	- Search how to read QRCode using webcam
#	- Search how to create and write to text file
#	- Your source code should be in github before Feb 19
#	- Create a demo of your program (1-2 min) and send it directly to my messenger.

import cv2
import numpy as np
from pyzbar.pyzbar import decode
from datetime import datetime


capture = cv2.VideoCapture(0)               # for the use of webcam
capture.set(3,640)
capture.set(4,480)

while True:
    success, image = capture.read()
    for code in decode(image):                  # to decode the image into strings
        Data = code.data.decode('utf-8')
        qrshapes = np.array([code.polygon], np.int32)     # used to create a shape around the qr 
        qrshapes = qrshapes.reshape((-1,1,2))
        cv2.polylines(image,[qrshapes], True, (57,255,20), 5)
        DateAndTime = datetime.now()                            # for getting the date and time
        FormatOfDateAndTime = DateAndTime.strftime("Date: %B %d, %Y \nTime: %H:%M:%S")




