nome = input('Digite um nome:\t').lower().strip()
print('Analisando quantos (A) aparecem na frase...')
nome = nome.replace(' ', '')
print('A letra (A) aparece {} vezes na frase'.format(nome.count('a')))
print('A primeira letra (A) apareceu na {} posição\nA última letra (A) apareceu na {} posição'.format(nome.find('a')+1, nome.find('a', -1)+1))

