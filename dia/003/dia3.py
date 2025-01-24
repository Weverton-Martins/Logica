# Calculando troco
pao = 3.50
leite = 4.20
cafe = 2.80

total_compra = pao + leite + cafe

valor_pago = 20

troco = valor_pago - total_compra

print("Valor pago: R$", valor_pago)
print("Seu troco será de: R$", troco)


# Verificando prova do Enem 

# Aprovado se nota >= 7  e frequencia >= 75% 
nota = 7
frequencia = 75

aprovado = (nota >= 7) and (frequencia >= 75)
print("Aluno esta aprovado: ", aprovado)


# Oferta especial
# Desconto se comprar mais 10 itens OU comprar acima de 100

qtd_itens = 11
valor_total = 90

direito_desconto = (qtd_itens > 10) or (valor_total > 100)
print("Cliente tem direito ao desconto: ", direito_desconto)

# Acesso ao sistema
# senha correta E não pode estar bloqueado

senha_inserida = "abcd1234"
senha_correta = "abcd1234"
bloqueado = False

acesso_permitido = (senha_inserida == senha_correta) and (bloqueado == False)
print("Usuario pode acessar o destino? ", acesso_permitido)

# Divisão de Tarefas

conta = 150
amigos = 3

divisao_conta = conta / amigos 
resto_divisao = (conta % amigos) == 0
print("Valor divido para os 3 será de RS", divisao_conta)
print("Divisão foi exata sem resto ? ", resto_divisao)

# Classe etária
idade = int(input("Digite sua idade: "))

permitido = idade >= 16

print("Você pode assitir o filme? ", permitido)

# Calculadora de IMC
peso = float(input("Digite seu Peso em KG: "))
altura = float(input("Digite sua Altura em metros: "))

massa_corporal = peso / (altura ** 2)
peso_ideal = (massa_corporal >= 18.5) and (massa_corporal <= 24.9)

print("Seu IMC é: ", massa_corporal)
print("Estou no peso ideal? ", peso_ideal)

# par ou impar
numero = int(input("Insira um numero: "))

par = (numero % 2) == 0 

print("Meu numero é par: ", par)
