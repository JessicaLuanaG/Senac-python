def verificar_impar(lista):
    if (lista%2) == 1:
        return "É ímpar"
    else:
        return "Não é impar" 

import unittest

class testVerificarImpar(unittest.TestCase):
        
    def test_vericar_impar_um(self):
        self.assertEqual(verificar_impar(1), "É ímpar")
        
    def test_verficar_impar_duas(self):
        self.assertEqual(verificar_impar(2), "Não é impar")
        
    def test_verficar_impar_tres(self):
        self.assertEqual(verificar_impar(3), "É ímpar")
        
    def test_verficar_impar_quatro(self):
        self.assertEqual(verificar_impar(4), "Não é impar")
        

if __name__ == '__main__':
    unittest.main()
        