"""
Faça um programa que leia algo pelo teclado e mostre na
tela o seu tipo primitivo e todas as informações possíveis
sobre ele.
"""
print('TIPOS PRIMITIVOS')

algo = input('Digite algo: ')

print('O tipo primitivo é: ',type(algo))
print('Só tem espaços? ',algo.isspace())
print('É um número? ',algo.isnumeric())
print('É alfabético? ',algo.isalpha())
print('Está em maiúsculas? ',algo.isupper())
print('Está em minúsculas? ',algo.islower())
print('Está capitalizada? ',algo.istitle())

