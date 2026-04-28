#Pratica dia 06
'''
Crie uma lista com nomes de convidados para uma festa. Exiba uma mensagem
personalizada para cada convidado.
'''

convidados = ['João', 'Maria', 'Beto', 'Ana']

for convidado in convidados:
    print(f'Olá {convidado} você está convidado para a festa!')

'''
Peça ao usuário para inserir uma lista de números (separados por espaço) e calcule:
● O maior número
● O menor número
● A soma dos números
● A média dos números
'''

numero = input('Informe uma lista de numeros separado por espaços: ')
lista = [float(num) for num in numero.split()]

maior_numero = max(lista)
menor_numero = min(lista)
soma_numero = sum(lista)
media_numero = soma_numero / len(lista)

print('Maior numero: ', maior_numero)
print('Menor numero: ', menor_numero)
print('Soma dos numero: ', soma_numero)
print('Media dos numero: ', media_numero)

'''Peça ao usuário para inserir uma frase e conte quantas vezes cada letra aparece.'''

frase = input('Informe uma frase: ').lower()
letras = {}

for char in frase:
    if char.isalpha():
        if char in letras:
            letras[char] +=1
        else:
            letras[char] = 1

for letra, contagem in letras.items():
    print(f'A letra {letra} aparece {contagem} vez(es).')

'''Peça ao usuário para inserir uma lista de números (separados por espaço) e exiba a lista
em ordem crescente e decrescente'''

entrada = input('Informe uma lista de numeros separa por espaço: ')
numeros = [float(num) for num in entrada.split()]

numeros.sort() #crescente
print(f'Numeros em ordem crescente: {numeros}')

numeros.sort(reverse=True) #decrescente
print(f'Numeros em ordem decrescente: {numeros}')

'''Crie uma tupla com nomes de meses do ano. Peça ao usuário um número entre 1 e 12 e
exiba o nome do mês correspondente.'''

tupla_meses = ('Janeiro', 'Fevereiro','Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

numero = int(input('Informe um número entre 1 e 12: '))
indice = numero - 1

print(f'O mês correspondnete é {tupla_meses[indice]}')

'''Desafios Extras'''
# Lista de Tarefas

'''Crie um programa que gerencia uma lista de tarefas. O usuário deve ser capaz de:
● Adicionar uma tarefa
● Remover uma tarefa
● Listar todas as tarefas'''

tarefa = []


while True:
    print('___Lista de Tarefas___')
    print('Selecione a opção desejada:')
    print('1 - Adicionar uma tarefa')
    print('2 - Remover uma tarefa')
    print('3 - Listar todas as tarefas')
    print('4 - Sair\n')
    
    opcao = int(input('Informe o que deseja realizer: '))

    if opcao == 1:
            taf = input('Informe a tarefa a ser adicionada: ')
            tarefa.append(taf)
            print('Tarefa adicionada com sucesso!\n')

    elif opcao == 2:
            remover = input('Informe qual tarefa remover: ').lower()
            if remover in tarefa:
                   tarefa.remove(remover)
                   print('Tarefa removida com sucesso.\n')
            else:
                   print('Tarefa não encontrada\n')
    elif opcao == 3:
           print(tarefa)
    
    else:
           print('Saindo...')
           break
    
'''Crie um programa que recebe as notas dos alunos em uma lista e:
● Exibe a maior e a menor nota.
● Calcula a média da turma.
● Exibe as notas acima da média.'''

notas = []

while True:
    print('___Notas___')
    print('Selecione a opção desejada:\n')
    print('1 - Adicionar uma nota')
    print('2 - Exibir a maior e a menor nota')
    print('3 - Calcula a média da turma.')
    print('4 - Exibe as notas acima da média.')
    print('5 - Sair\n')

    opcao = int(input('Informe o que deseja realizar: '))

    if opcao == 1:
           nota = int(input('Informe a nota a ser adicionada: '))
           notas.append(nota)
           print('Nota adicionada com sucesso!\n')
    elif opcao == 2:
           maior_nota = max(notas)
           menor_nota = min(notas)
           print(f'A maior nota é {maior_nota} a menor nota é {menor_nota}\n')
    elif opcao ==3:
           soma_notas = sum(notas)
           media_nota = soma_notas / len(notas)
           print(f'A média da turma é {media_nota}\n')
    elif opcao == 4:
           for n in notas:
                  if n > media_nota:
                         print(f'Notas acima da média: {n}')
    elif opcao == 5:
           print('Saindo...')
           break
    else:
           print('Opção invalida!')

'''Peça ao usuário para inserir um texto e conte quantas vezes cada palavra aparece.''' 

texto = input('Informe um texto: ').lower()
palavra = texto.split()
contagem = {}

for palavras in palavra:
    if palavras in contagem:
        contagem[palavras] += 1
    else:
        contagem[palavras] = 1

print('___Contagem de Palavras___')
for palavras, cont in contagem.items():
    print(f'A {palavras} apareceu {cont} vez(es)')


    



