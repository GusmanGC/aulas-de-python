'''
8- Faça um programa em Python que solicite ao usuário a placa e o valor da multa de 15
carros. As informações obtidas devem ser armazenadas em 2 listas distintas.
0 AAA-1234
1 CCC-1234
2 AAA-1234
3 DDD-1234
...
14 BBB-1234
0 880.41
1 1467.35
2 293.47
3 293.47
...
14 2934.70
É obrigatório o uso de estrutura de repetição e listas.
Calcule e mostre e o valor médio de todas as multas e
quantos carros possuem o valor de multa maior ou
igual a R$300.00, para isso utilize os dados
armazenados nas listas descritas anteriormente e
estrutura de repetição.
'''

placas = []
multas = []

for i in range(2):
    placa = input(f"Digite a placa do {i+1}º carro: ")
    valor = float(input(f"Digite o valor da multa do {i+1}º carro: R$ "))

    placas.append(placa)
    multas.append(valor)

soma = 0

for valor in multas:
    soma += valor

media = valor / len(multas)

acima_300 = 0

for valor in multas:
    if valor >= 300:
        acima_300 += 1

print(f" A média das multas é: R$ {round(media, 2)}")
print(f"A quantidade de multas acima ou iguais a R$ 300: {acima_300}")