def invertendo_string(lista):
        return lista[::-1]
    
import unittest

class testInvertendoString(unittest.TestCase):

    def test_invertendo_string_unico(self):
        self.assertEqual(invertendo_string("apple"), "elppa")
        
    def test_invertendo_string_duas_entradas(self):
        self.assertEqual(invertendo_string("aba"), "aba")
        
    def test_invertendo_string_tres_entradas(self):
        self.assertEqual(invertendo_string("maria"), "airam")
        
    def test_invertendo_string_quatro_entradas(self):
        self.assertEqual(invertendo_string("pedro"), "ordep")
        

if __name__ == '__main__':
    unittest.main()