'''
5- O Cebolinha é um menino muito esperto, mas tem dificuldades de dicção. O seu
problema é que toda vez que uma palavra tem um erre (R), ou dois erres (RR), ele o troca
por um ele (L). Queremos escrever um programa para saber como o Cebolinha falaria
uma palavra.
Exemplo:
Entrada: é uma única palavra que pode ou não conter
erres e está escrita em caixa alta: churrasqueiro
Saída: palavra como Cebolinha falaria: chulasqueilo
'''

palavra = input('Digite uma palavra: ')

palavra = palavra.lower()

cebolinha = palavra.replace('r', 'l')

print(f'Como o cebolinha falaria a palavra {palavra}? ele falaria', cebolinha)

