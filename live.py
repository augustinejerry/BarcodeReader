import cv2 
import numpy as np
from pyzbar import pyzbar
import cv2

def decode(image):
    # decodes all barcodes from an image
    decoded_objects = pyzbar.decode(image)
    for obj in decoded_objects:
        print("Type:", obj.type)
        print("Data:", obj.data)
        print()
    return image
  
if __name__ == "__main__":   
    while(True):
        url = 'http://192.168.2.12:8080/shot.jpg?rnd=729428'
        cap = cv2.VideoCapture(url)
        ret, frame = cap.read()
        if frame is not None:
            cv2.imshow('frame',frame)
            img = decode(frame)
        q = cv2.waitKey(100)
        if q == ord("q"):
            break
    cv2.destroyAllWindows()