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
        return (tamaño == 4 or tamaño == 9)
    
    def ingresar_dimension(self):
        tamaño = 0
        while self.dimension(tamaño) is False:
            try:
                tamaño = int(input("Ingrese el tamaño sudoku (4 o 9): "))
                if (self.dimension(tamaño)):
                    return tamaño
                print("Ingresaste un tamaño no permitido, intentalo de nuevo")
            except ValueError:
                print("Ingresaste un tamaño no permitido, intentalo de nuevo")
    
    def ingresar_valor(self, tabla, tamaño):
        self.showTable(tabla, tamaño)
        number = 0
        fila = 0
        columna = 0
        while not self.ingreso_numero(number, tamaño) or not self.ingreso_coordenadas(fila,
                                                                                    columna,
                                                                                    tamaño):
            try:
                fila = int(input("\n\nFila: "))
                columna = int(input("Columna: "))
                number = int(input("Valor de la casilla: "))
            except ValueError:
                pass
            if (self.ingreso_numero(number, tamaño) and self.ingreso_coordenadas(fila,
                                                                                columna,
                                                                                tamaño)):
                uinput = [fila - 1, columna - 1, number]
                return uinput
            print("Ingresaste un valor no permitido, intentalo de nuevo")

    
    def play(self):
        jugar = Sudoku(["53xx7xxxx",
                            "6xx195xxx",
                            "x98xxxx6x",
                            "8xxx6xxx3",
                            "4xx8x3xx1",
                            "7xxx2xxx6",
                            "x6xxxx28x",
                            "xxx419xx5",
                            "xxxx8xx79"])
        self.ingresar_dimension()
        # crear sudoku...
        while not jugar.juego_terminado():
            # mostrar tablero
            jugar.tabla()
            jugar.ingresar_valor()
            #jugar.
            # poner en el sudoku...


if __name__ == "__main__":
    u = UserInput()
    u.play()
