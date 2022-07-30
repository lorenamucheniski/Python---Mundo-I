salario = float(input('Qual é o salário do funcionário?'))
novo = salario + (salario * 15 / 100)
print('O funcionário que tinha o salário de R${} com o aumento de 15% passará a receber {}'.format(salario, novo))