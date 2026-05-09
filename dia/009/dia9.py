#Cód.principal
import conversoes

opcoes = input('Informe qual conversão deseja realizar (C, F, K): ').lower()
numero = float(input('Informe o valor da temperatura: '))

if opcoes == 'c':
    resultado1 = conversoes.celcius_kelvin(numero)
    print(f'A conversão de {numero} em Celsius para Kelvin é {resultado1}')
    resultado2 = conversoes.celcius_fahrenheit(numero)
    print(f'A conversão de {numero} em Celsius para Fahrenheit é {resultado2}')
elif opcoes == 'f':
    resultado1 = conversoes.fahrenheit_celcius(numero)
    print(f'A conversão de {numero} em Fahrenheit para Celsius é {resultado1}')
    resultado2 = conversoes.fahrenheit_kelvins(numero)
    print(f'A conversão de {numero} em Fahrenheit para Kelvin é {resultado2}')
elif opcoes == 'k':
    resultado1 = conversoes.kelvin_celcius(numero)
    print(f'A conversão de {numero} em Kelvin para Celsius é {resultado1}')
    resultado2 = conversoes.kelvin_fahrenheit(numero)
    print(f'A conversão de {numero} em Kelvin para Fahrenheit é {resultado2}')
else:
    print('Erro!')
