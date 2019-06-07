""" convert Black and white"""
import cv2
img=cv2.imread('download.jpeg',0)

ret, bw=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow('output',bw)
cv2.waitKey(0)
cv2.destroyAllWindows()
