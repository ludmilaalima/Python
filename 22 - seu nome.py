nome = str(input('Digite seu nome completo:\t')).strip()
print('Analisando seu nome..... podemos ver que:\nSeu nome em MAIÚSCULAS: {}\nSeu nome em minúscilo: {}'.format(nome.upper(), nome.lower()))
nome_junto = nome.replace(" ", "")
separar_nome = nome.split()
print('Seu nome ao todo tem {} letras\nSeu primeiro nome é {} e tem {} letras'.format(len(nome_junto), separar_nome[0], len(separar_nome[0])))
