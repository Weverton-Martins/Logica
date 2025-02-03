# Lista de Convidados

convidados = ["Joao", "Maria", "Pedro", "Bruno", "Rosa"]

for convidado in convidados:
    print(f"Permitido acesso: {convidado}")

# Estatísticas de Números
#Peça ao usuário para inserir uma lista de números (separados por espaço) e calcule:

entrada = input("Digite números separados por espaço: ")
numeros = [float(num) for num in entrada.split()]  #separa os numeros com base nos espaço

maior_numero = max(numeros)
menor_numero = min(numeros)
soma_numero= sum(numeros)
media_numero = soma_numero / len(numeros)

print("Maior número: ", maior_numero)
print("Menor número: ", menor_numero)
print("Soma dos números: ", soma_numero)
print("Média dos números: ", media_numero)

# Contagem de Caracteres em uma String

frase = input("Digite uma frase: ").lower()
letras= {} #Cria um dicionário vazio que armazenará as palavras e suas quantidades

for caracter in frase:
    if caracter.isalpha():
        if caracter in letras:
            letras[caracter] += 1
        else:
            letras[caracter] = 1

for letras, contagem in letras.items():
    print(f"A letra'{letras}' aparece {contagem} vez(es).")

# Trabalhando com Tuplas

meses = ("Janeiro", "Fevereiro", "Marco", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

num_mes= int(input("Digite um número para descobrir o mês correspondete entre 1 e 12: "))

if 1 <= num_mes <=12:
    print(f"O mês correspondente é {meses [num_mes - 1]}")
else:
    print("Número inválido. Por favor digite um número entre 1 e 12")

# Contando Palavras em um Texto

texto = input("Informe um texto: ").lower()
palavras =texto.split()  #Divide o texto em uma lista de palavras com base nos espaços entre elas.
cont_palavra = {} #Cria um dicionário vazio que armazenará as palavras e suas quantidades

for palavra in palavras:
    if palavra in cont_palavra:
        cont_palavra[palavra] += 1  #e a palavra já está no dicionário, incrementa o valor dela
    else:
        cont_palavra[palavra] = 1  #se não adiciona valor 1
print("\nContagem de Plavras")
for palavra, contagem in cont_palavra.items():
    print(f"A palavra '{palavra}' aparece {contagem} vez(es)")
