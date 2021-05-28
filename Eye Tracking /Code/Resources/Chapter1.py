import cv2
#print(cv2._version_)

img = cv2.imread("Resources/test.png")
cv2.imshow("Output",img)
cv2.waitKey(0)

