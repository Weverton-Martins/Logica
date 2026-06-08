#Teste e Debugging 

#Crie uma função que multiplica dois números, mas introduza um erro intencional. Use técnicas de depuração para identificar e corrigir o erro.
import pdb
def multiplicar(a,b):
    pdb.set_trace()
    return a * c # Erro: variável 'c' não definida

resultado= multiplicar(4,5)
print(resultado)

#Crie uma função que soma dois números e escreva testes unitários para verificar seu funcionamento.
import unittest
def somar(a,b):
    return a + b

class TestSomar(unittest.TestCase):
    def test_somar_positivos(self):
        self.assertEqual(somar(2, 3), 5)

    def test_somar_negativos(self):
        self.assertEqual(somar(-1, -1), -2)
    
    def test_somar_zero(self):
        self.assertEqual(somar(0, 5), 5)

if __name__ == '__main__':
    unittest.main()