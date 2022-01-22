
from tkinter import *
import tkinter

# Propiedades de la ventana principal
root=Tk()
root.title("Triki")
root.iconbitmap("game.ico")

# Frame para el tablero
frameTablero=Frame(root)
#frameTablero.pack(fill="both", expand=1)
frameTablero.grid(row=0, column=0)

img_x=PhotoImage(file="x.png")
img_o=PhotoImage(file="o.png")
img_nada=PhotoImage(file="nada.png")

turno="x"
def marcarTablero(boton):
    if turno == "x":
        boton.config(image=img_x)
    else:
        boton.config(image=img_o)
    

b1=Button(frameTablero, command=lambda: marcarTablero(b1), image=img_nada)
b1.grid(row=0, column=0)
b1.config(width=100, height=100)

b2=Button(frameTablero, command=lambda:marcarTablero(b2), image=img_nada)
b2.grid(row=0, column=1)
b2.config(width=100, height=100)


















root.mainloop()