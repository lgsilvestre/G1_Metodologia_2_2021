from PIL import ImageTk, Image
from tkinter import ttk

import tkinter

import Algoritmo1
import Informacion

ventana = None
    
def Info():
    
    Informacion.Interfaz(ventana,0)

def Webcam():
    
    Algoritmo1.Webcam()

def Imagen():
    
    Algoritmo1.Imagen()

def Interfaz(window):
    
    global ventana
    ventana = window
        
    imagen = Image.open("Recursos\Iconos\MenuUsuario.png")
    render = ImageTk.PhotoImage(imagen)
    
    fondo1 = ttk.Label(window, image=render)
    fondo1.image = render
    fondo1.pack()
    fondo1.place(x=-2, y=-2)
        
    boton1 = ttk.Button(text="Detectar Rostro en Imagen", command=Imagen)
    boton1.place(width=194, height=193, x=170, y=114)

    boton2 = ttk.Button(text="Detectar Rostro en Video", command=Webcam)
    boton2.place(width=194, height=193, x=426, y=114)
    
    boton4 = ttk.Button(text="Informacion", command=Info)
    boton4.place(width=194, height=193, x=170, y=355)
    
    boton5 = ttk.Button(text="Configuración", state=tkinter.DISABLED)
    boton5.place(width=194, height=193, x=426, y=355)
    
    Boton1 = ttk.Button(text="Cerrar Sesión")
    Boton1.place(width=100, height=30, x=30, y=550)
    