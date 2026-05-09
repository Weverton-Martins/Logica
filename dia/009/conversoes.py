"""
Biblioteca de Conversões Térmicas
Autor: Weverton
Descrição: Este módulo fornece funções para converter temperaturas entre 
as escalas Celsius, Fahrenheit e Kelvin.
"""
def celcius_kelvin(c):
    kelvin = c + 273.15
    return kelvin

def kelvin_celcius(k):
    celcius = k - 273.15
    return celcius

def celcius_fahrenheit(c):
    fahrenheit = (c * 1.8) + 32
    return fahrenheit

def fahrenheit_celcius(f):
    celcius = (f - 32)/1.8
    return celcius

def fahrenheit_kelvins(f):
    kelvins = ((f-32)/1.8) + 273.15
    return kelvins

def kelvin_fahrenheit(k):
    fahrenheit = (k-273.15)*1.8 + 32
    return fahrenheit