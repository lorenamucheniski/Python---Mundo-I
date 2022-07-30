preco = float(input('Qual o valor do produto?'))
novo = preco - (preco * 5 / 100 )
print('O preço do produto era de {} , com 5% de desconto na promoção passou a ser {}.'.format(preco, novo))