import cv2
import time

def Deteccion():
    
    face_cascade = cv2.CascadeClassifier('Recursos/Datos/frontalface.xml')
    cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
    
    cont = 0
    
    while cap.isOpened():
        
        frame = cap.read()[1]
        image = cv2.resize(frame,(480,270))
    
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
        for (x, y , w ,h) in faces:
            
            cv2.rectangle(image, (x,y), (x+w, y+h), (255, 0 , 0), 2)
            
            if(cont < 15):
                
                name = "testA"
                face = gray[y:y + h, x:x + w]
                face_resize = cv2.resize(face, ((x+w)-x,(y+h)-y))
                cv2.imwrite('% s/% s.png' % ("Recursos\Caras\\", str(name) + str(cont)), face_resize)
                cont += 1
            
        cv2.imshow('Reconocimiento', image)
        
        if cv2.waitKey(1) & 0xFF == ord('q'): # Para salir apretar 'Q'
            break
        
        time.sleep(0.1)
    
    cap.release()
    cv2.destroyAllWindows()