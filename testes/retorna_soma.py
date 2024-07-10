def retorna_soma(lista):
    if len(lista) == 0:
        return "0"
    return sum(lista)

import unittest

class testRetornaSoma(unittest.TestCase):
    def test_retorna_soma_vazia(self):
        self.assertEqual(retorna_soma([]), "0")
        
    def test_retorna_soma_unico(self):
        self.assertEqual(retorna_soma([5]), 5)
        
    def test_retorna_soma_duas_entradas(self):
        self.assertEqual(retorna_soma([5, 10]), 15)
        
    def test_retorna_soma_tres_entradas(self):
        self.assertEqual(retorna_soma([5, 10, 7]), 22)
        
    def test_retorna_soma_quatro_entradas(self):
        self.assertEqual(retorna_soma([4, -4, 8,8]), 16)
        

if __name__ == '__main__':
    unittest.main()
