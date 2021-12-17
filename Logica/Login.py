from PIL import ImageTk, Image
from xml.dom import minidom
from tkinter import ttk

import tkinter
import hashlib

import MenuPrincipal
import MenuSuperAdmin

users = minidom.parse("Recursos/Datos/usuarios.xml")
ventana = None

user = None
password = None

def Verificar():
    
    userName = user.get()
    userPassword = password.get()
    
    encoded = hashlib.md5(userPassword.encode())
    resultado = encoded.hexdigest()
    
    usuarios = users.getElementsByTagName("usuario")
    
    for usuario in usuarios:
        
        systemName = usuario.getElementsByTagName("username")[0]
        systemPassword = usuario.getElementsByTagName("password")[0]
        systemLevel = usuario.getElementsByTagName("level")[0]
        
        if(systemName.firstChild.data == userName):
            
            if(systemPassword.firstChild.data == resultado):
                
                if(systemLevel.firstChild.data == "1"):
                    MenuSuperAdmin.Interfaz(ventana)
                    
                if(systemLevel.firstChild.data == "0"):
                    MenuPrincipal.Interfaz(ventana)
                
    user.set("")
    password.set("")

def Interfaz(window):
    
    global ventana
    global user
    global password
    
    ventana = window
    user = tkinter.StringVar()
    password = tkinter.StringVar()
    
    imagen = Image.open("Recursos\Iconos\MenuAcceso.png")
    render = ImageTk.PhotoImage(imagen)
    
    fondo1 = ttk.Label(window, image=render)
    fondo1.image = render
    fondo1.pack()
    fondo1.place(x=-2, y=-2)
    
    entrada1 = ttk.Entry(window, textvariable=user)
    entrada1.place(width=240, height=30, x=297, y=245)
    
    entrada2 = ttk.Entry(window, textvariable=password)
    entrada2.place(width=240, height=30, x=297, y=320)
    entrada2['show'] = "*"
    
    boton1 = ttk.Button(text="ACCEDER", command=Verificar)
    boton1.place(width=170, height=50, x=332, y=395)