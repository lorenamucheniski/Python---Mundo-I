import random
a1 = str(input('Nome do primeiro aluno(a):'))
a2 = str(input('Nome do segundo aluno(a):'))
a3 = str(input('Nome do terceiro aluno(a):'))
a4 = str(input('Nome do quarto aluno(a):'))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de apresentação sera: ')
print(lista)