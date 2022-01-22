# El siguiente programa es el clásico juego tic-tac-toe o también llamado triqui
# Hecho por Alejandro Jaramillo :)

####################################################

import random
import time
import os


def ubicacionEsDigito(pos):
    if 49 <= ord(pos) <= 57:
        return True
    return False

# Verifica si la posicion ya ha sido marcada, devolviendo True o False
def ubicacionYaMarcada(IMP, pos):
    if IMP.tablero[str(pos)] != " ": return True
    return False


# Clase que contiene todos los menús y textos que se imprimen en la consola
class Triki():

    def __init__(self):
        # El tablero de juego es un diccionario, cada casilla contiene un turno sea "X" o "O"
        self.tablero = {    
            "1": " ",    "2": " ",    "3": " ",
            "4": " ",    "5": " ",    "6": " ",
            "7": " ",    "8": " ",    "9": " ",
            }
        self.TurnoActual = "X"

    def IMPlimpiarConsola(self):
        os.system("cls")

    def IMPmenuPrincipal(self):
        self.IMPlimpiarConsola()
        print("*** Bienvenido al clásico juego de TRIKI ***")
        print("    Selecciona el modo de juego: ")
        print("    1 - vs CPU Fácil")
        print("    2 - Juega contra un amigo")
        print("    3 - Salir")
        print("")
        return

    def IMPestadoJuego(self):
        self.IMPlimpiarConsola()
        print("** Triki **")
        print("")
        print(self.tablero["1"] + "  | " + self.tablero["2"] + " | " + self.tablero["3"])
        print("---+---+---")
        print(self.tablero["4"] + "  | " + self.tablero["5"] + " | " + self.tablero["6"])
        print("---+---+---")
        print(self.tablero["7"] + "  | " + self.tablero["8"] + " | " + self.tablero["9"])
        print("")
        return

    def IMPendGame(self):
        print(self.TurnoActual + " ha ganado - ¿Volver a jugar? S/N ")

    # Funcion que marca en el tablero, recibe la posicion y la marca (X u O)
    def anotarTurno(self, pos, xo):
        self.tablero[pos] = xo
        return

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
        tk.TurnoActual = "X"
        return

# Función que describe la lógica de la partida de triki y retorna True cuando finaliza la partida
def PartidaJVJ():
    tk.IMPestadoJuego()
    while True:
        pos = input(">> ")
        if (len(pos) == 1 and ubicacionEsDigito(str(pos)) == True and ubicacionYaMarcada(tk,str(pos)) == False):
            tk.anotarTurno(str(pos) , tk.TurnoActual)
            break
    tk.IMPestadoJuego()
    if(tk.hayGanador()):
        tk.IMPendGame()
        return True
    tk.cambiarTurno()

def PartidaJuegoCPU():
    pass

# Inicializamos la clase triki que contiene el tablero, turno actual
# y otras funciones bien chidoris
tk = Triki()

# Funcion que muestra el menu principal e inicia el modo de juego seleccionado
def MenuPartida():
    tk.IMPmenuPrincipal()
    while True:
        pos = input(">> ")
        if (pos == "1" or pos == "2"): break

    while True:
        if (PartidaJVJ()):
            ans = input(">> ")
            if(ans == "n" or ans == "N"): break
            else: tk.limpiarTablero()
            return

def main():
    while True:
        MenuPartida()

main()