'''
6- Faça um programa em Python que contenha 3 listas com os nomes: valores, par e
impar. Solicite N números inteiros ao usuário e armazene-os na lista chamada valores
(utilize como critério de parada se o usuário deseja continuar).
§ Após a obtenção dos dados, na lista par armazene apenas os números pares da lista
valores e na lista ímpar os números ímpares. É obrigatório o uso de estrutura de
repetição e listas.
§ Exiba os números armazenados nas 3 listas.
'''

valores = []
par = []
impar = []

while True:
    n = int(input("Digite um número inteiro: "))
    valores.append(n)

    continuar = input("Deseja continuar? (s/n): ")
    if continuar.lower() == "n":
        break

for numero in valores:
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print("Todos os valores:", valores)
print("Números pares:", par)
print("Números ímpares:", impar)