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

