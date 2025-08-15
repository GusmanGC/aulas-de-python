'''
7- Faça um programa que:
§ Leia duas listas com 5 inteiros cada.
§ Checa quais elementos da segunda lista são iguais a algum elemento da primeira
lista.
§ Se não houver elementos em comum, o programa deve informar isso.
Entrada Saída
[1, 2, 3, 4, 5]
[0, 7, 6, 10, 3]
3
Entrada Saída
[1, 2, 3, 4, 5]
[0, 7, 6, 10, 8]
Não há elemento em comum.
'''

lista1 = []
lista2 = []

for i in range(5):
    n = int(input('Digite um número para a lista 1: '))
    lista1.append(n)

for i in range(5):
    n = int(input('Digite um número para a lista 2: '))
    lista2.append(n)

numero_comum = []

for n in lista2:
    if n in lista1:
        numero_comum.append(n)

if numero_comum:
    for numero in numero_comum:
        print('O valor em comum nas duas listas é', numero)
else:
    print('Não há elemento em comum.')