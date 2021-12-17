from PIL import ImageTk, Image
from xml.dom import minidom
from tkinter import ttk

import tkinter
import hashlib

import MenuSuperAdmin

users = minidom.parse("Recursos/Datos/usuarios.xml")
ventana = None

user = None
password = None
confirm = None
level = None

def Agregar():
    
    userName = user.get()
    userPassword = password.get()
    userConfirm = confirm.get()
    userLevel = level.get()[6:7]
    
    print(userLevel)
    
    encoded = hashlib.md5(userPassword.encode())
    resultado = encoded.hexdigest()
    
    if(len(userName) > 0 and len(userPassword) > 0):
    
        if(userPassword == userConfirm):
            
            nodo = users.createElement("usuario")
            
            userElement = users.createElement('username')
            userElement.appendChild(users.createTextNode(userName))
            
            nodo.appendChild(userElement)
            
            userElement = users.createElement('password')
            userElement.appendChild(users.createTextNode(resultado))
            
            nodo.appendChild(userElement)
            
            userElement = users.createElement('level')
            userElement.appendChild(users.createTextNode(userLevel))
            
            nodo.appendChild(userElement)
            
            usuarios = users.getElementsByTagName("usuarios")[0]
            usuarios.appendChild(nodo)
            
            #Archivo = open("Recursos/Datos/usuarios.xml", 'w')        
            #Archivo.write(usuarios.toxml())
          
def Volver():
    
    MenuSuperAdmin.Interfaz(ventana)
    
def Interfaz(window):
    
    global ventana
    global user
    global password
    global confirm
    global level
    
    ventana = window
    
    user = tkinter.StringVar()
    password = tkinter.StringVar()
    confirm = tkinter.StringVar()
    level = tkinter.StringVar()
    
    imagen = Image.open("Recursos\Iconos\RegistroUsuario.png")
    render = ImageTk.PhotoImage(imagen)
    
    fondo1 = ttk.Label(window, image=render)
    fondo1.image = render
    fondo1.pack()
    fondo1.place(x=-2, y=-2)
    
    entrada1 = ttk.Entry(window, textvariable=user)
    entrada1.place(width=240, height=30, x=297, y=105)
    
    entrada2 = ttk.Entry(window, textvariable=password)
    entrada2.place(width=240, height=30, x=297, y=180)
    entrada2['show'] = "*"
    
    entrada2 = ttk.Entry(window, textvariable=confirm)
    entrada2.place(width=240, height=30, x=297, y=255)
    entrada2['show'] = "*"
    
    levels = ttk.Combobox(window, values=["Nivel 0 (Usuario)", "Nivel 1 (Administrador)"], state="readonly", textvariable=level)
    levels.current(0)
    levels.place(width=240, height=30, x=297, y=330)
    
    boton1 = ttk.Button(text="AGREGAR", command=Agregar, state=tkinter.DISABLED)
    boton1.place(width=170, height=50, x=332, y=395)
    
    Boton2 = ttk.Button(text="Regresar", command=Volver)
    Boton2.place(width=100, height=30, x=30, y=550)
