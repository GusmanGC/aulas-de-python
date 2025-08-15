'''
2- Faça um programa em Python que solicite um número inteiro de três algarismos e
imprima a soma desse número com seu inverso.
Exemplo:
Digite um número inteiro com três algarismos: 123
O inverso do número é: 321
A soma é: 123 + 321 = 444
'''

num = input('Digite um número inteiro de três algarismos: ')

inverso = num[::-1]

normal = int(num)
contrario = int(inverso)

soma = normal + contrario

print(f'A soma é {normal} + {contrario} = {soma}')