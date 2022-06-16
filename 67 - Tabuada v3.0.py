print('Digite um número negativo para sair!')
tabuada = int(input('Quer ver a tabuada de qual valor?\t'))
print('-'*50)
while True:
    if tabuada < 0:
        break
    for i in range(11):
        print(f'{tabuada} x {i} = {tabuada*i}')
    print('Digite um número negativo para sair!')
    tabuada = int(input('Quer ver a tabuada de qual valor?\t'))
    print('-' * 50)
print('Tabuada encerrada! Volte sempre.')

