# Declarando Variaveis
idade = 25 
altura = 1.90
nome = "Weverton"
estudante = True 

# Exibindo informações
print("idade:", idade)
print("nome:", nome)
print("altura:", altura)
print("estudante:", estudante)

# Operação Simples
ano_nascimento = 2025 - idade
print("Ano de Nascimento:", ano_nascimento)

maior_de_idade = idade >= 18
print("Mairo de idade:", maior_de_idade)

# Manipulando String
frase = "Olá meu nome é " + nome + " e eu tenho " + str(idade) + " anos"
print(frase)

# Calculadora Simples

numero1 = float(input("Insira o primeiro numero: "))
numero2 = float(input("Insira o segundo numero: "))

soma = numero1 + numero2
subtração = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

print("Soma:", soma)
print("Subtração:", subtração)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)

# Conversor de Temperaturas

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = celsius * 9/5 + 32
print("A temperatura em Fahrenheit é: ", fahrenheit)

# Calculando area de um circulo
raio = float(input("Digito o raio do circulo: "))
pi = 3.14159
area = pi*raio ** 2
print("A área do circulo é:", area)