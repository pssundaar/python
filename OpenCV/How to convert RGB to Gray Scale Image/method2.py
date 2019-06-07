import cv2
img=cv2.imread('download.jpeg')
cv2.imshow('output',img)
cv2.waitKey(0)
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('GRAY',gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
