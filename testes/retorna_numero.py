def retorna_numero(lista):
    if len(lista) == 0:
        return "0"
    return len(lista)

import unittest

class testRetornaNumero(unittest.TestCase):
    def test_retorna_numero_vazia(self):
        self.assertEqual(retorna_numero([]), "0")
        
    def test_retorna_numero_unico(self):
        self.assertEqual(retorna_numero([5]), 1)
        
    def test_retorna_numero_duas_entradas(self):
        self.assertEqual(retorna_numero([5, 10]), 2)
        
    def test_retorna_numero_tres_entradas(self):
        self.assertEqual(retorna_numero([5, 10, 7]), 3)
        
    def test_retorna_numero_quatro_entradas(self):
        self.assertEqual(retorna_numero([4, -4, 8,8]), 4)
        

if __name__ == '__main__':
    unittest.main()
