from PIL import ImageTk, Image
from tkinter import ttk

import tkinter

import Informacion
import CrearUsuario
import ModificarUsuario
import Login

ventana = None

def Modificar():
    
    ModificarUsuario.Interfaz(ventana)
    
def Crear():
    
    CrearUsuario.Interfaz(ventana)

def Info():
    
    Informacion.Interfaz(ventana,1)

def CerrarSesion():
    
    Login.Interfaz(ventana)
    
def Interfaz(window):
    
    global ventana
    ventana = window
    
    imagen = Image.open("Recursos\Iconos\MenuAdmin.png")
    render = ImageTk.PhotoImage(imagen)
    
    fondo1 = ttk.Label(window, image=render)
    fondo1.image = render
    fondo1.pack()
    fondo1.place(x=-2, y=-2)
        
    boton1 = ttk.Button(text="Crear Usuario", command=Crear)
    boton1.place(width=194, height=193, x=50, y=114)

    boton2 = ttk.Button(text="Modificar Usuario", command=Modificar)
    boton2.place(width=194, height=193, x=303, y=115)
    
    boton3 = ttk.Button(text="Eliminar Usuario", state=tkinter.DISABLED)
    boton3.place(width=194, height=193, x=558, y=115)
    
    boton4 = ttk.Button(text="Informacion", command=Info)
    boton4.place(width=194, height=193, x=171, y=355)
    
    boton5 = ttk.Button(text="Configuracion", state=tkinter.DISABLED)
    boton5.place(width=194, height=193, x=427, y=356)
    
    Boton1 = ttk.Button(text="Cerrar Sesión", command=CerrarSesion)
    Boton1.place(width=100, height=30, x=30, y=550)