from tkinter import filedialog

import os
import cv2
import time

cap = None
filename = ""

def Webcam():
    
    global cap
    global filename
    
    cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
    filename = ""
    
    Deteccion()
    
def Imagen():
    
    global cap
    global filename
    
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("PNG files","*.png*"),("JPG files","*.jpg*")))
    cap = None
    
    Deteccion()

def Deteccion():
    
    if not os.path.exists("Recursos\Caras\\"):
        os.makedirs("Recursos\Caras\\")
    
    face_cascade = cv2.CascadeClassifier('Recursos/Datos/frontalface.xml')
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    working = False
    cont = 0
    
    while True:
        
        if(filename != ""):
            frame = cv2.imread(filename)
            working = True
            
        if(cap != None):
            frame = cap.read()[1]
            working = True
            
        if(working):
            
            ratio = 270 / len(frame)
            width = int(len(frame[0]) * ratio)
            height = int(len(frame) * ratio)
            
            image = cv2.resize(frame,(width,height))
    
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            
            for (x, y , w ,h) in faces:
                
                cv2.rectangle(image, (x,y), (x+w, y+h), (255, 0 , 0), 2)
                
                face = gray[y:y + h, x:x + w]
                face_resize = cv2.resize(face, ((x+w)-x,(y+h)-y))
                
                if(cont < 15):
                    
                    name = "testA"
                    cv2.imwrite('% s/% s.png' % ("Recursos\Caras\\", str(name) + str(cont)), face_resize)
                    cont += 1
                
            rostros = "Rostros Detectados: " + str(len(faces))
            cv2.rectangle(image, (5,5), (200,25), (0,0,0), -1)
            cv2.putText(image, rostros, (10,20), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
            cv2.imshow('Reconocimiento (Presionar Q para Salir)', image)
            
            if cv2.waitKey(1) & 0xFF == ord('q'): # Para salir apretar 'Q'
                break
            
            time.sleep(0.1)
            
        else:
            break
    
    if(cap != None):
        cap.release()
        
    cv2.destroyAllWindows()