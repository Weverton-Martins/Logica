#1. Calculadora com Funções
'''Crie uma calculadora simples usando funções para somar, subtrair, multiplicar e dividir dois
números.'''

def soma (a,b):
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
    #começa o loop de escolhas
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
    #condição se deseja continuar
    continuar = input('Deseja realizar uma nova operação: (s/n): ').lower()
    if continuar != 's':
        print('Encerrando!')
        break

#2. Função para Verificar Número Primo
'''Crie uma função que verifica se um número é primo.'''
#condição de primo tem que ser maior que 1 e não pode ser par com excessão do 2 
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

#3. Conversor de Temperaturas
'''Crie funções para converter temperaturas entre Celsius, Fahrenheit e Kelvin.'''
#funções de conversões
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
#mostra as conversões possiveis pra cada temperatura
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
    print('Tipo invalido de temperatura..')

#4. Função Recursiva para Fatorial
'''Crie uma função recursiva para calcular o fatorial de um número.'''
#fatorial de 0 e 1 é 1
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

import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    #solda os caracteres na variavel resultado, e repete varias vezes mas não usa esse valor pra nada
    resultado = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return resultado

tamanho_senha = int(input('Informe qual o tamanho da senha: '))
senha_gerada = gerar_senha(tamanho_senha)
print('Senha gerada: ', senha_gerada)

#Calculando a Distância Entre Dois Pontos
'''Crie uma função que calcula a distância euclidiana entre dois pontos em um plano
cartesiano.'''
#funções matemáticas
import math

def distancia(ponto1,ponto2):
    ponto1 = x1, y1
    ponto2 = x2, y2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2) #sqrt raiz quadrada

x1 = float(input('Digite x1: '))
x2 = float(input('Digite x2: '))
y1 = float(input('Digite y1: '))
y2 = float(input('Digite y2: '))

dist = distancia((x1, y1), (x2,y2))
print(f'A distancia entre o pontos é: {dist}')