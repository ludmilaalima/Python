numero = int(input('Digite um número inteiro qualquer:\t'))
print('Escolha uma das opções para que seja convertido:\n1 - Binário\n2 - Octal\n3 - Hexadecimal.')
escolha = int(input())
if escolha == 1:
    binario = bin(numero)
    print('O número {} em binário é {}'.format(numero, binario[2:]))
elif escolha == 2:
    octal = oct(numero)
    print('O número {} em octal é {}'.format(numero, octal[2:]))
elif escolha == 3:
    hexa = hex(numero)
    print('O número {} em hexadecimal é {}'.format(numero, hexa[2:]))
else:
    print('Escolha inválida! Tente novamente.')



