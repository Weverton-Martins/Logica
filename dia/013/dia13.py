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
    palavras = texto.lower().split()
    contagem = {}

    for palavra in palavras:
        palavra = palavra.strip('.,!";:-()')
        if palavra in contagem:
            contagem[palavra] +=1
        else:
            contagem[palavra] = 1
    
    for chave,valor in contagem.items():
        print(f'Cada palavra: {chave} apareceu: {valor} vez(es)')

#Crie um programa que permita ao usuário armazenar contatos em um arquivo CSV.Adicionar um novo contato (nome, telefone, email).Listar todos os contatos.

import csv

def adicionar_contato():
    nome = input('Nome: ')
    telfone = input('Telefone: ')
    email = input('E-mail: ')

    with open('contatos.csv', 'a', newline='') as arquivo_csv: # utilizado o 'a' pois adiciona informação na ultima linha
        escritor = csv.writer(arquivo_csv)
        escritor.writerow([nome, telfone, email]) #formata com virgulas e salva no arquivo
        print('Contato adicionado com sucesso!')

def listar_contato():
    try:
        with open('contatos.csv', 'r') as arquivo_csv: #'r' leitura
            leitor = csv.reader(arquivo_csv) #transforma em texto pra percorrer usando o for
            for linha in leitor:
                print(f'Nome: {linha[0]}, Telefone: {linha[1]}, E-mail: {linha[2]}')
    except FileNotFoundError:
        print('Nenhum contato encontrado')

while True:

    print('\n Menu:')
    print('Opção 1: Adicionar')
    print('Opção 2: Listar Contatos')
    print('Opção 3: Sair')

    #proteção pra evitar que o bloco quebra e feche na cara do usuario
    try:
        opcao = int(input('Escolha uma opção acima: '))
    except ValueError:
        print('Porfavor digite apenas numeros inteiros 1,2,3...')
        continue
    if opcao == 1:
        adicionar_contato()
    elif opcao == 2:
        listar_contato()
    elif opcao == 3:
        print('Saindo...')
        break
    else:
        print('OPção Invalida!')
