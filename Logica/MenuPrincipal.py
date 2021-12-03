from PIL import ImageTk, Image
from tkinter import ttk

import tkinter

def Interfaz():
        
    imagen = Image.open("Interfaz 2.png")
    render = ImageTk.PhotoImage(imagen)
    
    fondo1 = ttk.Label(window, image=render)
    fondo1.image = render
    fondo1.pack()
    fondo1.place(x=-1, y=-1)
        
    boton1 = ttk.Button(text="Detectar Rostro en Imagen")
    boton1.place(width=200, height=200, x=47, y=110)

    boton2 = ttk.Button(text="Detectar Rostro en Video")
    boton2.place(width=200, height=200, x=300, y=110)
    
    boton3 = ttk.Button(text="Lista Peronas Registradas")
    boton3.place(width=200, height=200, x=557, y=110)
    
    boton4 = ttk.Button(text="Sobre Algoritmos")
    boton4.place(width=200, height=200, x=168, y=350)
    
    boton5 = ttk.Button(text="Configuración")
    boton5.place(width=200, height=200, x=425, y=350)
    
if __name__ == '__main__':
    
    window = tkinter.Tk()
    window.title('Facial Recognition')
    window.geometry("800x600")
    window.resizable(0,0)
    
    user = tkinter.StringVar()
    password = tkinter.StringVar()
    
    Interfaz()
    
    window.mainloop()