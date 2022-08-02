from random import randrange
computador = randrange(0,5)
print('Vou pensar em um número entre 0 e 5, tente adivinhar ....')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei?'))
if jogador == computador:
    print('PARABÉNS! Você acertou! :D')
else:
    print('Você errou! O número que eu pensei foi {}'.format(computador))