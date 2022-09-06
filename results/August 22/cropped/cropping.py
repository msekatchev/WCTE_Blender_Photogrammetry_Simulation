import cv2
import numpy as np

for i in [0,15,30,45,60,75,90]:
    img = cv2.imread("1m"+str(i)+"deg.png")
    print(img.shape)
    cv2.imshow("crop"+str(i),img[450:650, 875:1050])
    cv2.imwrite("1m"+str(i)+"deg-cropped.png", img[450:650, 875:1050])
cv2.waitKey(0)
cv2.destroyAllWindows()

