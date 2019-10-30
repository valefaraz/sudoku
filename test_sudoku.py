import unittest
from parameterized import parameterized
from sudoku import Sudoku


class TestSudoku(unittest.TestCase):
    
    def setUp(self):
        self.game=Sudoku([  "53xx7xxxx",
                            "6xx195xxx",
                            "x98xxxx6x",
                            "8xxx6xxx3",
                            "4xx8x3xx1",
                            "7xxx2xxx6",
                            "x6xxxx28x",
                            "xxx419xx5",
                            "xxxx8xx79"],9)

        self.game4=Sudoku([ "x2xx",
                            "x3x2",
                            "x124",
                            "2xx1"],4)

    @parameterized.expand([
        (0,1),
        (1,1),
        (3,3),
        (1,3),
        (2,1),
        (2,2),
        (2,3),
        (3,0)
    ])
    def test_control_fijos_false4(self,fila,columna):
        self.assertEqual(self.game4.control_de_fijos(fila,columna), False)
    
    @parameterized.expand([
        (0,0),
        (0,3),
        (3,1),
        (0,2),
        (1,0),
        (1,2),
        (3,2),
        (2,0)
    ])
    def test_control_fijos_true4(self,fila,columna):
        self.assertEqual(self.game4.control_de_fijos(fila,columna), True)

    @parameterized.expand([
        (0,0),
        (0,1),
        (8,8),
        (0,4),
        (1,0),
        (1,3),
        (1,4),
        (1,5),
        (7,8),
        (2,1),
        (2,2),
        (2,7),
        (3,0),
        (3,4),
        (3,8),
        (4,0),
        (4,3),
        (4,5)
    ])
    def test_control_fijos_false9(self,fila,columna):
        self.assertEqual(self.game.control_de_fijos(fila,columna), False)

    @parameterized.expand([
        (1,1),
        (0,2),
        (8,6),
        (8,5),
        (7,0),
        (0,3),
        (8,0),
        (8,1),
        (0,3),
        (0,6),
        (0,7),
        (0,8),
        (3,1),
        (3,2),
        (3,3),
        (3,5),
        (3,6),
        (4,1),
        (4,2),
        (4,4),
        (4,6)
    ])
    def test_control_fijos_true9(self,fila,columna):
        self.assertEqual(self.game.control_de_fijos(fila,columna), True)

    @parameterized.expand([
        (0,2,"8"),
        (2,0,"9"),
        (6,8,"6")
    ])
    def test_control_repetir_false9(self,fila,columna,valor):
        self.assertEqual(self.game.control_repetir_fila_columna(fila,columna,valor), False)

    @parameterized.expand([
        (0,0,"1"),
        (0,2,"2"),
        (7,0,"2")
    ])
    def test_control_repetir_true9(self,fila,columna,valor):
        self.assertEqual(self.game.control_repetir_fila_columna(fila,columna,valor), True)
    
    @parameterized.expand([
        (0,0,"2"),
        (3,2,"2"),
        (0,3,"4")
    ])
    def test_control_repetir_false4(self,fila,columna,valor):
        self.assertEqual(self.game4.control_repetir_fila_columna(fila,columna,valor), False)

    @parameterized.expand([
        (0,0,"1"),
        (3,2,"3"),
        (0,3,"3")
    ])
    def test_control_repetir_true4(self,fila,columna,valor):
        self.assertEqual(self.game4.control_repetir_fila_columna(fila,columna,valor), True)

    @parameterized.expand([
        (0,2,"6"),
        (1,1,"5")
    ])
    def test_control_repetir_zona_false9(self,fila,columna,valor):
        self.assertEqual(self.game.control_repetir_zona(fila,columna,valor), False)
    
    @parameterized.expand([
        (0,2,"2"),
        (8,6,"4")
    ])
    def test_control_repetir_zona_true9(self,fila,columna,valor):
        self.assertEqual(self.game.control_repetir_zona(fila,columna,valor), True)

    @parameterized.expand([
        (0,2,"2"),
        (3,2,"4")
    ])
    def test_control_repetir_zona_false4(self,fila,columna,valor):
        self.assertEqual(self.game4.control_repetir_zona(fila,columna,valor), False)
    
    @parameterized.expand([
        (0,2,"1"),
        (3,1,"3")
    ])
    def test_control_repetir_zona_true4(self,fila,columna,valor):
        self.assertEqual(self.game4.control_repetir_zona(fila,columna,valor), True)
    
    def test_control_general_1(self):
        self.assertEqual(self.game.control_general(0,2,"1"), True)
    
    def test_control_general_2(self):
        self.assertEqual(self.game.control_general(0,0,"5"), False)
    
    def test_write9_1(self):
        self.assertEqual(self.game.write(0,2,"1"), "1")
    
    def test_write9_2(self):
        self.assertEqual(self.game.write(0,7,"2"), "2")
    
    def test_write9_3(self):
        self.assertEqual(self.game.write(0,2,"5"), "x")
    
    def test_write4_1(self):
        self.assertEqual(self.game4.write(0,2,"1"), "1")
    
    def test_write4_2(self):
        self.assertEqual(self.game4.write(3,1,"2"), "x")
    
    def test_write4_3(self):
        self.assertEqual(self.game4.write(3,2,"3"), "3")

    def test_overwrite(self):
        self.assertEqual(self.game.write(0,2,"2"), "2")

    def test_write_fijo(self):
        self.assertEqual(self.game.write(0,0,"1"), "5")
    
    def test_game_over_1(self):
        
        self.game = Sudoku(["533175384", "612195537", "298376369", "882668363",
                 "481863981", "717328356", "169836281", "916419925",
                 "816288179"],9)
        self.assertEqual(self.game.juego_terminado(), True)

    def test_game_over_2(self):
        
        self.game = Sudoku(["533175384", "612195537", "298376369", "882668363",
                 "481863981", "71732x356", "169836281", "916419925",
                 "816288179"],9)
        self.assertEqual(self.game.juego_terminado(), False)

    def test_game_over_3(self):
        
        self.game4 = Sudoku(["5331",
                            "6121", 
                            "2983", 
                            "8826"],4)

        self.assertEqual(self.game4.juego_terminado(), True)
    
    def test_game_over_4(self):
        
        self.game4 = Sudoku(["5331",
                            "6121", 
                            "2983", 
                            "882x"],4)

        self.assertEqual(self.game4.juego_terminado(), False)



if __name__ == '__main__':
    unittest.main()