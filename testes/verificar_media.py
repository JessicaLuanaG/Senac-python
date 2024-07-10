def verificar_media(lista):
    if len(lista) == 0:
        return "Lista Vazia"
    media = sum(lista) / len(lista)
    return media

import unittest

class testVerificarMedia(unittest.TestCase):
    def test_verificar_media_vazia(self):
        self.assertEqual(verificar_media([]), "Lista Vazia")
        
    def test_vericar_media_unico(self):
        self.assertEqual(verificar_media([5]), 5)
        
    def test_verficar_media_duas_entradas(self):
        self.assertEqual(verificar_media([5, 10]), 7.5)
        
    def test_verficar_media_tres_entradas(self):
        self.assertEqual(verificar_media([5, 10, 7.5]), 7.5)
        
    def test_verficar_media_quatro_entradas(self):
        self.assertEqual(verificar_media([4, 4, 8,8]), 6)
        

if __name__ == '__main__':
    unittest.main()