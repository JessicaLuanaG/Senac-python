def aumentano_string(lista):
    if len(lista) == 0:
        return "Lista Vazia"
    else:
        return [x.upper() for x in lista]

import unittest

class testMenorNumero(unittest.TestCase):
    def test_aumentano_string_vazia(self):
        self.assertEqual(aumentano_string([]), "Lista Vazia")
        
    def test_aumentano_string_unico(self):
        self.assertEqual(aumentano_string(["apple"]), ["APPLE"])
        
    def test_aumentano_string_duas_entradas(self):
        self.assertEqual(aumentano_string(["a", " Maria"]), ["A", " MARIA"])
        
    def test_aumentano_string_tres_entradas(self):
        self.assertEqual(aumentano_string(["a", " maria", " é"]), ["A" ," MARIA", " É"])
        
    def test_aumentano_string_quatro_entradas(self):
        self.assertEqual(aumentano_string(["a", " maria", " é", " cansada"]), ["A" ," MARIA", " É", " CANSADA"])
        

if __name__ == '__main__':
    unittest.main()