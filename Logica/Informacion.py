from PIL import ImageTk, Image
from tkinter import ttk

import tkinter


def Interfaz():
    
    imagen = Image.open("Recursos\Iconos\Info.png")
    render = ImageTk.PhotoImage(imagen)
    
    fondo = ttk.Label(window, image=render)
    fondo.image = render
    fondo.pack()
    fondo.place(x = -1, y = -1)

    Titulo = ttk.Label(text="OpenCV (Open Source Computer Vision Library)")
    Titulo.pack()
    Titulo.place(x=260, y= 130)
    
    Informacion = ttk.Label(text="Es una biblioteca de software de visión artificial y machine learning open source\noriginalmente desarrollada por Intel.\nSe creó para proporcionar una infraestructura común para aplicaciones de visión\npor computadora y para acelerar el uso de la percepción de la máquina en\nlos productos comerciales.")
    Informacion.pack()
    Informacion.place(x=175, y= 165)
    
    Informacion2 = ttk.Label(text="Al ser un producto con licencia BSD, OpenCV facilita que las empresas utilicen y \nmodifiquen el código.")
    Informacion2.pack()
    Informacion2.place(x=175, y= 244)

    Informacion3 = ttk.Label(text="Estos algoritmos se pueden utilizar para:\n - Detectar y reconocer rostros\n - Identificar objetos\n - Clasificar acciones humanas en videos\n - Rastrear los movimientos de la cámara\n - Rastrear objetos en movimiento\n - Extraer modelos 3D de objetos \n - Producir nubes de puntos 3D a partir de cámaras estéreo\n - Unir imágenes para producir una alta resolución imagen de una escena completa\n - Buscar imágenes similares de una base de datos de imágenes\n - Eliminar ojos rojos de imágenes tomadas con flash\n - Seguir los movimientos oculares\n - Reconocer paisajes\n - Establecer marcadores para superponerlos con realidad aumentada\n - Entre otros ")
    Informacion3.pack()
    Informacion3.place(x=175, y= 278)

    Informacion4 = ttk.Label(text="Para más informacion visite la siguiente pagina: https://opencv.org/about/")
    Informacion4.pack()
    Informacion4.place(x=175, y= 518)    
if __name__ == '__main__':
    
    window = tkinter.Tk()
    window.title('Informacion')
    window.geometry("800x600")
    window.resizable(0,0)
    
    user = tkinter.StringVar()
    password = tkinter.StringVar()
    
    Interfaz()
    window.mainloop()