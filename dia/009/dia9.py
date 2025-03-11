import conversoes
import random

temperatura_c = float(input("Digite a temperatura em Celsius: "))
temperatura_f = conversoes.celsius_para_fahrenheit(temperatura_c)
temperatura_k = conversoes.celsius_para_kelvin(temperatura_c)

print(f"{temperatura_c}°C equivalem a {temperatura_f} °F em Fahrenheit e {temperatura_k} K em Kelvin")


def jogo_adivinha():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Bem-vindo ao jogo de Adivinhação")
    print("Tente adivinhar o número de 1 a 100.")

    while True:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        if palpite == numero_secreto:
            print(f"Parabens voce ganhou em {tentativas} tentativas")
            break
        elif palpite < numero_secreto:
            print("Muito baixo! Tente novamente.")
        else:
            print("Muito alto! Tente novamente")
      
jogo_adivinha()
