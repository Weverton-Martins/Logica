class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca      # Atributo de instância
        self.modelo = modelo    # Atributo de instância
        self.ano = ano          # Atributo de instância
        self.velocidade = 0     # Atributo de instância
    
    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f'O carro {self.modelo} está agora a {self.velocidade} km/h')
    
    def frear(self, decremento):
        self.velocidade -= decremento
        if self.velocidade < 0:
            self.velocidade = 0
        print(f'O carro {self.modelo} esta agora a {self.velocidade} km/h')

#Criando e usando objetos 
carro1 = Carro('Honda', 'Civic', 2010)
carro2 = Carro('Fiat', 'Punto T-jet', 2010)

#usar o metodo
carro1.acelerar(50)     # Saída: O carro está agora a 50 km/h.
carro2.acelerar(100)
carro2.frear(30)        # Saída: O carro está agora a 70 km/h.


#Crie uma classe Retangulo que representa um retângulo, com os atributos largura e altura. Inclua os métodos: area e perimetro

class retangulo:

    def __init__(self, altura, base):
        self.altura = altura
        self.base = base
        
    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2*(self.base+self.altura)

medidas = retangulo(10, 5)
print(f'\nA area do retangulo é {medidas.area()}')
print(f'O perimetro do retangulo é {medidas.perimetro()}')

#Crie uma classe Aluno com os atributos nome e notas (uma lista de notas). Inclua os métodos:adicionar_nota(nota) e calcular_media()

class Aluno:

    def __init__(self, nome):
        self.nome = nome
        self.notas = []

    def adiciona_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        if self.notas:
            return sum(self.notas)/len(self.notas)
        else:
            return 0

aluno1 = Aluno('Weverton')
aluno1.adiciona_nota(10)
aluno1.adiciona_nota(9)
aluno1.adiciona_nota(5)

media = aluno1.calcular_media()
print(f'\nA media das notas de {aluno1.nome} são {media:.2f}')

#Crie uma classe Livro com os atributos titulo, autor e ano. Inclua um método exibir_informacoes() que imprime os detalhes do livro.

class Livro:

    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def exibir_informacoes(self):
        print(f'\nLivro: {self.titulo}')
        print(f'Autor: {self.autor}')
        print(f'Ano: {self.ano}')

livro = Livro('Harry Portter', 'J. K. Rowling', 1997)
livro.exibir_informacoes()

#Crie uma classe Calculadora que tenha métodos para as operações básicas 

class Calculadora:

    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def somar(self):
        return self.a + self.b

    def subtrair(self):
        return self.a - self.b
    def multiplicar(self):
        return self.a * self.b
    def dividir(self):
        if self.b != 0:
            return self.a / self.b
        else:
            print('Erro: Divbisão por zero')
            return None

valores = Calculadora(10,0)
print(f'\nOs calculos de {valores.a} e {valores.b} são: ')
print(f'Resultado soma: {valores.somar()}')
print(f'Resultado subtrair: {valores.subtrair()}')
print(f'Resultado multiplicar: {valores.multiplicar()}')
print(f'Resultado dividir: {valores.dividir()}')
