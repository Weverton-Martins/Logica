#1. Sistema de Estoque Simples (Dicionários)
'''Crie um programa que armazena o nome de 3 produtos e seus respectivos preços em um dicionário. Depois, peça ao usuário para digitar o nome de um produto. Se o produto existir, mostre o preço; se não, peça para ele cadastrar o preço desse novo item.'''

estoque = {"maca": 2.50, "banana": 1.99, 'pera': 3.00}

produto = input('Digite o nome de um produto: ').strip().lower()

if produto in estoque:
    print(f'O produto {produto} custa R${estoque[produto]:.2f}')
else:
    preco = float(input('Cadastre o preço desse novo produto: '))
    estoque[produto] = preco
    print('Produto adicionado com sucesso!')

print(estoque)

#O Clube de Leitores (Conjuntos/Sets)
'''Peça para o usuário digitar os nomes de 3 livros que ele leu este ano e guarde em um conjunto. Depois, peça para ele digitar os nomes de 3 livros que o melhor amigo dele leu e guarde em outro conjunto
'''

livros_user = set()
livros_friend = set()

for i in range(3):
    livro = input('\nInforme o livro que vocè leu: ').strip()
    livros_user.add(livro)

for i in range(3):
    livro = input('\nInforme o livro que seu amigo leu: ').strip()
    livros_friend.add(livro)

uniao = livros_user.union(livros_friend)
print(f'A união dos livros fica: {uniao}')

inter = livros_user.intersection(livros_friend)
print(f'A interseção dos livros fica: {inter}')

difer = livros_user.difference(livros_friend)
print(f'A diferença dos livros fica: {difer}')

#Agrupando por Categoria (Dicionários + Listas)
'''O Desafio: Imagine que você tem uma lista de nomes de alunos e suas notas: dados = [("Ana", 8), ("Beto", 5), ("Caio", 9), ("Duda", 4)]. Crie um dicionário que agrupe esses alunos em duas chaves: "Aprovados" (nota >= 7) e "Reprovados" (nota < 7).'''

dados = [("Ana", 8), ("Beto", 5), ("Caio", 9), ("Duda", 4)]

resultado = {"Aprovados": [], "Reprovados": []}

for nome,nota in dados:
    if nota >=7:
        resultado["Aprovados"].append(nome)
    else:
        resultado["Reprovados"].append(nome)

print(f'Lista de aprovadoos {resultado["Aprovados"]}')
print(f'Lista de reprovados {resultado["Reprovados"]}')
