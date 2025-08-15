'''
9- Faça um programa em Python que solicite ao usuário o dia da semana e o volume de
chuva correspondente a 10 dias. As informações obtidas devem ser armazenadas em 2
listas distintas (observe que cada lista poderá ter apenas 10 itens armazenados e que na
posição i das duas listas ficarão armazenados: o dia da semana i e o volume de chuva i). É
obrigatório o uso de estrutura de repetição e listas.
Em seguida, calcule e mostre o volume médio de chuva apenas do dia de semana igual a
quarta-feira e a soma total do volume de chuva, para isso utilize os dados armazenados
nas listas. É obrigatório o uso de estrutura de repetição e das listas do exercício descritas
anteriormente.
'''

dias_da_semana = []
volume_chuva = []

for i in range(10):
    dia = input(f"Digite o dia da semana do {i+1}º registro: ").strip().lower()
    volume = float(input(f"Digite o volume de chuva em milímetros do {i+1}º registro: "))

    dias_da_semana.append(dia)
    volume_chuva.append(volume)

soma_total = 0

for volume in volume_chuva:
    soma_total += volume

soma_quarta = 0
qntd_quarta = 0

for i in range(10):
    if dias_da_semana[i] == "quarta-feira":
        soma_quarta += volume_chuva[i]
        qntd_quarta += 1

if qntd_quarta > 0:
    media_quarta = soma_quarta / qntd_quarta
else:
    media_quarta = 0

print(f"A soma total da chuva nos 10 dias é de: {soma_total} milímetros")
print(f"A média de chuva nas quartas-feiras é de: {round(media_quarta, 2)} milímetros")