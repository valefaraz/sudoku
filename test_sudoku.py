import unittest

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
                            "xxxx8xx79"])

    def test_playing(self):
        self.assertTrue(self.game.playing)

    def test_control_fijos_1(self):
        self.assertEqual(self.game.control_de_fijos(0,0), False)

    def test_control_fijos_2(self):
        self.assertEqual(self.game.control_de_fijos(1,1), True)

    def test_control_fijos_3(self):
        self.assertEqual(self.game.control_de_fijos(0,1), False)

    def test_control_fijos_4(self):
        self.assertEqual(self.game.control_de_fijos(8,8), False)

    def test_control_repetir_1(self):
        self.assertEqual(self.game.control_repetir_fila_columna(0,2,"8"), False)
    
    def test_control_repetir_2(self):
        self.assertEqual(self.game.control_repetir_fila_columna(0,0,"1"), True)
    
    def test_control_repetir_zona_1(self):
        self.assertEqual(self.game.control_repetir_zona(0,2,"6"), False)

    def test_control_repetir_zona_2(self):
        self.assertEqual(self.game.control_repetir_zona(0,2,"1"), True)
    
    def test_control_general_1(self):
        self.assertEqual(self.game.control_general(0,2,"1"), True)
    
    def test_control_general_2(self):
        self.assertEqual(self.game.control_general(0,0,"5"), False)
    
    def test_write_1(self):
        self.assertEqual(self.game.write(0,2,"1"), "1")
    
    def test_write_2(self):
        self.assertEqual(self.game.write(0,7,"2"), "2")
    
    def test_write_3(self):
        self.assertEqual(self.game.write(0,2,"5"), "x")

    def test_overwrite(self):
        self.assertEqual(self.game.write(0,2,"2"), "2")

    def test_write_fijo(self):
        self.assertEqual(self.game.write(0,0,"1"), "5")
    
   # def test_game_over(self):
    #    self.assertEqual(self.game.juego_termiando(tabla_completa), True)

    
    







if __name__ == '__main__':
    unittest.main()