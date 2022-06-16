primeiro = float(input('Digite um número:\t'))
segundo = float(input('Digite um número:\t'))
terceiro = float(input('Digite um número:\t'))
if primeiro > segundo and primeiro > terceiro:
    print('O primeiro é maior de todos!')
elif segundo > primeiro and segundo > terceiro:
    print('O segundo é o maior de todos!')
elif terceiro > primeiro and terceiro > segundo:
    print('O terceiro é o maior de todos!')
if primeiro < segundo and primeiro < terceiro:
    print('O primeiro é o menor número!')
elif segundo < primeiro and segundo < terceiro:
    print('O segundo é o menor número!')
elif terceiro < primeiro and terceiro < segundo:
    print('O terceiro é o menor número!')
else:
    print('Todos são iguais!')
