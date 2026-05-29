#Testando recursão com algoritimos básicos
#resursão é quando uma função chama a se mesmo pra resolver o problema

'''Crie uma função recursiva que calcula o fatorial de um número fornecido pelo
usuário.'''

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

n = int(input('Informe um número inteiro que deseja saber o fatorial: '))
if n < 0:
    print('Erro: Valor negativo')
else:
    resultado = fatorial(n)
    print(f'O fatorial de {n} é {resultado}')

'''Crie uma função recursiva que retorna o n-ésimo número da sequência de
Fibonacci'''

def fibonacci(numero):
    if numero < 2:
        return numero
    else:
        return fibonacci(numero - 1) + fibonacci(numero - 2)

numero = int(input('Informe o número a ser calculado a sequencia de Fibonnaci: '))
if numero < 0:
    print('Erro: Valor negativo')
else:
    resultado = fibonacci(numero)
    print(f'A sequência de Fibonnaci do {numero} é {resultado}')
    

'''Crie uma função recursiva que realiza uma contagem regressiva a partir de um
número fornecido pelo usuário até zero.'''

def contagem_regressiva(num):
    if num <= 0:
        print('Fim!')
    else:
        print(num)
        return contagem_regressiva(num - 1)

num = int(input('Informe um numero: '))
contagem_regressiva(num)
