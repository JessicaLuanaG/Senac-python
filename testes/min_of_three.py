def min_of_three(a, b, c):
    vet = [a, b, c]
    vet.sort()
    return vet[0]

import unittest

class TestMinOfThree(unittest.TestCase):
    def test_min_of_trhee_numeros_positivos(self):
        self.assertEqual(min_of_three(2,3,1), 1)
        
    def test_min_of_trhee_numeros_positivos_e_negativos(self):
        self.assertEqual(min_of_three(2,-3,1), -3)
        
    def test_min_of_trhee_numeros_negativos(self):
        self.assertEqual(min_of_three(-5,-3,-1), -5)
        
    def test_min_of_trhee_numeros_iguais(self):
        self.assertEqual(min_of_three(2,1,1), 1)
        
    def test_min_of_trhee_numeros_zero(self):
        self.assertEqual(min_of_three(2,1,0), 0)
        
    def test_min_of_trhee_numeros_diferentes_tipos(self):
        self.assertEqual(min_of_three(-2,3,0), -2)
        
        
if __name__ == '__main__':
    unittest.main()    