#alguns mini desafios de conclusão do curso
#Desafio 1: Calculo de fatorial com validação de entrada, valide a entrada e calcular fatorial por um loop

def calculo_fatorial():
    while True:
        try:
            numero = int(input('Informe um número inteiro: '))
            if numero < 0:
                print('Erro: Informe apenas numeros positivos!')
                continue
            break
        except ValueError:
            print('Entrada inválida!')

    fatorial = 1
    for i in range(1, numero+1):
           fatorial*=i
    print(f'O fatorial de {numero} é {fatorial}')
    
calculo_fatorial()

#Desafio 2: Contador de palavras em um texto, palavras separadas por espaços

def contador_palavras(texto):
     
    try:
        textos = texto.strip().split()
        #tambem poderia ter utilizado um return len(palavras)
        contador = {}
        for palavra in textos:
            if palavra in contador:
                contador[palavra] +=1
            else:
                contador[palavra] = 1

        print(contador)

    except AttributeError:
        print("Erro: Informe um texto válido.")

#teste 1 testando o contador 
contador_palavras('Weverton vai conseguir eu sei que vai')
#teste 2 testando o except 
contador_palavras(1234)


    