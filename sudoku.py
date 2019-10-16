class Sudoku():

    def __init__(self,matriz):
        self.tablero = [ [ 0 for __ in range(9) ] for _ in range(9) ]
        self.tablero_fijo = [ [ 0 for __ in range(9) ] for _ in range(9) ]
        self.convertir_tablero(matriz)

    def convertir_tablero(self,matriz):
        for i in range(9):
            for j in range(9):
                self.tablero[i][j] = matriz[i][j]
                self.tablero_fijo[i][j] = matriz[i][j]
    
    def control_de_fijos(self,i,j):
        return self.tablero_fijo[i][j] == "x"
    
    def control_repetir_fila_columna(self,fila,columna,valor):
    #dejamos fija "i" y recorremos "j"(controla que no se repitan los valores en la fila)
        for n in range(9):
            if self.tablero[n][columna] == valor: #chequea columna
                return False
            if self.tablero[fila][n] == valor: #chequea fila
                return False
        return True
    def control_repetir_zona(self,fila,columna,valor):
        if (fila < 3):
            fila = 0
        elif (fila >= 3 and fila < 6):
            fila = 3
        else:
            fila = 6
        if (columna < 3):
            columna = 0
        elif (columna >= 3 and columna < 6):
            columna = 3
        else:
            columna = 6
        for i in range(3):
            for j in range(3):
                if (self.tablero[fila + i][columna + j] == valor):
                    return False
        return True
    def control_general(self,fila,columna,valor):
        c = 0
        if self.control_repetir_fila_columna(fila, columna, valor) is False:
            print("Problema en fila y/o columna")
        else:
            c += 1
        if self.control_repetir_zona(fila, columna, valor) is False:
            print("Problema en el Bloque")
        else:
            c += 1
        if self.control_de_fijos(fila, columna)is False:
            print("No se puede sobreescribir ese valor")
        else:
            c += 1
        if c == 3:
            return True
        else:
            return False
    
    def write(self, fila, columna, valor):
        if self.control_general(fila, columna, valor) is True:
            self.tablero[fila][columna] = valor
            #print(self.tablero)
        return (self.tablero[fila][columna])
    
    def juego_terminado(self):
        for i in range(9):
            if ("x" in self.tablero[i]):
                return False
        print("Fin del juego")
        return True
        

    def tabla(self):
        for i in self.tablero:
            for j in i:
                print(j,end=' ')
            print (' ') 




