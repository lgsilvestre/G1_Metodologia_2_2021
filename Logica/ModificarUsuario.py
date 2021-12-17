from PIL import ImageTk, Image
from xml.dom import minidom
from xml.etree import ElementTree
from tkinter import ttk

import tkinter
import hashlib

import MenuSuperAdmin

usersMini = minidom.parse("Recursos/Datos/usuarios.xml")
usersTree = ElementTree.parse("Recursos/Datos/usuarios.xml")

ventana = None

user = None
password = None
confirm = None
level = None

def Modificar():
    
    userName = user.get()
    userPassword = password.get()
    userConfirm = confirm.get()
    userLevel = level.get()[6:7]
    
    ConfirmEncoded = hashlib.md5(userConfirm.encode())
    ConfirmResultado = ConfirmEncoded.hexdigest()
    
    elementos = usersTree.findall('usuario')
    
    adminsPass = []
    
    for elemento in elementos:
        
        sysName, sysPass, sysLevel = list(elemento)
        
        if(sysLevel.text == "1"):
            adminsPass.append(sysPass.text)
            
    if(len(userPassword) == 0):
        
        for elemento in elementos:
            
            sysName, sysPass, sysLevel = list(elemento)
            
            if(sysName.text == userName):
                
                for passAdmin in adminsPass:
                    
                    if(ConfirmResultado == passAdmin):
                        
                        sysLevel.text = userLevel
        
    else:
        
        PassEncoded = hashlib.md5(userPassword.encode())
        PassResultado = PassEncoded.hexdigest()
        
        for elemento in elementos:
            
            sysName, sysPass, sysLevel = list(elemento)
            
            if(sysName.text == userName):
                
                for passAdmin in adminsPass:
                    
                    if(ConfirmResultado == passAdmin):
                        
                        sysPass.text = PassResultado
                        sysLevel.text = userLevel
                        
    usersTree.write("Recursos/Datos/usuarios.xml")
    
    password.set("")
    confirm.set("")
    
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

    imagen = Image.open("Recursos\Iconos\EditarUsuario.png")
    render = ImageTk.PhotoImage(imagen)

    fondo1 = ttk.Label(window, image=render)
    fondo1.image = render
    fondo1.pack()
    fondo1.place(x=-2, y=-2)
    
    usuarios = usersMini.getElementsByTagName("usuario")
    lista = []
    
    for usuario in usuarios:
        
        systemName = usuario.getElementsByTagName("username")[0]
        lista.append(systemName.firstChild.data)

    selUsers = ttk.Combobox(window, values=lista, state="readonly", textvariable=user)
    selUsers.current(0)
    selUsers.place(width=240, height=30, x=297, y=105)
    
    levels = ttk.Combobox(window, values=["Nivel 0 (Usuario)", "Nivel 1 (Administrador)"], state="readonly", textvariable=level)
    levels.current(0)
    levels.place(width=240, height=30, x=297, y=180)

    entrada1 = ttk.Entry(window, textvariable=password)
    entrada1.place(width=240, height=30, x=297, y=255)
    entrada1['show'] = "*"
    
    entrada2 = ttk.Entry(window, textvariable=confirm)
    entrada2.place(width=240, height=30, x=297, y=330)
    entrada2['show'] = "*"

    boton1 = ttk.Button(text="MODIFICAR", command=Modificar)
    boton1.place(width=170, height=50, x=332, y=395)
    
    Boton2 = ttk.Button(text="Regresar", command=Volver)
    Boton2.place(width=100, height=30, x=30, y=550)