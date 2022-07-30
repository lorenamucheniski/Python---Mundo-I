km = float(input('Quantos km foram percorridos?'))
dia = int(input('Quantos dias o carro ficou alugado?'))
vkm = km * 0.15
vdia = dia * 60
print('Foram {} km percorridos e {} dias de aluguel. O valor a pagar é de {}'.format(km, dia, (vkm+vdia)))