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
carro2.frear(30)      # Saída: O carro está agora a 70 km/h.


#Crie uma classe Retangulo que representa um retângulo, com os atributos largura e altura. Inclua os métodos: area e perimetro

class retangulo:

    def __init__(self, altura, base):
        self.altura = altura #atributos
        self.base = base #atributos
        
    def area(self): #metodo
        return self.base * self.altura

    def perimetro(self): #metodo
        return 2*(self.base+self.altura)

medidas = retangulo(10, 5)
print(f'\nA area do retangulo é {medidas.area()}')
print(f'O perimetro do retangulo é {medidas.perimetro()}')

#Crie uma classe Aluno com os atributos nome e notas (uma lista de notas). Inclua os métodos:adicionar_nota(nota) e calcular_media()

class Aluno:

    def __init__(self, nome): #MÉTODO CONSTRUTOR
        self.nome = nome
        self.notas = []

    def adiciona_nota(self, nota): #MÉTODO
        self.notas.append(nota)

    def calcular_media(self): #MÉTODO
        if self.notas:
            return sum(self.notas)/len(self.notas)
        else:
            return 0
#INSTANCIAÇÃO criando um OBJETO real a partir do molde 'Aluno'
aluno1 = Aluno('Weverton')
#CHAMANDO MÉTODOS
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

valores = Calculadora(10,5)
print(f'\nOs calculos de {valores.a} e {valores.b} são: ')
print(f'Resultado soma: {valores.somar()}')
print(f'Resultado subtrair: {valores.subtrair()}')
print(f'Resultado multiplicar: {valores.multiplicar()}')
print(f'Resultado dividir: {valores.dividir()}')

#Ficha de Treino Upper/Lower (Foco em Classes, Atributos e Métodos)

class Exercicio:

    def __init__(self, nome, num_series, num_repeticao, carga):
        self.nome = nome
        self.num_series = num_series
        self.num_repeticao = num_repeticao
        self.carga = carga
    
    def resumo(self):
        print(f'\nAnotações: {self.nome}: {self.num_series} series de {self.num_repeticao} reps com {self.carga}Kg')

    def aumentar_cargas(self, valor):
        self.carga += valor
        return self.carga


dia1 = Exercicio('Supino', 4, 10, 50)
dia1.resumo()
dia2 = Exercicio('Agachamento', 2, 8, 90)
dia2.resumo()
dia3 = Exercicio('Terra', 2, 6, 160)
dia3.resumo()
print(f'Carga aumentada no {dia1.nome} pra {dia1.aumentar_cargas(50)}kg')
dia1.resumo()

#Monitoramento Blue Team (Foco em Composição e Lógica)

class AlertaSeguranca:

    def __init__(self, ip_origem, tipo_ataque, severidade):
        self.ip_origem = ip_origem
        self.tipo_ataque = tipo_ataque
        self.severidade = severidade


class DashboardSOC:

    def __init__(self):
        self.alerta = []
    
    def registrar_alerta(self, novo_alerta):
        self.alerta.append(novo_alerta)

    def filtrar_criticos(self):
        for i in self.alerta:
            if i.severidade > 7:
                print(f'\nCritíco: Nivel {i.severidade} | Ataque: {i.tipo_ataque} | Ip de origem{i.ip_origem}')

# Criando 3 alertas simulados
alerta1 = AlertaSeguranca("192.168.0.15", "Brute Force SSH", 9)
alerta2 = AlertaSeguranca("10.0.0.5", "Port Scan", 4)
alerta3 = AlertaSeguranca("172.16.2.100", "Ransomware Detectado", 10)

# Iniciando o Dashboard
meu_painel = DashboardSOC()

# Injetando os alertas para dentro do Dashboard
meu_painel.registrar_alerta(alerta1)
meu_painel.registrar_alerta(alerta2)
meu_painel.registrar_alerta(alerta3)

# Rodando a função de filtro
meu_painel.filtrar_criticos()