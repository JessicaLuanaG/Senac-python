def menor_numero(lista):
    if len(lista) == 0:
        return "Lista Vazia"
    else:
        lista.sort()
        return lista[0]
    
import unittest

class testMenorNumero(unittest.TestCase):
    def test_menor_numero_vazia(self):
        self.assertEqual(menor_numero([]), "Lista Vazia")
        
    def test_menor_numero_unico(self):
        self.assertEqual(menor_numero([5]), 5)
        
    def test_menor_numero_duas_entradas(self):
        self.assertEqual(menor_numero([5, 10]), 5)
        
    def test_menor_numero_tres_entradas(self):
        self.assertEqual(menor_numero([5, 10, 7.5]), 5)
        
    def test_menor_numero_quatro_entradas(self):
        self.assertEqual(menor_numero([4, -4, 8,8]), -4)
        

if __name__ == '__main__':
    unittest.main()