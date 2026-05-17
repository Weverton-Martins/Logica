#Tratamento de Exceções
try:
    numero = int(input('Digite um numero inteiro:'))
    resultado = 100/numero
except ValueError: #Captura erro se a entrada não for numeros inteiros
    print('Erro: Entrada invalida. Favor digite um numero inteiro.')
except ZeroDivisionError: #Captura quando há tentativas de divisão por zero
    print('Erro: Divisão por zero não pe permitido.')
else:
    print(f'O resultado é {resultado}')
finally:
    print('Operação finalizada!')

#1. Divisão Segura
#Escreva um programa que solicite dois números ao usuário e realize a divisão do primeiro pelo segundo. Trate as possíveis exceções, como divisão por zero e entrada inválida.

def divisorNumero():
    try:
        numero1 = int(input('Digite o primeiro numero inteiro: '))
        numero2 = int(input('Digite o segundo numero inteiro: '))
        resultado = numero1 / numero2
    except ValueError:
        print('Erro: Divisão apenas com numeros inteiros.')
    except ZeroDivisionError:
        print('Erro: Um dos numeros informados foi Zero')
    else:
        print(f'A divisão de {numero1} pelo {numero2} é: {resultado}')
    finally:
        print('Operação finalizada!')

divisorNumero()

#2. Abertura de Arquivo com Verificação
# Crie um programa que solicite ao usuário o nome de um arquivo para leitura. Tente abrir o arquivo e exibir seu conteúdo. Trate erros como arquivo não encontrado e permissão negada.

def aberturaArquivo():
    nome_arquivo = input('Informe o nome do arquivo')
    try:
        with open(nome_arquivo, 'r') as arquivo: #garantia que seja fechado automaticamente
            conteudo = arquivo.read() #ler o conteudoi
            print(conteudo)
    except FileNotFoundError:
        print('Erro: Arquivo não encontrado.')
    except PermissionError:
        print('Erro: Sem permissão para acesar o arquivo')
    except Exception as e:
        print(f'Erro: {e}')
    
aberturaArquivo()

#3. Conversão de Temperaturas com Validação
#Escreva um programa que converte temperaturas de Celsius para Fahrenheit. O programa deve validar a entrada do usuário, garantindo que seja um número.

def celsiusFahrenheit():
    try:
        temperatura = float(input('Informe a temperatura em Celcius a ser convertida para Fahrenheit: '))
        fahrenheit = (temperatura * 1.8) + 32
    except ValueError:
        print('Erro: Insira um valor numerico.')
    else:
        print(f'A conversção de {temperatura}ºC para Fahrenheit é {fahrenheit:.2f}ºF')
    
celsiusFahrenheit()

#Exercício: O Verificador de Portas

try:
    porta = int(input('Digite um número de porta: '))

except ValueError:
    print('Erro: Digite apenas numeros!')
finally:
    print('Encerrado com sucesso!')
''
# Exercício: Alerta de Brute Force

def analisar_login(tentativas):
    if tentativas > 5:
        raise ValueError('Alerta Crítico: Possível ataque de Brute Force detectado!') #criando um erro intencional
    return tentativas

print('Monitoramento Logs iniciando...')
try:
    analisar_login(3)
    print('Trafego Normal!')
except ValueError as erro: #impreme o erro mencionado no raise
    print(f'Incidente de segurança -> {erro}')

# 1. Calculadora com Tratamento de Exceções
# Crie uma calculadora que realiza operações básicas e trata possíveis erros de entrada.

def calculadora():

    try:
        numero1 = float(input('Informe o primeiro numero: '))
        operacao = input('Informe o que ira realizar (+,-,*,/): ')
        numero2 = float(input('Informe o primeiro numero: '))

        if operacao == '+':
            resultado = numero1 + numero2
        elif operacao == '-':
            resultado = numero1 - numero2
        elif operacao == '*':
            resultado = numero1 * numero2
        elif operacao == '/':
            resultado = numero1 / numero2
        else:
            raise ValueError('Operação invalida!')
   
    except ValueError as ve:
        print(f'Erro de valor: {ve}')
    except ZeroDivisionError:
        print('Erro: Divisão por Zero')
    else:
        print(f'Resultado da operação: {resultado}')
    finally:
        print('Encerrando programa...')

calculadora()

#Manipulação Segura de Listas
# Crie um programa que solicita ao usuário um índice e tenta acessar o elemento correspondente em uma lista predefinida. Trate exceções relacionadas a índices inválidos.

frutas = ['banana', 'uva', 'pera', 'morango'] #lista pra relacionar aos indecis

def seletor():
    try:
        indice = int(input('Informe o indice que deseja acessar: '))
        elemeto = frutas[indice]
    except ValueError:
        print('Erro: informe um valor inteiro!')
    except IndexError: #erro de indice fora do range da lista acima 
        print('Indicie informado fora do range da lista!')
    else:
        print(f'A fruta do indice {indice} é {elemeto}')
    finally:
        print('\nConcluindo programa!')

seletor()

#Sistema de Login Simples
# Implemente um sistema de login que solicita um nome de usuário e senha. Se o nome de usuário não existir ou a senha estiver incorreta, lance uma exceção personalizada.
class UsuarioNotFound(Exception): #Criando meus proprios erros, ele deve herdar todos os comportamentos do erro padrão (Exception)
    pass

class IncorrectPassword(Exception): #Criando meus proprios erros, ele deve herdar todos os comportamentos do erro padrão (Exception)
    pass
#dicionario
usuarios = {
    'admin' : 'admin', 
    'user' : '12345'
}

def login():

    try:
        usuario = input('Informe o usuario: ')
        senha = input('Informe a senha: ')

        if usuario not in usuarios: #verificando se o user existe no dicionario
            raise UsuarioNotFound ('Usuario não encontrado!')
        elif usuarios[usuario] != senha: # se a senha e compativel
            raise IncorrectPassword ('Senha incorreta!')

    except UsuarioNotFound as e: #pega as mensagens escritas no raise
        print(f'Erro: {e}')
    
    except IncorrectPassword as e:
        print(f'Erro: {e}')
    
    else:
        print('Acesso permitido')

login()
    
