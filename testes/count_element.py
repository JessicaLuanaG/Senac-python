def count_element(lista,elemento):
    if elemento in lista:
        return "Elemento em lista"
    else:
        return "perdeu"

import unittest

class testCountElement(unittest.TestCase):
    def test_count_element_unico(self):
        self.assertEqual(count_element([0,97,34,55,4,9766,38,48,29,569,29],10), "perdeu")
        
    def test_count_element_duas_entradas(self):
        self.assertEqual(count_element([0,97,34,55,4,9766,38,48,29,569,29],0), "Elemento em lista")
        
    def test_count_element_tres_entradas(self):
        self.assertEqual(count_element([0,97,34,55,4,9766,38,48,29,569,29],68), "perdeu")
        
    def test_count_element_quatro_entradas(self):
        self.assertEqual(count_element([0,97,34,55,4,9766,38,48,29,569,29],29), "Elemento em lista")
        

if __name__ == '__main__':
    unittest.main()