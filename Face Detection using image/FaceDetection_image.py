import cv2

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread("C:/Users/Kamalesh/Python program_ test/Virtual paint assignment/Face Detection/Face Detection - image/group.jpg")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgGray = cv2.imwrite("C:/Users/Kamalesh/Python program_ test/Virtual paint assignment/Face Detection/Face Detection - image/group_new.jpg",imgGray)

faces = faceCascade.detectMultiScale(imgGray,1.1,4)

while True:
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
        cv2.imshow("Result",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break