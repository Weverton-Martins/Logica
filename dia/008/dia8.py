#Crie uma calculadora simples usando funções para somar, subtrair, multiplicar e dividir dois números.

def somar(a, b):
    return a + b

def sub(a,b):
    return a - b

def mult (a, b):
    return a * b

def dividir (a,b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero!"

num1 = float(input("Informe um numero: "))
num2 = float(input("Informe outro numero: "))
operacao= input("Escolha uma operação (+, -, *, /): ")     

if operacao == '+':
    resultado = somar(num1, num2)

elif operacao == '-':
    resultado = sub(num1, num2)

elif operacao == '*':
    resultado = mult(num1, num2)

elif operacao == '/':
    resultado = dividir(num1, num2)

else:
    resultado = "Opração Invalida!"

print("Resultado: ", resultado)

#Crie uma função que verifica se um número é primo.

def eh_primo(numero):
    if numero <=1:
        return False
    for i in range (2, numero):
        if numero % i == 0:
            return False
    return True
    
num = int(input("Digite um numero inteiro: "))

if eh_primo(num):
    print(f"{num} é numero primo.")
else:
    print(f"{num} não é numero primo.")

#Crie uma função recursiva para calcular o fatorial de um número
#criar uma função
#definir o calculo
#exiber o resultado 

def fatorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * fatorial(n-1)

num = int(input("DIgite um numero inteiro positivo: "))
if num >= 0:
    resultado = fatorial(num)
    print(f"O fatorial de {num} é {resultado}")
else:
    print("Número inválido")
