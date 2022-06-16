from random import choice
primeiro = input('Digite o primeiro nome:\t')
segundo = input('Digite o segundo nome: \t')
terceiro = input('Digite o terceiro nome:\t')
quarto = input('Digite o quarto nome:\t')
lista = [primeiro, segundo, terceiro, quarto]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))