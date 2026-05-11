# 1.Agenda Telefônica
#Crie um programa que permita ao usuário: ● Adicionar um contato com nome e telefone. ● Buscar um contato pelo nome. ● Remover um contato.
#fazer funções pra cada e depois um menu

agenda = {}

def adicionar_contato():
    nome = input('Nome: ')
    telefone = input('Telefone: ')
    agenda[nome] = telefone
    print('Adicionado com sucesso!')

def buscar_contato():
    nome = input('Informe qual contato deseja buscar pelo nome: ').lower()
    if nome in agenda:
        print(f'Telefone de {nome}: {agenda[nome]}')
    else:
        print('Nome não encontrado!')

def remover_contato():
    nome = input('Informe o contato que deseja remover da agenda: ')
    if nome in agenda:
        del agenda[nome]
        print('Removido com sucesso!')
    else:
        print('Contato não encontrado!')

while True:

    print('\n O que deseja realizar na agenda.')
    print('1 - Adicionar Contato')
    print('2 - Buscar Contato')
    print('3 - Remover Contato')
    print('4 - Exibir Agenda')
    print('5 - Sair')

    opcoes = int(input('Informe o que deseja realizar: '))

    if opcoes == 1:
        adicionar_contato()
    elif opcoes == 2:
        buscar_contato()
    elif opcoes == 3:
        remover_contato()
    elif opcoes == 4:
        print(agenda)
    elif opcoes == 5:
        print('Encerrando...')
        break
    else:
        print('Opção Invalida!')
        
#2. Verificação de Palavras Únicas
#Peça ao usuário para digitar uma frase e mostre todas as palavras únicas dessa frase.

frase = input('Digite uma frase: ')
lista = frase.split()
palavras_unicas = set(lista)
print(f'As palavras unicas são: {palavras_unicas}')

#3. União e Interseção de Conjuntos
#Crie dois conjuntos com números fornecidos pelo usuário e mostre: ● A união dos conjuntos. ● A interseção dos conjuntos.

numero_a = input('Informe alguns números separados com espaço: ').split()
numero_b = input('Informe alguns números separados com espaço: ').split()

set_a = set(numero_a)
set_b = set(numero_b)

uniao = set_a.union(set_b)
print(f'A união das duas listas são: {uniao}')

inter = set_a.intersection(set_b)
print(f'A interseção das duas listas são: {inter}')

dif = set_a.difference(set_b)
print(f'A diferença das duas listas são: {dif}')

#4. Contador de Caracteres
#Peça ao usuário para digitar um texto e conte quantas vezes cada caractere aparece.

texto = input('Informe um texto: ')

contador = {}

for caracter in texto.lower():
    if caracter in contador:
        contador[caracter] += 1
    else:
        contador[caracter] = 1


print('_'*5+'Contagem de caracteres'+'_'*5)
for char, valor in contador.items():
    print(f'O caractere {char} aparece {valor} vez(es)')