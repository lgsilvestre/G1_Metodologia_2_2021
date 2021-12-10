from PIL import ImageTk, Image
from tkinter import ttk

import tkinter

import Informacion

ventana = None
    
def Info():
    
    Informacion.Interfaz(ventana,1)
    
def Interfaz(window):
    
    global ventana
    ventana = window
    
    imagen = Image.open("Recursos\Iconos\MenuAdmin.png")
    render = ImageTk.PhotoImage(imagen)
    
    fondo1 = ttk.Label(window, image=render)
    fondo1.image = render
    fondo1.pack()
    fondo1.place(x=-2, y=-2)
        
    boton1 = ttk.Button(text="Crear Usuario")
    boton1.place(width=194, height=193, x=50, y=114)

    boton2 = ttk.Button(text="Modificar Usuario")
    boton2.place(width=194, height=193, x=303, y=115)
    
    boton3 = ttk.Button(text="Eliminar Usuario")
    boton3.place(width=194, height=193, x=558, y=115)
    
    boton4 = ttk.Button(text="Informacion", command=Info)
    boton4.place(width=194, height=193, x=171, y=355)
    
    boton5 = ttk.Button(text="Configuracion", state=tkinter.DISABLED)
    boton5.place(width=194, height=193, x=427, y=356)