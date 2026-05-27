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
