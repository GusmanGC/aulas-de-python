'''
1- Elabore um programa em Python que solicite o e-mail do usuário e imprima na tela
somente o domínio.
Exemplo:
Entre com seu e-mail: teste@uol.com.br
O domínio do seu e-mail é: http://uol.com.br
'''

email = input('Digite o seu e-mail: ')
partes = email.split('@')

partes[0]
partes[1]

print('Seu domínio é https://' + partes[1])

