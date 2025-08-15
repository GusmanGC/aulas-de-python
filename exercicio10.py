'''
10- Criar um programa em Python que leia os dados necessários para cadastrar os nomes
de N alunos em uma lista, em outra lista as respectivas notas dos alunos e em uma
terceira lista o seu curso (ccp ou tads). Observe que na posição i das três listas ficarão
guardados: o nome do aluno i, a nota do aluno i e o curso do aluno i.
Resolva os seguintes itens:
a) Calcule e visualize a quantidade de alunos do curso de tads.
b) Calcule e visualize a média das notas dos N alunos.
c) Quantos alunos estão com a nota acima da média.
'''

nomes = []
notas = []
cursos = []

num = int(input('Digite a quantidade de alunos: '))

for i in range(num):
    nome = input(f"Digite o nome do {i+1}º aluno: ")
    nota = float(input(f"Digite a nota do {i+1}º aluno: "))
    curso = input(f"Digite o curso do {i+1}º aluno (ccp ou tads): ").strip().lower()

    nomes.append(nome)
    notas.append(nota)
    cursos.append(curso)

contar_tads = 0

for c in cursos:
    if c == "tads":
        contar_tads += 1

soma_notas = 0

for n in notas:
    soma_notas += n

media = soma_notas / num

acima_media = 0

for nota in notas:
    if nota > media:
        acima_media += 1

print(f"\nQuantidade de alunos do curso TADS: {contar_tads}")
print(f"Média geral das notas: {round(media, 2)}")
print(f"Quantidade de alunos com nota acima da média: {acima_media}")