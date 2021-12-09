from PIL import ImageTk, Image
from tkinter import ttk

import tkinter

def Webcam():
    print("")
    
def Imagen(): 
    print("")
    
def Interfaz():
        
    imagen = Image.open("Recursos\Iconos\PlaceHolder.png")
    render = ImageTk.PhotoImage(imagen)
    
    fondo1 = ttk.Label(window, image=render)
    fondo1.image = render
    fondo1.pack()
    fondo1.place(x=-1, y=-1)
        
    boton1 = ttk.Button(text="Crear Usuario", command=Imagen)
    boton1.place(width=200, height=200, x=47, y=210)

    boton2 = ttk.Button(text="Modificar Usuario", command=Webcam)
    boton2.place(width=200, height=200, x=300, y=210)
    
    boton3 = ttk.Button(text="Eliminar Usuario")
    boton3.place(width=200, height=200, x=557, y=210)
    
if __name__ == '__main__':
    
    window = tkinter.Tk()
    window.title('Facial Recognition')
    window.geometry("800x600")
    window.resizable(0,0)
    
    user = tkinter.StringVar()
    password = tkinter.StringVar()
    
    Interfaz()
    window.mainloop()