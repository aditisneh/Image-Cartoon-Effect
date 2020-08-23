import cv2
import numpy as np

img = cv2.imread("C:/Users/HP/Downloads/mypic.jpg")
#Edges
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
blurred_img = cv2.medianBlur(img,5)

#edges = cv2.Canny(img, 75, 150)

#color
color = cv2.bilateralFilter(img, 9, 300, 300)

#cartoon
cartoon = cv2.bitwise_and(color, color, mask=edges)
cv2.imshow("Image", img)
#cv2.imshow("blur",blurred_img)
#cv2.imshow("Gray",gray)
#cv2.imshow("Edges", edges)
#cv2.imshow("color", color)
cv2.imshow("Cartoon", cartoon)

cv2.waitKey(0)
cv2.destroyAllWindows()