#Crie um programa que leia o nome de uma pessoa e diga se o nome dela tem "Silva"
nome =str(input('Digite seu nome completo:')).strip().upper().split()
if 'SILVA' in nome:
    print('Seu nome tem Silva!')
else:
    print('Seu nome não tem Silva!')