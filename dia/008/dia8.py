#1. Calculadora com Funções
'''Crie uma calculadora simples usando funções para somar, subtrair, multiplicar e dividir dois
números.'''

'''def soma (a,b):
    return a + b

def sub (a,b):
    return a - b

def mult (a,b):
    return a * b

def div (a,b):
    if b != 0:
        return a / b
    else:
        return 'ERRO, Divisão por zero!'
    
while True:
    
    num1 = float(input('Escolha o primeiro numero: '))
    num2 = float(input('Escolha o segundo numero: '))
    opcao = input('Escolha o que deseja realizar: (+, -, *, /): ')

    if opcao == '+':
        result = soma(num1, num2)
        print(f'A soma de {num1} + {num2}: {result}')

    elif opcao == '-':
        result = sub(num1,num2)
        print(f'A subtração de {num1} - {num2}: {result}')
        
    elif opcao == '*':
        result = mult(num1,num2)
        print(f'A multiplicação de {num1} * {num2}: {result}')

    elif opcao == '/':
        result = div(num1,num2)
        print(f'A divisão de {num1} / {num2}: {result}')

    else:
        result = 'Operação invalida!'
    
    continuar = input('Deseja realizar uma nova operação: (s/n): ').lower()
    if continuar != 's':
        print('Encerrando!')
        break
'''
#2. Função para Verificar Número Primo
'''Crie uma função que verifica se um número é primo.'''
'''
def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

numero = int(input('Informe um número: '))

if eh_primo(numero):
    print(f'O {numero} é primo.')
else:
    print(f'O {numero} não é primo.')
'''
#3. Conversor de Temperaturas
'''Crie funções para converter temperaturas entre Celsius, Fahrenheit e Kelvin.'''
'''
def celcius_kelvin(c):
    kelvin = c + 273.15
    return kelvin

def kelvin_celcius(k):
    celcius = k - 273.15
    return celcius

def celcius_fahrenheit(c):
    fahrenheit = (c * 1.8) + 32
    return fahrenheit

def fahrenheit_celcius(f):
    celcius = (f - 32)/1.8
    return celcius

def fahrenheit_kelvins(f):
    kelvins = ((f-32)/1.8) + 273.15
    return kelvins

def kelvin_fahrenheit(k):
    fahrenheit = (k-273.15)*1.8 + 32
    return fahrenheit

valor = float(input('Informe uma temperatura: '))
opcao = input('Qual seu tipo de temepratura informada (Celsius, Fahrenheit ou Kelvin): ').lower()

if opcao == 'celsius':
    result = celcius_kelvin(valor)
    print(f'A temperatura {valor} em Celsius para Kelvin: {result}')
    result = celcius_fahrenheit(valor)
    print(f'A temperatura {valor} em Celsius para Fahrenheit: {result}')

elif opcao == 'fahrenheit':
    result = fahrenheit_celcius(valor)
    print(f'A temperatura {valor} em Fahrenheit para Celcius: {result}')
    result = fahrenheit_kelvins(valor)
    print(f'A temperatura {valor} em Fahrenheit para Kelvin: {result}')

elif opcao == 'kelvin':
    result = kelvin_fahrenheit(valor)
    print(f'A temperatura {valor} em Kelvin para Fahrenheit: {result}')
    result = kelvin_celcius(valor)
    print(f'A temperatura {valor} em Kelvin para Celcius: {result}')

else:
    print('Tipo invalido de temperatura..')'''

#4. Função Recursiva para Fatorial
'''Crie uma função recursiva para calcular o fatorial de um número.'''

def fatorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * fatorial(n-1)

num = int(input('Informe o numero que deseja saber o fatorial: '))
if num >=0:
    result = fatorial(num)
    print(f'O fatorial de {num} é {result}')
else:
    print('Numero invalido!')

#Desafios
#1. Gerador de Senhas Aleatórias
'''Crie uma função que gera uma senha aleatória com tamanho especificado, contendo letras
maiúsculas, minúsculas, números e símbolos.'''


