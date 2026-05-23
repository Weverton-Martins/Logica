#Controle de Orçamento (Foco: Inputs, Conversão de Dados e Condicionais)

'''Peça para o usuário digitar o orçamento total que ele tem disponível.
Calcule o valor total da compra.

Verifique se a compra coube no orçamento. Se coube, imprima o valor restante. Se passou, imprima um alerta dizendo que estourou o limite e mostre de quanto foi o prejuízo.'''

print('Controle de Orçamento')

orcamento_total = float(input('Informe sua renda disponivel: '))
produto1 = float(input('Informe o valor do primeiro produto: '))
produto2 = float(input('Informe o valor do segundo produto: '))
produto3 = float(input('Informe o valor do terceiro produto: '))
total = produto1 + produto2 + produto3 #calculo

if orcamento_total >= total:
    restante = orcamento_total - total
    print(f'Compra feita com sucesso, apos a compra seu saldo total é {restante}')

elif orcamento_total <= total:
    restante = orcamento_total - total
    print(f'ALERTA!! Limite estourado, passou {restante} do valor.')
else:
    print('Erro')

# Diário de Treino (Foco: Listas, Dicionários e Funções)
'''Crie uma lista chamada rotina contendo três dicionários. Cada dicionário representará um dia de treino com as chaves: "dia" (ex: Segunda), "foco" (ex: Upper ou Lower) e "exercicios" (um número inteiro, ex: 6).

calcular_volume que receba essa lista como parâmetro.
'''
#lista com os 3 dicionarios de rotinas
rotina = [
        {'dia': 'Segunda', 'foco': 'upper', 'exercicios': 6},
        {'dia': 'Terça', 'foco': 'Lower', 'exercicios': 5},
        {'dia': 'Segunda', 'foco': 'upper', 'exercicios': 4}
        ]

#função e soma do volume
def calcular_volume(rotina):
    soma_exercicios = 0
    for item in rotina:
        soma_exercicios += item['exercicios'] #quem_vai_guardar_o_resultado += valor_que_quero_adicionar.
    
    print(f'Realizado um rotal de {soma_exercicios} exercicios na semana.')

calcular_volume(rotina)