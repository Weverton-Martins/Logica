# Imprimindo Números de 1 a 10

for i in range(1, 11):
    print("Numero: ", i)

# Calculando a Soma dos Números de 1 a N

numero = int(input("Digite um numero inteiro: "))

soma = 0

for i in range(1, numero+1):
    soma += i

print("A soma dos numero de 1 a ", numero, "é", soma)

# Tabuada de um Número

num = int(input("Digite um numero pra ver a tabuada: "))

for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")


# Contando Números Pares e Ímpares

impares = 0
pares = 0

for i in range(1, 21):
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1
print("Impares: ", impares)
print("Pares: ", pares)

# Adivinhe o Número

import random

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    palpite = int(input("Adivinhe o numero (entre 1 e 100): "))
    tentativas += 1

    if palpite == numero_secreto:
        print(f"Parabens! Voce acerto na {tentativas}")
        break
    elif palpite < numero_secreto:
        print("O numero é maior!")
    else:
        print(("O numero é menor!"))

#  Calculando Fatorial de um Número
# Peça ao usuário um número inteiro positivo e calcule o fatorial desse número.
# ● Fatorial de N (N!) é o produto de todos os números inteiros positivos de 1 até N.
# ● Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

N = int(input("Informe um numero para ver seu fatorial: "))

fatorial = 1

if N < 0:
    print("Não existe fatorial de numero negativo")

elif N == 0 and N == 1:
    print(f"Fatorial de {N} é 1")

else:
    for i in range(1, N+1):
        fatorial *=i
        print(f"Fatorial do numero {N} é: {fatorial}")




