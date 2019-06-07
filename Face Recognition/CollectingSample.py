import cv2
import numpy as np
#Collected samples for this program
# first we need something that our model should recognize that yes this is face human face
#so we can use clasifier it will be insie cv2 folder it having eye, fullbody, smile, superbody etc
# here we have to use fronttalface_default.xml
face_classifier=cv2.CascadeClassifier('/Users/745453/anaconda3/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')

# we need extract the face values

def face_extractor(img):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_classifier.detectMultiScale(gray,1.3,5)
    if faces is():
        return None
    for(x,y,w,h) in faces:
        cropped_face=img[y:y+h,x:x+w]
        return cropped_face

    
    
cap=cv2.VideoCapture(0)
count=0

while True:
    ret,frame=cap.read()
    if face_extractor(frame) is not None:
        count+=1
        face=cv2.resize(face_extractor(frame),(200,200))
        face= cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
        file_name_path='/Users/745453/Documents/facerec/user'+str(count)+'.jpg'
        cv2.imwrite(file_name_path,face)
        cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,55,0),2)
        cv2.imshow('Fca2',face)
        
    else:
        print("face not found")
        pass
    if cv2.waitKey(1)==13 or count==100:
        break
cap.release()
cv2.destroyAllWindows()


print('Collected samples completed')
