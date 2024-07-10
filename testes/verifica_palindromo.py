def verifica_palindromo(lista):
        x = lista[::-1]
        if lista == x:
            return "É palindromo"
        else:
            return "Não é palindromo"


import unittest

class testVerificaPalindromo(unittest.TestCase):

    def test_verifica_palindromo_unico(self):
        self.assertEqual(verifica_palindromo("apple"), "Não é palindromo")
        
    def test_verifica_palindromo_duas_entradas(self):
        self.assertEqual(verifica_palindromo("aba"), "É palindromo")
        
    def test_verifica_palindromo_tres_entradas(self):
        self.assertEqual(verifica_palindromo("maria"), "Não é palindromo")
        
    def test_verifica_palindromo_quatro_entradas(self):
        self.assertEqual(verifica_palindromo("ovo"), "É palindromo")
        

if __name__ == '__main__':
    unittest.main()