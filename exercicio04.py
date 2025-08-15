'''
4- Um palíndromo é uma palavra ou frase que tenha a propriedade de poder ser lida tanto
da direita para a esquerda como da esquerda para a direita.
Exemplo: as strings "aaaaa", "1221", "bbaabb" são palíndromos, entretanto a string "chef"
não é um palíndromo.
Crie um programa que solicite uma palavra e indique se é um palíndromo ou não.
'''

palavra = input('Digite uma palavra: ')

palavra = palavra.lower()

inversa = palavra[::-1]

if palavra == inversa:
    print('Essa palavra é um palíndromo!')
else:
    print('Essa palavra não é um palíndromo...')