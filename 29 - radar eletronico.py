velocidade = float(input('Qual a velocidade atual do carro? (Km)\t'))
if velocidade > 80:
    calculo1 = velocidade-80
    calculo2 = calculo1*7
    print('MULTADO! Você excedeu o limite de 80Km. Deverá pagar uma multa de R${}'.format(calculo2))
print('Tenha um Bom Dia! Dirija com cuidado!')
