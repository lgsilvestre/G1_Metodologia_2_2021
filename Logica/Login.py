from PIL import ImageTk, Image
from xml.dom import minidom
from tkinter import ttk

import tkinter
import hashlib

import MenuPrincipal

users = minidom.parse("Recursos/Datos/usuarios.xml")

def Verificar():
    
    userName = user.get()
    userPassword = password.get()
    
    encoded = hashlib.md5(userPassword.encode())
    resultado = encoded.hexdigest()
    
    usuarios = users.getElementsByTagName("usuario")
    
    for usuario in usuarios:
        
        systemName = usuario.getElementsByTagName("username")[0]
        systemPassword = usuario.getElementsByTagName("password")[0]
        
        if(systemName.firstChild.data == userName):
            
            if(systemPassword.firstChild.data == resultado):
                MenuPrincipal.Interfaz(window)
                
    user.set("")
    password.set("")

def Interfaz():
    
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

if __name__ == '__main__':
    
    window = tkinter.Tk()
    window.title('Facial Recognition')
    window.geometry("800x600")
    window.resizable(0,0)
    
    user = tkinter.StringVar()
    password = tkinter.StringVar()
    
    Interfaz()
    window.mainloop()