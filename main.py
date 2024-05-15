import requests
import cv2
import numpy as np
import imutils

url = "http://10.80.80.10:8080/shot.jpg"

while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content),dtype=np.uint8)
    img = cv2.imdecode(img_arr, 1)
    cv2.imshow("Android Cam",img)
    
    if cv2.waitKey(1) == 27:
        break
    
cv2.destroyAllWindows()