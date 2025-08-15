'''
3- Elabore um programa em Python que leia uma string, converta para caixa alta e
imprima quantas vezes cada caractere aparece nessa string.
Exemplo:
Entrada:
• Entre com uma string: TTAAC
Saída:
• O caractere T aparece 2 vezes
• O caractere A aparece 2 vezes
• O caractere C aparece 1 vez
'''

texto = input('Digite uma palavra: ')

texto = texto.upper()

letras_verificadas = []

for letra in texto:
    if letra not in letras_verificadas:
        quantidade = texto.count(letra)
        print(f"O caractere {letra} aparece {quantidade} vezes")
        letras_verificadas.append(letra)
