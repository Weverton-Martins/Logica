# Verificando se um numero é Positivo, Negativo ou Zero

numero = float(input("Digite um numero: "))

if numero > 0:
    print("Numero Positivo")
elif numero < 0:
    print("Numero Negativo")
elif numero == 0:
    print("Numero digitado é 0")

# Calculadora Simples

numero1 = float(input("Digite um numero: "))
numero2 = float(input("Digite outro numero: "))

operacao = input("Digite uma operação (+, -, *, /): ")

if operacao == '+':
    soma = numero1 + numero2
    print("Resultado = ", soma)
    
elif operacao == '-':
    sub = numero1 - numero2
    print("Resultado = ", sub)

elif operacao == '*':
    mult = numero1 * numero2
    print("Resultado = ", mult)

elif operacao == '/':
    if numero2 != 0:
        resultado = numero1 / numero2
        print("Resultado = ", resultado)  
    else:
        print("Erro: Divisão por zero!")  
else:
    print("Operação invalida")

# Classificação de Idade

idade = int(input("Digite sua Idade: "))

if idade == 0 and idade <= 12:
    print("Voce é Criança")
elif idade == 13 or idade <= 17:
    print("Voce é Adolecente")
elif idade == 18 or idade <= 59:
    print("Voce é Adulto")
elif idade == 60:
    print("Voce é Idoso")
else:
    print("Idade invalida")

# Verificando Ano Bissexto
ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 !=0) or (ano % 400 == 0):
    print("O ano é Bissexto")

else:
    print("Ano nâo e Bissexto!")

# Simulador de Caixa Eletrônico
saque = int(input("Informe o Valor do Saque: R$"))

if saque <= 0:
    print("Valor inválido")
else:
    cedula_100 = saque // 100  #Quantas cedulas de 100 podem ser usadas
    saque %= 100 #O que sobra pra pagar com cedulas menores

    cedula_50 = saque // 50
    saque %= 50

    cedula_20 = saque // 20
    saque %= 20

    cedula_10 = saque // 10
    saque %= 10

    cedula_5 = saque // 5
    saque %= 5

    cedula_2 = saque // 2
    saque %= 2

    if saque != 0:
        print("Não é possivel sacar o valor especificado com as cedulas dispóniveis")

    else:
        print("Cédulas entregues: ")
        if cedula_100 > 0:
            print(f"{cedula_100} x R$100")
        if cedula_50 > 0:
            print(f"{cedula_50} x R$50")    
        if cedula_20 > 0:
            print(f"{cedula_20} x R$20")
        if cedula_10 > 0:
            print(f"{cedula_10} x R$10")
        if cedula_5 > 0:
            print(f"{cedula_5} x R$5")
        if cedula_2 > 0:
            print(f"{cedula_2} x R$2")