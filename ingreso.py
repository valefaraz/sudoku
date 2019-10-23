from sudoku import Sudoku
from api import api
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
        self.tamaño = 0
        while self.dimension(self.tamaño) is False:
            try:
                self.tamaño = int(input("Ingrese el tamaño del sudoku (4 o 9): "))
                if (self.dimension(self.tamaño)):
                    return int(self.tamaño)
                print("Ingresaste un tamaño no permitido, intentalo de nuevo")
            except ValueError:
                print("Ingresaste un tamaño no permitido, intentalo de nuevo")
    
    def ingresar_valor(self, jugar, tamaño):
        number = 0
        fila = 0
        columna = 0
        while self.ingreso_numero(number, tamaño) is False or self.ingreso_coordenadas(fila,
                                                                                    columna,
                                                                                    tamaño) is False:
            try:
                fila = int(input("\n\nFila: "))
                columna = int(input("Columna: "))
                number = int(input("Valor: "))
            except ValueError:
                pass

            if (self.ingreso_numero(number,tamaño) and self.ingreso_coordenadas(fila,
                                                                                columna,
                                                                                tamaño)) is True:
                if jugar.control_general(fila - 1, columna - 1,number) is False:
                    print('No se puede escribir sobre un valor fijo')

                elif jugar.control_repetir_fila_columna(fila - 1, columna - 1,str(number)) is False:
                    print('No se puede escribir, el valor ya se encuentra en la fila y/o columna')

                elif jugar.control_repetir_zona(fila - 1,columna - 1,str(number)) is False:
                    print('No se puede escribir, el valor se encuentra en la zona')
                    
                return fila - 1, columna - 1, number
                
            print("Ingresaste un valor no permitido, intentalo de nuevo")

    
    def play(self):
        print ("......SUDOKU......\n")
        print("Intente llenar el tablero sin repetir valores en filas, columnas y bloques \n")
        jugar = Sudoku(api(self.ingresar_dimension()),self.tamaño)
        #self.ingresar_dimension()
        while not jugar.juego_terminado():
            # mostrar tablero
            print(jugar.tabla())
            # jugar.write(*self.ingresar_valor(self.tamaño))
            x, y, n = self.ingresar_valor(jugar,self.tamaño)
            jugar.write(x, y, n)
        
        print("Felicitaciones, ganó el juego")



if __name__ == "__main__":
    u = UserInput()
    u.play()
