#1. Contador de Palavras em um Arquivo
#Crie um programa que leia um arquivo de texto e conte quantas vezes cada palavra aparece no texto
import os
print("Arquivos nesta pasta:", os.listdir())
nome_arquivo = input('Digite o nome do arquivo: ')

try:
    with open (nome_arquivo, 'r') as arquivo:
        texto = arquivo.read()
        print(texto)
except FileNotFoundError:
    print('Arquivo não encontrado!')
else:
    palavras = texto.lower().replace(',', '').replace('-', '').split()
    contagem = {}

    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] +=1
        else:
            contagem[palavra] = 1
    
    for chave,valor in contagem.items():
        print(f'Cada palavra: {chave} apareceu: {valor} vez(es)')
