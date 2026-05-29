#Padrão Singleton
'''Crie uma classe Database que utiliza o padrão Singleton para garantir que apenas uma
instância do banco de dados seja criada.'''

class Database:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(Database, cls).__new__(cls)
            cls._instancia.conexao = 'Conexão com o banco de dados estabelecida'
        return cls._instancia

    def conectar(self):
        print(self.conexao)
    
obj1 = Database()
obj2 = Database()

obj1.conectar()
obj2.conectar()
print(obj1 is obj2)

#Padrão Factory Method
'''Crie um padrão Factory Method para criar diferentes formas geométricas (Circulo,
Quadrado, Triangulo) com base em um parâmetro.'''

from abc import ABC, abstractmethod

class Forma(ABC): #Classe
    @abstractmethod
    def desenhar(self):
        pass

#fábrica de desehos
class Circulo(Forma): #sub_classe
    def desenhar(self):
        print('Forma do Circulo realizada!')

class Quadrado(Forma): #sub_classe
    def desenhar(self):
        print('Forma do Quadrado realizada!')

class Triangulo(Forma): #sub_classe
    def desenhar(self):
        print('Forma do Triangulo realizada!')

#criar a fábrica, você especifica o tipo de forma que deseja, e a fábrica cria a instância correspondente.
class fabricaforma:
    def criar_forma(self, tipo):
        if tipo == 'circulo':
            return Circulo()
        elif tipo == 'quadrado':
            return Quadrado()
        elif tipo == 'triangulo':
            return Triangulo()
        else:
            raise ValueError('Erro: Tipo de forma desconhecido!')

fabrica = fabricaforma()
tipo_forma1 = fabrica.criar_forma('circulo')
tipo_forma1.desenhar()

tipo_forma2 = fabrica.criar_forma('quadrado')
tipo_forma2.desenhar()

tipo_forma3 = fabrica.criar_forma('triangulo')
tipo_forma3.desenhar()





