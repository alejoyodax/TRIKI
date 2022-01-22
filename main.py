from tkinter import *
import tkinter
import time

# Propiedades de la ventana principal
root=Tk()
root.title("Triki")
root.iconbitmap("game.ico")

# Frame para el tablero
frameTablero=Frame(root)
#frameTablero.pack(fill="both", expand=1)
frameTablero.grid(row=0, column=0)

# Se cargan las imágenes correspondientes a X y O
img_x=PhotoImage(file="x.png")
img_o=PhotoImage(file="o.png")
img_nada=PhotoImage(file="nada.png")

labelFinJuego=Label(frameTablero, text="")
labelFinJuego.grid(row=5, column=0)

b10=Button(frameTablero, text="R", command=lambda:Triqui.reiniciarJuego())
b10.grid(row=5, column=4, sticky="e")


class Triki():

    def __init__(self):
        # El tablero de juego es un diccionario, cada casilla contiene un turno sea "X" o "O"
        self.tablero = {    
            "1": " ",    "2": " ",    "3": " ",
            "4": " ",    "5": " ",    "6": " ",
            "7": " ",    "8": " ",    "9": " ",
            }
        self.TurnoActual = "X"

    # Funcion que marca en el tablero, recibe la posicion y la marca (X u O)
    def marcarTablero(self, pos, boton):
        self.tablero[pos] = self.TurnoActual
        print(self.tablero)

        if self.TurnoActual == "X":
            boton.config(image=img_x)
        else:
            boton.config(image=img_o)
        
        if self.hayGanador() == True:
            self.deshabilitarBotones()
            labelFinJuego.config(text="FIN DEL JUEGO")
            #self.habilitarBotones()
            #self.limpiarBotones()


        self.cambiarTurno()



        return

    def deshabilitarBotones(self):
        b1.config(state="disabled")
        b2.config(state="disabled")
        b3.config(state="disabled")
        b4.config(state="disabled")
        b5.config(state="disabled")
        b6.config(state="disabled")
        b7.config(state="disabled")
        b8.config(state="disabled")
        b9.config(state="disabled")

    def reiniciarJuego(self):
        b1.config(state="active", image=img_nada)
        b2.config(state="active", image=img_nada)
        b3.config(state="active", image=img_nada)
        b4.config(state="active", image=img_nada)
        b5.config(state="active", image=img_nada)
        b6.config(state="active", image=img_nada)
        b7.config(state="active", image=img_nada)
        b8.config(state="active", image=img_nada)
        b9.config(state="active", image=img_nada)
        self.limpiarTablero()
        labelFinJuego.config(text="")

    def limpiarBotones(self):
        b1.config(image=img_nada)
        b2.config(image=img_nada)
        b3.config(image=img_nada)
        b4.config(image=img_nada)
        b5.config(image=img_nada)
        b6.config(image=img_nada)
        b7.config(image=img_nada)
        b8.config(image=img_nada)
        b9.config(image=img_nada)

    # Funcion que verifica si alguien gana devolviendo True
    def hayGanador(self):
        if self.tablero["1"] == self.tablero["2"] == self.tablero["3"] != " " : return True
        if self.tablero["4"] == self.tablero["5"] == self.tablero["6"] != " " : return True
        if self.tablero["7"] == self.tablero["8"] == self.tablero["9"] != " " : return True

        if self.tablero["1"] == self.tablero["4"] == self.tablero["7"] != " " : return True
        if self.tablero["2"] == self.tablero["5"] == self.tablero["8"] != " " : return True
        if self.tablero["3"] == self.tablero["6"] == self.tablero["9"] != " " : return True

        if self.tablero["1"] == self.tablero["5"] == self.tablero["9"] != " " : return True
        if self.tablero["3"] == self.tablero["5"] == self.tablero["7"] != " " : return True
        return False

    def cambiarTurno(self):
        if self.TurnoActual == "X":
            self.TurnoActual = "O"
        else: self.TurnoActual = "X"

    def limpiarTablero(self):
        for n in range(0,9):
            self.tablero[str(n+1)] = " "
        self.TurnoActual = "X"
        return


Triqui=Triki()

# Objetos que funcionan como lineas horizontales y verticales

vert1=Canvas(frameTablero, border=0)
vert1.grid(row=0, column=1, rowspan=5, columnspan=1, sticky="n")
vert1.config(bg="gray", width=10, height=326, borderwidth=-2)

vert1=Canvas(frameTablero, border=0)
vert1.grid(row=0, column=3, rowspan=5, columnspan=1, sticky="n")
vert1.config(bg="gray", width=10, height=326, borderwidth=-2)

hor1=Canvas(frameTablero)
hor1.grid(row=1, column=0, rowspan=1, columnspan=5, sticky="w")
hor1.config(bg="gray", width=326, height=10, borderwidth=-2)

hor1=Canvas(frameTablero)
hor1.grid(row=3, column=0, rowspan=1, columnspan=5, sticky="w")
hor1.config(bg="gray", width=326, height=10, borderwidth=-2)


# ------------- LINEA 1 --------------#

b1=Button(frameTablero, width=100, height=100, image=img_nada, command=lambda: Triqui.marcarTablero("1", b1))
b1.grid(row=0, column=0)
b1.config(background="white", border=0)

b2=Button(frameTablero, width=100, height=100, image=img_nada, command=lambda: Triqui.marcarTablero("2", b2))
b2.grid(row=0, column=2)
b2.config(background="white", border=0)

b3=Button(frameTablero, width=100, height=100, image=img_nada, command=lambda: Triqui.marcarTablero("3", b3))
b3.grid(row=0, column=4)
b3.config(background="white", border=0)

# ----------------- LINEA 2 --------------#

b4=Button(frameTablero, width=100, height=100, image=img_nada, command=lambda: Triqui.marcarTablero("4", b4))
b4.grid(row=2, column=0)
b4.config(background="white", border=0, )

b5=Button(frameTablero, width=100, height=100, image=img_nada, command=lambda: Triqui.marcarTablero("5", b5))
b5.grid(row=2, column=2)
b5.config(background="white", border=0)

b6=Button(frameTablero, width=100, height=100, image=img_nada, command=lambda: Triqui.marcarTablero("6", b6))
b6.grid(row=2, column=4)
b6.config(background="white", border=0)

# ----------------- LINEA 3 --------------#

b7=Button(frameTablero, width=100, height=100, image=img_nada, command=lambda: Triqui.marcarTablero("7", b7))
b7.grid(row=4, column=0)
b7.config(background="white", border=0, )

b8=Button(frameTablero, width=100, height=100, image=img_nada, command=lambda: Triqui.marcarTablero("8", b8))
b8.grid(row=4, column=2)
b8.config(background="white", border=0)

b9=Button(frameTablero, width=100, height=100, image=img_nada, command=lambda: Triqui.marcarTablero("9", b9))
b9.grid(row=4, column=4)
b9.config(background="white", border=0)


root.mainloop()

# --------------------- Fin de la creación de GUI ---------------------- #
