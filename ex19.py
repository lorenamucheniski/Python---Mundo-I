print('---------- RADAR ELETRÔNICO ----------')
print('=-=' * 15)
velocidade = int(input('Qual é a velocidade atual do carro?'))
if velocidade > 80:
    multa = (velocidade-80) * 7.0
    print('VOCÊ FOI MULTADO! A máxima permitida é de 80 km/h.')
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')

