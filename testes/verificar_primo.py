import math

def verificar_primo(num1):
    if num1 < 2:
        return "Não é primo"
    mult = math.floor(num1/2)
    for i in range(2,mult + 1, 1):
        if(not(num1%i)):
            return "Não é primo"
        exit()
    return "É primo"


import unittest

class testVerificarPrimo(unittest.TestCase):
        
    def test_vericar_primo_um(self):
        self.assertEqual(verificar_primo(1), "Não é primo")
        
    def test_verficar_primo_duas(self):
        self.assertEqual(verificar_primo(2), "É primo")
        
    def test_verficar_primo_tres(self):
        self.assertEqual(verificar_primo(3), "É primo")
        
    def test_verficar_primo_quatro(self):
        self.assertEqual(verificar_primo(4), "Não é primo")
        

if __name__ == '__main__':
    unittest.main()
        