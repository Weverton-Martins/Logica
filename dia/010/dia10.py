#1. Contador de Vogais
# Crie um programa que pede uma frase ao usuário e conta quantas vogais existem nela
'''
frase = input('Informe uma frase: ').lower()
vogais = 'aeiou'
contador  = 0

for letras in frase:
    if letras in vogais:
        contador +=1

print(f'A frase {frase} tem {contador} vogais!')'''

#2. Invertendo Palavras
#Escreva um programa que inverte a ordem das palavras em uma frase.

'''frase = input('Informe uma frase: ').lower()

fatia = frase[:: -1]

print(f'A frase invertida é: {fatia}')'''

#3. Verificação de Palíndromo
#Um palíndromo é uma palavra que é igual de trás para frente. Crie um programa que verifica se uma palavra é um palíndromo.

'''palavra = input('Informe uma frase: ').lower()
palavras_semespaco = palavra.replace(' ', '')
fatia = palavras_semespaco[:: -1]

if palavras_semespaco == fatia:
    print(f'A palavras {palavra} é igual escrita de tras pra frente {fatia}. Logo é um palíndromo!')

else:
    print(f'A palavras {palavra} não é igual escrita de tras pra frente {fatia}. Logo não é um palíndromo!')'''

#Senha Forte
#Crie um programa que verifica se uma senha é forte. A senha deve ter pelo menos 8 caracteres, conter letras maiúsculas e minúsculas, números e símbolos

senha = input('Digite uma senha: ')

verifica_caracter = len(senha) >= 8 #Verifica o compirmento
temletrasM = any(c.isupper() for c in senha) #Verifica se tem letra MAIUSCULO
temletrasm = any(c.islower() for c in senha) #Verifica se tem letra minuscula
temNum = any(c.isdigit() for c in senha) #Verifica se tem numeros 0:9
temSimbolos = any(not c.isalnum() for c in senha) #o esalnum verifica se tem num ou letras, not faz o contrario busca simbolos.

if verifica_caracter and temletrasM and temletrasm and temNum and temSimbolos:
    print(f'Senha Forte')
else:
    print('Senha Fraca, verifique os requiisitos: 8 caracteres, conter letras maiúsculas e minúsculas, números e símbolos!')

# Melhorar código assima posteriormente