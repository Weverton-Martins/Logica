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
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
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
        raise ValueError('Alerta Crítico: Possível ataque de Brute Force detectado!')
    return tentativas

print('Monitoramento Logs iniciando...')
try:
    analisar_login(3)
    print('Trafego Normal!')
except ValueError as erro:
    print(f'Incidente de segurança -> {erro}')

    