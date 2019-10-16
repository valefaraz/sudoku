from sudoku import Sudoku
#from API import API
#import sys
#import math


class UserInput():

    def ingreso_numero(self, number, tamaño):
        if(number > 0 and number <= tamaño):
            return True
        else:
            return False

    def ingreso_coordenadas(self, fila, columna, tamaño):
        if(fila > 0 and fila <= tamaño and columna > 0 and columna <= tamaño):
            return True
        else:
            return False

    

    def dimension(self, tamaño):
        return (tamaño != 4 and tamaño != 9)
    
    def ingresar_dimension(self):
        tamaño = 0
        while not self.dimension(tamaño):
            try:
                tamaño = int(input("Ingrese el tamaño sudoku (4 o 9): "))
                if (self.dimension(tamaño)):
                    return tamaño
                print("Ingresaste un tamaño no permitido, intentalo de nuevo")
            except ValueError:
                print("Ingresaste un tamaño no permitido, intentalo de nuevo")
    
    def play(self):
        self.dimension() # donde se guarda la dimension???
        # crear sudoku...
        while not jjj.juego_terminado():
            # mostrar tablero
            print(jjj.get_board())
            # ingresar ...
            # poner en el sudoku...


if __name__ == "__main__":
    u = UserInput()
    u.play()
