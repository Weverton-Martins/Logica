#Crie um programa que pede uma frase ao usuário e conta quantas vogais existem nela.

frase = input("Digite uma frase: ").lower()
vogais = 'aeiou'
contador = 0

for letra in frase:
    if letra in vogais:
        contador +=1

print(f"A frase digitada tem {contador} vogais.")

decoracao = "--" * 7
print(decoracao)


# Escreva um programa que inverte a ordem das palavras em uma frase.
frases = input("Difite uma frase:  ")
palavras = frases.split()
frase_invertida = " " .join(reversed(palavras))
print(f"Frase invertida: {frase_invertida}")