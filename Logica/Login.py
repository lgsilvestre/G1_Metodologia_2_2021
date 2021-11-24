from PIL import ImageTk, Image
from tkinter import ttk

import tkinter
import pathlib

def Verificar():
    
    print(user.get())
    print(password.get())

def Login():
    
    origen = str(pathlib.Path().resolve())
    path = origen[:len(origen)-6]
    
    imagen = Image.open(path+"Recursos\\Iconos\\fondo_login.png")
    render = ImageTk.PhotoImage(imagen)
    
    fondo1 = ttk.Label(window, image=render)
    fondo1.image = render
    fondo1.pack()
    fondo1.place(x=-1, y=-1)
    
    entrada1 = ttk.Entry(window, textvariable=user)
    entrada1.place(width=240, height=30, x=280, y=305)
    
    entrada2 = ttk.Entry(window, textvariable=password)
    entrada2.place(width=240, height=30, x=280, y=365)
    
    boton1 = ttk.Button(text="Iniciar Sesión", command=Verificar)
    boton1.place(width=170, height=50, x=315, y=425)

if __name__ == '__main__':
    
    window = tkinter.Tk()
    window.title('Facial Recognition')
    window.geometry("800x600")
    window.resizable(0,0)
    
    user = tkinter.StringVar()
    password = tkinter.StringVar()
    
    Login()
    
    window.mainloop()