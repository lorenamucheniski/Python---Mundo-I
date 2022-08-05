print('---------- CUSTO DA VIAGEM ----------')
distancia = int(input('Qual será a distância percorrida na sua viagem?'))
if distancia <= 200:
    preço1 = distancia * 0.50
    print('Você pagará R${} nessa viagem.'.format(preço1))
else:
    preço2 = distancia * 0.45
    print('Você pagará R${} nessa viagem.'.format(preço2))
