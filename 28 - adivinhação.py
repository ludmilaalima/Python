import random
from time import sleep
print('************** Estou pensando em um número de 1 a 5, tente adivinhar! **************')
numero = int(input('Em que número eu pensei?\t'))
print('Processando.....')
sleep(3)
numero_escolhido = random.randint(1,5)
if numero_escolhido == numero:
    print('Parabéns! Você finalmente me venceu!')
else:
    print("Hmmm, parece que você errou! Eu pensei no número {} e não no {}".format(numero_escolhido, numero))


