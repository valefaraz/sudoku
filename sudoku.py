import math

class Sudoku():

    def __init__(self,matriz,tamaño):
        self.tamaño=tamaño
        self.tablero = [ [ 0 for __ in range(self.tamaño) ] for _ in range(self.tamaño) ]
        self.tablero_fijo = [ [ 0 for __ in range(self.tamaño) ] for _ in range(self.tamaño) ]
        self.convertir_tablero(matriz)

    def convertir_tablero(self,matriz):
        for i in range(self.tamaño):
            for j in range(self.tamaño):
                self.tablero[i][j] = matriz[i][j]
                self.tablero_fijo[i][j] = matriz[i][j]
    
    def control_de_fijos(self,i,j):
        return self.tablero_fijo[i][j] == 'x'
    
    def control_repetir_fila_columna(self,fila,columna,valor):
    #dejamos fija "i" y recorremos "j"(controla que no se repitan los valores en la fila)
        for n in range(self.tamaño):
            if self.tablero[n][columna] == valor: #chequea columna
                return False
            if self.tablero[fila][n] == valor: #chequea fila
                return False
        return True
        #int(math.sqrt(self.tamaño)*2)
        
    def control_repetir_zona(self,fila,columna,valor):
        if (fila < int(math.sqrt(self.tamaño))):
            fila = 0
        elif (fila >= int(math.sqrt(self.tamaño)) and fila < int(math.sqrt(self.tamaño)*2)):
            fila = int(math.sqrt(self.tamaño))
        else:
            fila = int(math.sqrt(self.tamaño)*2)
        if (columna < int(math.sqrt(self.tamaño))):
            columna = 0
        elif (columna >= int(math.sqrt(self.tamaño)) and columna < int(math.sqrt(self.tamaño)*2)):
            columna = int(math.sqrt(self.tamaño))
        else:
            columna = int(math.sqrt(self.tamaño)*2)
        for i in range(int(math.sqrt(self.tamaño))):
            for j in range(int(math.sqrt(self.tamaño))):
                if (self.tablero[fila + i][columna + j] == valor):
                    return False
        return True

    def control_general(self,fila,columna,valor):
        c = 0
        if self.control_repetir_fila_columna(fila, columna, valor) is False:
            c += 0
            #print("Problema en fila y/o columna")
        else:
            c += 1
        if self.control_repetir_zona(fila, columna, valor) is False:
            c += 0
            #print("Problema en el Bloque")
        else:
            c += 1
        if self.control_de_fijos(fila, columna)is False:
            c += 0
            #print("No se puede sobreescribir ese valor")
        else:
            c += 1
        if c == 3:
            return True
        else:
            return False
    
    def write(self, fila, columna, valor):
        if self.control_general(fila, columna, str(valor)) is True:
            self.tablero[fila][columna] = str(valor)
            #print(self.tablero)
        return (self.tablero[fila][columna])
    
    def juego_terminado(self):
        for i in range(self.tamaño):
            if ("x" in self.tablero[i]):
                return False
        #print("Fin del juego")
        return True
        

    def tabla(self):
        a = ''
        for fila in self.tablero:
            a += ' | '.join(fila)
            a += '\n'
        return a 




