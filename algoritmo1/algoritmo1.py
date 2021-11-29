import cv2

face_cascade = cv2.CascadeClassifier('frontalface.xml')
cap = cv2.VideoCapture(3, cv2.CAP_DSHOW)

while cap.isOpened():
    
    frame = cap.read()[1]
    image = cv2.resize(frame,(320,180))

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y , w ,h) in faces:
        cv2.rectangle(image, (x,y), (x+w, y+h), (255, 0 , 0), 3)
    
    cv2.imshow('img', image)
    
    if cv2.waitKey(1) & 0xFF == ord('q'): #Para salir apretar Q
        break

cap.release()
cv2.destroyAllWindows()