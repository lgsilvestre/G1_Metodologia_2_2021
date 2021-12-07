from PIL import ImageTk, Image
from tkinter import ttk

import Algoritmo1

def Webcam():
    
    Algoritmo1.Webcam()

def Imagen():
    
    Algoritmo1.Imagen()

def Interfaz(window):
        
    imagen = Image.open("Recursos\Iconos\MenuPrincipal.png")
    render = ImageTk.PhotoImage(imagen)
    
    fondo1 = ttk.Label(window, image=render)
    fondo1.image = render
    fondo1.pack()
    fondo1.place(x=-1, y=-1)
        
    boton1 = ttk.Button(text="Detectar Rostro en Imagen", command=Imagen)
    boton1.place(width=200, height=200, x=47, y=110)

    boton2 = ttk.Button(text="Detectar Rostro en Video", command=Webcam)
    boton2.place(width=200, height=200, x=300, y=110)
    
    boton3 = ttk.Button(text="Lista Peronas Registradas")
    boton3.place(width=200, height=200, x=557, y=110)
    
    boton4 = ttk.Button(text="Sobre Algoritmos")
    boton4.place(width=200, height=200, x=168, y=350)
    
    boton5 = ttk.Button(text="Configuración")
    boton5.place(width=200, height=200, x=425, y=350)
    