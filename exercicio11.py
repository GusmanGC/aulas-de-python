'''
11- Elabore um programa em Python que leia os salários de 10 trabalhadores de uma
empresa e os armazene em uma lista. Após a entrada de dados, o programa deverá:
§ Calcular a média desses salários.
§ Determinar o maior dos salários desta empresa.
§ Contar os salários menores que R$850,00.
§ Exibir todos os resultados na tela.
'''

salarios = []

for i in range(10):
    salario = float(input(f'Digite o salário do {i+1}º trabalhador: '))
    salarios.append(salario)

soma_salario = 0

for s in salarios:
    soma_salario += s

media = soma_salario / len(salarios)

maior = max(salarios)

menor_850 = 0

for s in salarios:
    if s < 850:
        menor_850 += 1

print(f'A média dos salários da empresa é de: {round(media, 2)}')
print(f'O maior salário da empresa é de: R$ {round(maior, 2)}')
print(f'Os salários menores que R$850,00 são: {menor_850}')
print(salarios)